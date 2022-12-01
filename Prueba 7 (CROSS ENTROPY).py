# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:04:06 2022

@author: ferna
"""
import mnist_loader 
import Network5
import pickle

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

training_data = list(training_data)
test_data = list(test_data)

net=Network5.Network([784,30,10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
archivo = open("red_prueba1.pkl",'wb')
pickle.dump(net,archivo)
archivo.close()
exit()
#leer el archivo
archivo_lectura = open("red_prueba.pkl",'rb')
net = pickle.load(archivo_lectura)
archivo_lectura.close()
net.SGD( training_data, 10, 50, 0.5, test_data=test_data)
archivo = open("red_prueba.pkl",'wb')
pickle.dump(net,archivo)
archivo.close()
exit()
