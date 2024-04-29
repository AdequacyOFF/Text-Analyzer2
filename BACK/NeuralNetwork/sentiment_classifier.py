from transformers import BertTokenizer, BertForSequenceClassification
import NeuralNetwork.utils as U
from pymystem3 import Mystem

import os
import torch
import numpy as np
import gdown

class SentimentClassifier:
    def __init__(self, device='cpu'):
        # Device of the model
        self.device = device
        
        # Classification labels
        self.labels = ['neutral', 'joy', 'sadness', 'surprise', 'fear', 'anger']
        
        # Define parent directory for finding path to model checkpoint
        # and file with profanity 
        self.parent_dir = os.path.dirname(os.path.abspath(__file__))
        path_to_ckp = os.path.join(self.parent_dir, 'ckp')
        
        # If directory with model was not found
        if not os.path.exists(path_to_ckp):
            print('\nNo local neural network model files were found. Install them using the URL.\n')
            url = "https://drive.google.com/drive/folders/11r4dcUjVBCg0mJHfyhyWffTyYQHNhx7O?usp=drive_link"
            gdown.download_folder(url, output=path_to_ckp)
        
        # Load model
        self.tokenizer = BertTokenizer.from_pretrained(path_to_ckp)
        self.model = BertForSequenceClassification.from_pretrained(path_to_ckp, num_labels=len(self.labels),
                                                                   problem_type='multi_label_classification')
        # Put model on the device
        self.model.to(self.device)
        
        # Define path to file with profanity
        blacklist_path = os.path.join(self.parent_dir, 'blackwords.txt')
        
        self.blacklist = []
        
        # If file with profanity isn't found - disable profanity analys
        if not os.path.exists(blacklist_path):
            print('\nLocal file with profanity is not found. Disable profanity analys.\n')
        else:
            with open(blacklist_path, 'r', encoding='utf8') as f:
                for line in f.readlines():
                    self.blacklist.append(line[:-1])
                    
        self.lemmatizer = Mystem()
            
        
    def out(self, text):
        # Get embeddings from the tokenizer
        encoding = self.tokenizer.encode_plus(text,
            add_special_tokens=True,
            max_length=512,
            return_token_type_ids=False,
            truncation=True,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt'
        )
        
        out = { 'text': text,
                'input_ids': encoding['input_ids'].flatten(),
                'attention_mask': encoding['attention_mask'].flatten() 
                }
        
        input_ids = out["input_ids"].to(self.device)
        attention_mask = out["attention_mask"].to(self.device)
        
        # Pass data throw thr model
        outputs = self.model(
            input_ids=input_ids.unsqueeze(0),
            attention_mask=attention_mask.unsqueeze(0)
        )
        
        return torch.softmax(outputs.logits, dim=1).view(-1).cpu().detach()
    
    def analys(self, text):
        # Get probabilities from the model
        probs = self.out(text)
        
        # Define prediction of the model
        prediction = self.labels[torch.argmax(probs)]
        
        preds = probs.numpy()
        
        # Convert probabilities to percents
        neutral_percent = round(preds[0] * 100, 2)
        joy_percent = round(preds[1] * 100, 2)
        sadness_percent = round(preds[2] * 100, 2)
        surprise_percent = round(preds[3] * 100, 2)
        fear_percent = round(preds[4] * 100, 2)
        anger_percent = round(preds[5] * 100, 2)
        
        profanity_flag = False
        
        # Check text for profanity
        profanity_flag = bool(U.find_profanity(text, self.blacklist, self.lemmatizer))
        
        return (text, prediction, neutral_percent, joy_percent, sadness_percent, 
                surprise_percent, fear_percent, anger_percent, profanity_flag)
    
    def summary(self, text, sen_num=2):
        # Split text on pairs of <sen_num> sentences
        sentences = U.sentencer(text, sen_num)
        
        # Mean probabilities for all classes
        total = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        
        result = []
        
        # Iterate on sentences
        for sentence in sentences:
            out = self.analys(sentence)
            result.append(out)
            
            total += np.array([out[2], out[3], out[4], out[5], out[6], out[7]])
            
        total /= len(result)
            
        total_list = [round(total[0], 2),
                      round(total[1], 2),
                      round(total[2], 2),
                      round(total[3], 2),
                      round(total[4], 2),
                      round(total[5], 2)]
            
        return result, total_list
    
    