from getdata import get_mnist
import numpy as np
import matplotlib.pyplot as plt
import os


"""
w = weights, b = bias, i = input, h = hidden, o = output, l = label
e.g w_i_h = weights from input layer to hidden layer
"""

def train_model(w_i_h, w_h_o, b_i_h, b_h_o):
    images, labels = get_mnist()

    learn_rate = 0.01
    nr_correct = 0
    epochs = 10

    print("Start training!")
    for epoch in range(epochs):
        err_cnt = 0
        for i, (img, l) in enumerate(zip(images, labels)):
            img.shape += (1,)
            l.shape += (1,)
            # Forward propagation input -> hidden:
            h_pre = b_i_h + w_i_h @ img
            h = 1 / (1 + np.exp(-h_pre))
            # Forward propagation hidden -> output:
            o_pre = b_h_o + w_h_o @ h
            o = 1 / (1 + np.exp(-o_pre))

            # Cost, error calculation
            e = 1 / len(o) * np.sum((o - 1) ** 2, axis=0)
            predicted_label = np.argmax(o)
            true_label = np.argmax(l)
            if predicted_label != true_label:
                err_cnt += 1
                # print(f"Img {i} Error: {e[0]:.4f}, Predicted: {predicted_label}, True: {true_label}")

            nr_correct += int(np.argmax(o) == np.argmax(l))

            # Back-propagation output -> hidden (cost function derivative)
            delta_o = o - l
            w_h_o += -learn_rate * delta_o @ np.transpose(h)
            b_h_o += -learn_rate * delta_o
            # Back-propagation hidden -> input (activation function derivative)
            delta_h = np.transpose(w_h_o) @ delta_o * (h * (1 - h))
            w_i_h += -learn_rate * delta_h @ np.transpose(img)
            b_i_h += -learn_rate * delta_h
        # Show accuracy for this epoch
        print(f"Error : {err_cnt} Accuracy {epoch}: {round((nr_correct / images.shape[0]) * 100, 2)}%")
        nr_correct = 0
    return w_i_h, w_h_o, b_i_h, b_h_o

def checkmodelexist():
# Check if weight text files exist
    if os.path.exists("model_weights_i_h.txt") and os.path.exists("model_weights_h_o.txt") and \
       os.path.exists("model_bias_i_h.txt") and os.path.exists("model_bias_h_o.txt"):
        # Load the trained model from text files
        print("Loading from existing trained model!")
        w_i_h = np.loadtxt("model_weights_i_h.txt")
        w_h_o = np.loadtxt("model_weights_h_o.txt")
        b_i_h = np.loadtxt("model_bias_i_h.txt").reshape(-1, 1)
        b_h_o = np.loadtxt("model_bias_h_o.txt").reshape(-1, 1)
        # Update the model using the loaded weights and biases
        w_i_h, w_h_o, b_i_h, b_h_o = train_model(w_i_h, w_h_o, b_i_h, b_h_o)
    else:
        # Initialize random weights and biases if text files are not found
        print("Trained model not found!")
        w_i_h = np.random.uniform(-0.5, 0.5, (20, 784))
        w_h_o = np.random.uniform(-0.5, 0.5, (10, 20))
        b_i_h = np.zeros((20, 1))
        b_h_o = np.zeros((10, 1))
        # Train the model from scratch
        w_i_h, w_h_o, b_i_h, b_h_o = train_model(w_i_h, w_h_o, b_i_h, b_h_o)

    np.savetxt("model_weights_i_h.txt", w_i_h)
    np.savetxt("model_weights_h_o.txt", w_h_o)
    np.savetxt("model_bias_i_h.txt", b_i_h)
    np.savetxt("model_bias_h_o.txt", b_h_o)
    print("Trained model has been saved!")

if __name__ == "__main__":
    checkmodelexist()

