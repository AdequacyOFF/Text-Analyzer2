import re


def sentencer(text:str, num_sen=1):
    split_regex = re.compile(r'[.|!|?|…|!?]')
    splitted = list(filter(lambda t: t, [t.strip() for t in split_regex.split(text)]))
    
    if num_sen == 1:
        return splitted
    
    final_splitted = []
    
    i = 0
    while (i + num_sen) < len(splitted):
        string = ''
        for j in range(num_sen):
            var = splitted[i + j] + ' '
            string += var
            
        final_splitted.append(string)
        i += num_sen
        
    end_string = ''
    for j in range(len(splitted) - i):
        var = splitted[i + j] + ' '
        end_string += var
        
    if end_string != '':
        final_splitted.append(end_string)
        
    return final_splitted
    