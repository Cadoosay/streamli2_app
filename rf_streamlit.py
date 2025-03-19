import streamlit as st
import joblib
import numpy as np

model = joblib.load('RF_class.pkl')

def main():
    st.title('Machine Learning Model Deployment')
    
    sepal_length = st.slider('sepal_length',min_value=0.0, max_value=10.0,value=0.1)
    sepal_width = st.slider('sepal_width',min_value=0.0, max_value=10.0,value=0.1)
    patal_length = st.slider('patal_length',min_value=0.0, max_value=10.0,value=0.1)
    patal_width = st.slider('patal_width',min_value=0.0, max_value=10.0,value=0.1)
    
    if st.button('Make Predictions'):
        features = [sepal_length,sepal_width,patal_length,patal_width]
        result = make_prediction(features)
        st.success(f'The prediction is: {result}')
        
def make_prediction(features):
    input_array = np.array(features).reshape(1,-1)
    prediction = model.predict(input_array)
    return prediction[0]

if __name__ == '__main__':
    main()
    