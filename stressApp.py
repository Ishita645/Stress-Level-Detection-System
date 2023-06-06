import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open('path','rb'))
#creating a function
def stress_prediction(input_data):
 
 # changing the input_data to numpy array
 input_data_as_numpy_array = np.asarray(input_data)
 input_data_as_numpy_array = input_data_as_numpy_array.astype(np.float64)
 # reshape the array as we are predicting for one instance
 input_data_reshaped = [input_data_as_numpy_array]
 prediction = loaded_model.predict(input_data_reshaped)
 print(prediction)
 if (prediction[0] == 0):
 return 'The person is not stressed'
 elif (prediction[0] == 1):
 return 'The person is slightly stressed'
 elif (prediction[0] == 2):
 return 'The person is stressed'
 elif(prediction[0]==3):
 return 'The person is highly stressed'
 
 
def main():
 # giving a title
 st.title('Stress level predictor')
 
 
 # getting the input data from the user
 
 body_temperature = st.text_input('Body temperature')
 limb_movement = st.text_input('Limb movement')
 Blood_oxygen = st.text_input('Blood oxygen')
 Sleeping_hours = st.text_input('Sleeping hours')
 Heart_rate = st.text_input('Heart rate')
 
 
 # code for Prediction
 diagnosis = ''
 
 # creating a button for Prediction
  if st.button('Predict stress'):
    diagnosis = stress_prediction([body_temperature, limb_movement, 
Blood_oxygen, Sleeping_hours, Heart_rate])
 
 
 st.success(diagnosis)
 
 
if __name__ == '__main__':
 main()

