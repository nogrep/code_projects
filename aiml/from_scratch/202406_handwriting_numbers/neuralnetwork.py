from getdata import get_mnist
import numpy as np
import matplotlib.pyplot as plt


"""
w = weights, b = bias, i = input, h = hidden, o = output, l = label
e.g w_i_h = weights from input layer to hidden layer
"""

images, labels = get_mnist()
w_i_h = np.random.uniform(-0.5, 0.5, (20, 784))
w_h_o = np.random.uniform(-0.5, 0.5, (10, 20))
b_i_h = np.zeros((20,1))
b_h_o = np.zeros((10,1))

learn_rate = 0.01
nr_correct = 0
epochs = 3

for epoch in range(epochs):
    for img, l in zip(images, labels):
        img.shape += (1,)
        l.shape += (1,)
        # Forward propagation input -> hidden:
        h_pre = b_i_h + w_i_h @ img
        h = 1 / (1 + np.exp(-h_pre))
        # Forward propagation hidden -> output:
        o_pre = b_h_o + w_h_o @ h
        o = 1 / (1 + np.exp(-o_pre))

        # Cost, error calculation

