[TF Serving docker hub](https://hub.docker.com/r/tensorflow/serving)

[How to serve](https://github.com/tensorflow/serving/blob/master/tensorflow_serving/g3doc/docker.md)

[Manual](https://huggingface.co/blog/tf-serving)

The main idea is to run models from huggingface with [TensorFlow Serving](https://www.tensorflow.org/tfx/serving/docker).
For this we need to [build](https://huggingface.co/docs/transformers/main_classes/model#transformers.PreTrainedModel.from_pretrained) and [save](https://huggingface.co/docs/transformers/main_classes/model#transformers.PreTrainedModel.save_pretrained) an instance from this model and then put it to serve.

Transformer for this should start with TF so it produce tensorflow saved model not pytorch. For example `TFAutoModelForQuestionAnswering` for popular Bert model `deepset/roberta-base-squad2`.

To check the state of saved model:

```bash
saved_model_cli show --dir /models/model/1 --tag_set serve --signature_def serving_default
```

[Model](https://huggingface.co/distilbert/distilbert-base-uncased-distilled-squad)
