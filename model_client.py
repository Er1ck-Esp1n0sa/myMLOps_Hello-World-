import json
import streamlit as st
import requests


SERVER_URL = 'https://linear-model-service-er1ck-esp1n0sa.cloud.okteto.net/v1/models/linear-model:predict'

def make_prediction(inputs):
    # x = int(inputs[0])
    # y = x ** 2 + 1
    # return {'predictions': [[y]]}
    predict_request = {'instances': [inputs]}
    response = requests.post(SERVER_URL, json=predict_request)
    response.raise_for_status()
    prediction = response.json()
    return prediction

def main():
    st.title('Calculador de Ecuaciones')

   
    x = st.number_input('Ingrese el valor de X:', min_value=0.0, step=1.0)

   
    if st.button('Calcular'):
        prediction = make_prediction([x])
        st.write(f'Resultado de la ecuación: {prediction["predictions"][0][0]}')

if __name__ == '__main__':
    main()