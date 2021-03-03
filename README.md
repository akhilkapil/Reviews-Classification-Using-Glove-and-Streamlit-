# Text Classification With Glove/Streamlit/Docker
 
<br/>

## Project Overview 

Classified movie reviews into positive and negative with GloVe embeddings and machine learning techniques.
<br/>

This project showcases the use of `Glove Embedding's` and `Streamlit` in tandem. The trained model is deployed using a Streamlit rest service containerized using Docker. The front end UI is built on Streamlit which is hosted on its own `Docker` container.

![Alt Text](https://github.com/akhilkapil/Reviews-Classification-Using-Glove-and-Streamlit-/blob/main/app.PNG)

## Model Overview
For this project, I am using GloVe embedding with two  layer of bidirectional LSTM followed by fully connected layer for prediction. There were other great ideas as to how to go about modeling, 1D ConvNet + LSTM and traditional ML techniques like SVM for example. But I am sticking with deep learning approach. One thing to note is that this dataset seems to be prone to overfitting. Even slight complexity to the model showed signs of overfitting. The model was trained using google colab's GPU.

## Run the app with Docker 

Launch th streamlit app with docker:<br/>
         
          docker build -t myapp:latest .
          docker run -p 8501:8501 myapp
          streamlit run apps.py

the network will automatically after this. If not then visit http://localhost:8501/ 
