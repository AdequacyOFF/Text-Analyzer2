from transformers import BertTokenizer, BertForSequenceClassification
import utils as U

import os
import gdown
import torch
import numpy as np

class SentimentClassifier:
    def __init__(self, device='cpu'):
        self.device = device
        
        self.labels = ['neutral', 'joy', 'sadness', 'surprise', 'fear', 'anger']
        
        self.parent_dir = os.path.dirname(os.path.abspath(__file__))
        path_to_ckp = os.path.join(self.parent_dir, 'sentim_ckp')
        
        if not os.path.exists(path_to_ckp):
            print('\nNo local neural network model files were found. Install them using the URL.\n')
            url = "https://drive.google.com/drive/folders/11r4dcUjVBCg0mJHfyhyWffTyYQHNhx7O?usp=drive_link"
            gdown.download_folder(url, output=path_to_ckp)
        
        self.tokenizer = BertTokenizer.from_pretrained(path_to_ckp)
        self.model = BertForSequenceClassification.from_pretrained(path_to_ckp, num_labels=len(self.labels),
                                                                   problem_type='multi_label_classification')
        self.model.to(self.device)
        
    def out(self, text):
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
        
        outputs = self.model(
            input_ids=input_ids.unsqueeze(0),
            attention_mask=attention_mask.unsqueeze(0)
        )
        
        return torch.softmax(outputs.logits, dim=1).view(-1).cpu().detach()
    
    def analys(self, text):
        probs = self.out(text)
        
        prediction = self.labels[torch.argmax(probs)]
        
        preds = probs.numpy() * 100
        
        neutral_percent = round(preds[0], 2)
        joy_percent = round(preds[1], 2)
        sadness_percent = round(preds[2], 2)
        surprise_percent = round(preds[3], 2)
        fear_percent = round(preds[4], 2)
        anger_percent = round(preds[5], 2)
        
        return (text, prediction, neutral_percent, joy_percent, sadness_percent, surprise_percent, fear_percent, anger_percent)
    
    def summary(self, text, sen_num=2):
        sentences = U.sentencer(text, sen_num)
        
        total = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        
        result = []
        
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
    