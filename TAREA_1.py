# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 08:28:48 2022

@author: ferna
"""
import mnist_loader 
import network
import pickle

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

training_data = list(training_data)
test_data = list(test_data)

net=network.Network([784,30,10])
net.RMSPROP (training_data, 30, 10, 3.0, test_data=test_data)
