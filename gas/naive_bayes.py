import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import confusion_matrix

class Modelo():
    def modelo_navie_base(self, gas, temperatura, umidade):
        basededados = pd.read_csv('gas\dadosTeste.csv')
        basededados.Classe.unique()
    
        x = basededados.iloc[:,[0,1,2]].values
        y = basededados.iloc[:, 3].values
        
        x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(x, y, 
                                                                          test_size = 0.3,
                                                                          random_state = 0)
        modelo = GaussianNB()
        modelo.fit(x_treinamento, y_treinamento)
        
        previsoes = modelo.predict([[gas, temperatura, umidade],]) #passar os dados da leitura do sensor aqui
        return previsoes
        
    
if __name__ == '__main__':
    modelo = Modelo()
    print(modelo.modelo_navie_base(gas=360, temperatura=18, umidade=70))  
    
    
    
    
    
#basededados = pd.read_csv('dadosTeste.csv')
#basededados.Classe.unique()
#
#x = basededados.iloc[:,[0,1,2]].values
#y = basededados.iloc[:, 3].values
#
#x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(x, y, 
#                                                                  test_size = 0.3,
#                                                                  random_state = 0)
#modelo = GaussianNB()
#modelo.fit(x_treinamento, y_treinamento)

#previsoes = modelo.predict([[363,20,76],]) #passar os dados da leitura do sensor aqui
#print(previsoes)