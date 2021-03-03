import os 
import streamlit
import pandas as pd 
import numpy as np 
import pickle 
import tensorflow 
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow.keras.models
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import re
import json
from gensim.parsing.preprocessing import remove_stopwords
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



#Loading tokenizer in json format
with open('tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)
    
#Loading the model and its weights
json_file = open('model.json','r')    
loaded_model_file = json_file.read()
json_file.close()
glove_embedding_model = model_from_json(loaded_model_file)
glove_embedding_model.load_weights('model.h5')


#Now we create a helper function to clearn the input review tokenize it, and pad the sequences. 
#Once its convrted into numerical form, we will use the loaded model to make the sentiment predictions

def senitment_prediction(review):
    sentiment = []
    input_review = [str(review)]
    input_review = [x.lower() for x in input_review]
    input_review = [re.sub('[^a-zA-z0-9\s]','',x) for x in input_review]

    input_feature = tokenizer.texts_to_sequences(input_review)
    input_feature = pad_sequences(input_feature, maxlen=50000, padding='pre')
    sentiment = glove_embedding_model.predict(input_feature)[0]
    
    if (np.argmax(sentiment) == 0):
        preds = 'Negative'
    else:
        preds = 'Positive'
        
    return preds


sent = ['NLP is good']
senitment_prediction(sent)

def run():
    streamlit.title("Sentiment Analysis - Glove/LSTM Model")
    html_temp = """ """
    streamlit.markdown(html_temp)
    tweet = streamlit.text_input("Enter The Review")
    prediction = ""
    
    if streamlit.button("Predict Sentiment"):
        prediction = senitment_prediction(tweet)
    streamlit.success("The sentiment predicted by Model:{}".format(prediction))
    

if __name__ == '__main__':
    run()   