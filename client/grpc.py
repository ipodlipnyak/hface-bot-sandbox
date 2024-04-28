#!/bin/python3

import grpc
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc

hostport = "127.0.0.1:8500"
channel = grpc.insecure_channel(hostport)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)model_request = predict_pb2.PredictRequest()
model_request.model_spec.name = 'bert-qa'string_record = tf.python_io.tf_record_iterator(path=predict_file)model_request.inputs['examples'].CopyFrom(
   tf.contrib.util.make_tensor_proto(string_record,
            dtype=tf.string,
            shape=[batch_size])
   )
result_future = stub.Predict.future(model_request, 30.0)  
raw_result = result_future.result().outputs
