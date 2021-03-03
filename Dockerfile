FROM python:3.7
WORKDIR /Sentiment
COPY ./requirements.txt /Sentiment
RUN pip3 install -r requirements.txt
EXPOSE 8501
COPY ./apps.py /Sentiment
COPY ./model.h5 /Sentiment
COPY ./model.json /Sentiment
COPY ./tokenizer.json /Sentiment
CMD ["python","apps.py"]