from os.path import join
import pandas as pd

class ClimaTempo:
    def __init__(self, data_inicio, data_fim):
        self.data_inicio = data_inicio
        self.data_fim: data_fim
    def tempo(self):

        city = 'Boston'
        key = 'WUJNC83UK3WMCFVMXQU9G3PRU'

        URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
                    f'{city}/{self.data_inicio}/{self.data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')

        dados = pd.read_csv(URL)

        file_path = f'/home/daniel/Documents/airflow_dados_tempo/semana={self.data_inicio}/'

        dados.to_csv(file_path + 'dados_brutos.csv')
        dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
        dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')
