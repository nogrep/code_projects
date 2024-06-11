
from getdata import get_mnist
from neuralnetwork import checkmodelexist
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the trained model from text files

if os.path.exists("model_weights_i_h1.txt") \
    and os.path.exists("model_weights_h1_h2.txt") \
    and os.path.exists("model_weights_h2_o.txt") \
    and os.path.exists("model_bias_i_h1.txt") \
    and os.path.exists("model_bias_h1_h2.txt") \
    and os.path.exists("model_bias_h2_o.txt"):
    # Load the trained model from text files
    print("Loading from existing trained model!")
else:
    # Initialize random weights and biases if text files are not found
    print("Trained model not found!")
    checkmodelexist()

w_i_h1 = np.loadtxt("model_weights_i_h1.txt")
w_h1_h2 = np.loadtxt("model_weights_h1_h2.txt")
w_h2_o = np.loadtxt("model_weights_h2_o.txt")
b_i_h1 = np.loadtxt("model_bias_i_h1.txt").reshape(-1, 1)
b_h1_h2 = np.loadtxt("model_bias_h1_h2.txt").reshape(-1, 1)
b_h2_o = np.loadtxt("model_bias_h2_o.txt").reshape(-1, 1)

images, labels = get_mnist()
# Show result
while True:
    index = int(input("Enter a number (0 - 59999):"))
    img = images[index]
    plt.imshow(img.reshape(28, 28), cmap="Greys")

    img.shape += (1,)

    # Forward propagation input -> hidden:
    h1_pre = b_i_h1 + w_i_h1 @ img.reshape(784, 1)
    # h1 = 1 / (1 + np.exp(-h1_pre))
    h1 = np.maximum(0, h1_pre)
    # Forward propagation hidden1 -> hidden2:
    h2_pre = b_h1_h2 + w_h1_h2 @ h1
    # h2 = 1 / (1 + np.exp(-h2_pre))
    h2 = np.maximum(0, h2_pre)
    # Forward propagation hidden2 -> output:
    o_pre = b_h2_o + w_h2_o @ h2
    o = 1 / (1 + np.exp(-o_pre))

    plt.title(f"Subscribe if its a {o.argmax()} :)")
    plt.show()
