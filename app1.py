import streamlit
from PIL import Image

with open('modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)
#cols=['NALA_DIA', 'RALLY_DIA', 'NALA_DOM', 'RALLY_DOM', 'PINKIE_DOM']
def welcome():
    return 'Bienvenido'

def prediccion(NALA_DIA, RALLY_DIA, NALA_DOM, RALLY_DOM,PINKIE_DOM):  
    prediccion=1*(modelo.predict(
        [[NALA_DIA, RALLY_DIA, NALA_DOM, RALLY_DOM,PINKIE_DOM]])[:,0]>=4)
    print(prediccion)
    return prediccion
def main():
      # giving the webpage a title
    streamlit.title("Trading Predicción")
      
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Clasificador</h1>
    </div>
    """
      
    streamlit.markdown(html_temp, unsafe_allow_html = True)
      
    NALA_DIA = streamlit.text_input("NALA_DIA", "Type Here")
    RALLY_DIA = streamlit.text_input("RALLY_DIA", "Type Here")
    NALA_DOM = streamlit.text_input("NALA_DOM", "Type Here")
    RALLY_DOM = streamlit.text_input("RALLY_DOM", "Type Here")
    PINKIE_DOM = streamlit.text_input("PINKIE_DOM", "Type Here")
    resultado =""

    if streamlit.button("Predict"):
        resultado = prediccion(NALA_DIA, RALLY_DIA, NALA_DOM, RALLY_DOM,PINKIE_DOM)
    streamlit.success('La predicción es {}'.format(resultado))
     
if __name__=='__main__':
    main()
