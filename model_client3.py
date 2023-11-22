import json
import streamlit as st
import requests

SERVER_URL = 'https://linear-model-service-er1ck-esp1n0sa.cloud.okteto.net/v1/models/linear-model:predict'

def make_prediction(inputs):
    # Estructura de la solicitud al modelo en Okteto
    predict_request = {'instances': [inputs]}
    
    # Hacer la solicitud al modelo en Okteto
    response = requests.post(SERVER_URL, json=predict_request)
    response.raise_for_status()
    
    # Parsear la respuesta JSON
    prediction = response.json()
    
    # Devolver la predicción
    return prediction

def main():
    st.title('Calculador de Tiempo de Entrega de un proyecto')
    st.title('y = mx + b')

    x = st.number_input('Ingrese el numero de lineas:', min_value=0.0, step=1.0)

    if st.button('Calcular'):
        # Hacer una solicitud al modelo en Okteto
        prediction = make_prediction([x])
        # Obtener la predicción y asegurarse de que no sea negativa
        estimated_time = max(prediction['predictions'][0][0], 0)
        st.write(f'Tiempo de entrega estimado por el modelo: {prediction["predictions"][0][0]} horas')

if __name__ == '__main__':
    main()
