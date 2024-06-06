
from getdata import get_mnist
from neuralnetwork import checkmodelexist
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the trained model from text files

if os.path.exists("model_weights_i_h.txt") and os.path.exists("model_weights_h_o.txt") and \
   os.path.exists("model_bias_i_h.txt") and os.path.exists("model_bias_h_o.txt"):
    # Load the trained model from text files
    print("Loading from existing trained model!")
else:
    # Initialize random weights and biases if text files are not found
    print("Trained model not found!")
    checkmodelexist()

w_i_h = np.loadtxt("model_weights_i_h.txt")
w_h_o = np.loadtxt("model_weights_h_o.txt")
b_i_h = np.loadtxt("model_bias_i_h.txt").reshape(-1, 1)
b_h_o = np.loadtxt("model_bias_h_o.txt").reshape(-1, 1)

images, labels = get_mnist()
# Show result
while True:
    index = int(input("Enter a number (0 - 59999):"))
    img = images[index]
    plt.imshow(img.reshape(28, 28), cmap="Greys")

    img.shape += (1,)
    # Forward propagation input -> hidden
    h_pre = b_i_h + w_i_h @ img.reshape(784, 1)
    h = 1 / (1 + np.exp(-h_pre))
    # Forward propagation hidden -> output
    o_pre = b_h_o + w_h_o @ h
    o = 1 / (1 + np.exp(-o_pre))

    plt.title(f"Subscribe if its a {o.argmax()} :)")
    plt.show()
