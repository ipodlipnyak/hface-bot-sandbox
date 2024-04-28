#!/bin/python3
import requests
import json

headers = {"content-type": "application/json"}
url = 'http://localhost:8501/v1/models/model:predict'

# @see https://www.tensorflow.org/tfx/serving/api_rest#request_format_2
# data = {
#         'inputs': {
#             'attention_mask': [[1, 1, 1, 1, 1, 1, 1, 1, 1]],
#             'input_ids': [[101, 2129, 2052, 2017, 2360, 4875, 1999, 3059, 102]],
#             'question': 'Why is model conversion important?',
#             'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
#             }
#         }

# data = {
#         "options": {
#             "n_best": True,
#             "n_best_size": 3,
#             "max_answer_length": 30
#             },
#         "data": [
#             {
#                 "id": "001",
#                 "question": "Who invented LSTM?",
#                 "context":  "Many aspects of speech recognition were taken over by a deep learning method called long short-term memory (LSTM), a recurrent neural network published by Hochreiter and Schmidhuber in 1997.[51] LSTM RNNs avoid the vanishing gradient problem and can learn \"Very Deep Learning\" tasks[2] that require memories of events that happened thousands of discrete time steps before, which is important for speech. In 2003, LSTM started to become competitive with traditional speech recognizers on certain tasks.[52] Later it was combined with connectionist temporal classification (CTC)[53] in stacks of LSTM RNNs.[54] In 2015, Google's speech recognition reportedly experienced a dramatic performance jump of 49% through CTC-trained LSTM, which they made available through Google Voice Search."
#                 }
#             ]
#         }

data = {
        'inputs': {
            'attention_mask': [[1]],
            'input_ids': [[101]]
            }
        }
data = {
        "instances": [{
            'question': "who"
            }]
        }
data = json.dumps(data)
r = requests.post(url, data=data, headers=headers)
print(r.text)
