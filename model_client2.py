import json
import streamlit as st
import requests

# URL del servidor que proporciona el servicio de predicción
SERVER_URL = 'https://linear-model-service-er1ck-esp1n0sa.cloud.okteto.net/v1/models/linear-model:predict'

# Función para realizar la predicción
def make_prediction(advertising_expenses):
    predict_request = {'instances': [advertising_expenses]}
    response = requests.post(SERVER_URL, json=predict_request)
    response.raise_for_status()
    prediction = response.json()
    return prediction

# Función principal
def main():
    st.title('Calculador de Ventas de Proyectos')

    # Entrada: Gasto en publicidad
    advertising_expenses = st.number_input('Ingrese numero de lineas de codigo:', min_value=0.0, step=1.0)

    # Botón para realizar la predicción
    if st.button('Calcular'):
        # Hacer la predicción utilizando el modelo
        prediction = make_prediction([advertising_expenses])
        
        # Asegurarse de que el resultado no sea negativo
        estimated_sales = max(0, prediction["predictions"][0][0])

        # Mostrar el resultado en la interfaz de usuario
        st.write(f'Estimación de Ventas: {estimated_sales}')

# Verificar si el script se ejecuta directamente
if __name__ == '__main__':
    main()