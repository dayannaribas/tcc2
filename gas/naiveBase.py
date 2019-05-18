import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import confusion_matrix

basededados = pd.read_csv('dadosTeste.csv')
basededados.Classe.unique()

x = basededados.iloc[:,[0,1,2]].values
y = basededados.iloc[:, 3].values

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(x, y, 
                                                                  test_size = 0.3,
                                                                  random_state = 0)