FROM python:latest 

RUN pip install huggingface_hub
#RUN pip install -U "huggingface_hub[cli]"

RUN huggingface-cli login --token $HUGGINGFACE_TOKEN

# RUN pip install joblib
# RUN pip install numpy

CMD python3
