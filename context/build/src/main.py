# from transformers import TFAutoModelForQuestionAnswering
# model_name = "deepset/roberta-base-squad2"
# model = TFAutoModelForQuestionAnswering.from_pretrained(model_name)
# 
# model.save_pretrained("/models/roberta", saved_model=True)
# 
# 
# from transformers import DistilBertTokenizer, TFDistilBertForQuestionAnswering
# import tensorflow as tf
# 
# tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-distilled-squad")
# model = TFDistilBertForQuestionAnswering.from_pretrained("distilbert-base-uncased-distilled-squad")
# 
# question, text = "Who was Jim Henson?", "Jim Henson was a nice puppet"
# 
# inputs = tokenizer(question, text, return_tensors="tf")
# outputs = model(**inputs)
# 
# answer_start_index = int(tf.math.argmax(outputs.start_logits, axis=-1)[0])
# answer_end_index = int(tf.math.argmax(outputs.end_logits, axis=-1)[0])
# 
# predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
# tokenizer.decode(predict_answer_tokens)

from huggingface_hub import hf_hub_download
import joblib

REPO_ID = "distilbert/distilbert-base-uncased-distilled-squad"
FILENAME = "384-8bits.tflite"

model = joblib.load(
    hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
)
