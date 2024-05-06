import easyocr
import cv2

class ImageReader:
    def __init__(self):
        self.reader = easyocr.Reader(['ru']) 
        
    def read(self, path):
        img = self.get_img(path)
        
        texts = []
        probs = []
        
        for i in range(4):
            result = self.reader.readtext(img)
            
            text_str = ''
            prob = 0.0
            
            for sample in result:
                prob += sample[2]
                
                if(sample[2] < 0.8):
                    continue
                else:
                    text_str += (sample[1] + ' ')
                    
            texts.append(text_str)
            probs.append(prob / len(result))
            
            img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            
        max_index = 0
        max_elem = max(probs)
        
        for i in probs:
            if i == max_elem:
                break
            else:
                max_index += 1
        
        return texts[max_index]
    
    def get_img(self, path):
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        return img
            
