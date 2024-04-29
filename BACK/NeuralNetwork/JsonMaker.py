import json
import numpy as np

def makeJson(result, total_list):
        total_dict_values = []
        for num in total_list:
            total_dict_values.append(num.astype(np.float64))
        total_dict_keys = ["total_neutral_percent", "total_joy_percent", "total_sadness_percent", "total_surprise_percent", "total_fear_percent", "total_anger_percent"]
        total_dict = dict(zip(total_dict_keys, total_dict_values))
        answer_list = []
        for data in result:
            centence_dict_keys = ["text", "conclusion", "neutral_percent", "joy_percent", "sadness_percent", "surprise_percent", "fear_percent", "anger_percent", "profanity_flag"]
            centence_dict_values = [data[0], data[1], data[2].astype(np.float64), data[3].astype(np.float64), data[4].astype(np.float64), data[5].astype(np.float64), data[6].astype(np.float64), data[7].astype(np.float64), data[8]]
            centence_dict = {"sentence "+str(result.index(data)): dict(zip(centence_dict_keys, centence_dict_values))}
            answer_list.append(centence_dict)
        answer_list.append(total_dict)
        return json.dumps(answer_list, ensure_ascii=False, sort_keys=False)