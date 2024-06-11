from getdata import get_mnist
import numpy as np
import os


"""
w = weights, b = bias, i = input, h = hidden, o = output, l = label
e.g w_i_h = weights from input layer to hidden layer
"""

def train_model(w_i_h1, w_h1_h2, w_h2_o, b_i_h1, b_h1_h2, b_h2_o):
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
            h1_pre = b_i_h1 + w_i_h1 @ img
            h1 = 1 / (1 + np.exp(-h1_pre))
            # h1 = np.maximum(0, h1_pre)
            # Forward propagation hidden1 -> hidden2:
            h2_pre = b_h1_h2 + w_h1_h2 @ h1
            h2 = 1 / (1 + np.exp(-h2_pre))
            # h2 = np.maximum(0, h2_pre)
            # Forward propagation hidden2 -> output:
            o_pre = b_h2_o + w_h2_o @ h2
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
            w_h2_o += -learn_rate * delta_o @ np.transpose(h2)
            b_h2_o += -learn_rate * delta_o
            # Back-propagation hidden2 -> hidden1 (activation function derivative)
            delta_h2 = np.transpose(w_h2_o) @ delta_o * (h2 * (1 - h2))
            w_h1_h2 += -learn_rate * delta_h2 @ np.transpose(h1)
            b_h1_h2 += -learn_rate * delta_h2
            # Back-propagation hidden1 -> input (activation function derivative)
            delta_h1 = np.transpose(w_h1_h2) @ delta_h2 * (h1 * (1 - h1))
            w_i_h1 += -learn_rate * delta_h1 @ np.transpose(img)
            b_i_h1 += -learn_rate * delta_h1
        # Show accuracy for this epoch
        print(f"Error : {err_cnt} Accuracy {epoch}: {round((nr_correct / images.shape[0]) * 100, 2)}%")
        nr_correct = 0
    return w_i_h1, w_h1_h2, w_h2_o, b_i_h1, b_h1_h2, b_h2_o

def checkmodelexist():
# Check if weight text files exist
    if os.path.exists("model_weights_i_h1.txt") \
        and os.path.exists("model_weights_h1_h2.txt") \
        and os.path.exists("model_weights_h2_o.txt") \
        and os.path.exists("model_bias_i_h1.txt") \
        and os.path.exists("model_bias_h1_h2.txt") \
        and os.path.exists("model_bias_h2_o.txt"):
        # Load the trained model from text files
        print("Loading from existing trained model!")
        w_i_h1 = np.loadtxt("model_weights_i_h1.txt")
        w_h1_h2 = np.loadtxt("model_weights_h1_h2.txt")
        w_h2_o = np.loadtxt("model_weights_h2_o.txt")
        b_i_h1 = np.loadtxt("model_bias_i_h1.txt").reshape(-1, 1)
        b_h1_h2 = np.loadtxt("model_bias_h1_h2.txt").reshape(-1, 1)
        b_h2_o = np.loadtxt("model_bias_h2_o.txt").reshape(-1, 1)
        # Update the model using the loaded weights and biases
        w_i_h1, w_h1_h2, w_h2_o, b_i_h1, b_h1_h2, b_h2_o = train_model(w_i_h1, w_h1_h2, w_h2_o, b_i_h1, b_h1_h2, b_h2_o)
    else:
        # Initialize random weights and biases if text files are not found
        print("Trained model not found!")
        # w_i_h = np.random.uniform(-0.5, 0.5, (20, 784))
        # w_h_o = np.random.uniform(-0.5, 0.5, (10, 20))
        # b_i_h = np.zeros((20, 1))
        # b_h_o = np.zeros((10, 1))
        w_i_h1 = np.random.uniform(-0.5, 0.5, (30, 784))  # Weights from input layer to hidden layer 1
        w_h1_h2 = np.random.uniform(-0.5, 0.5, (20, 30))  # Weights from hidden layer 1 to hidden layer 2
        w_h2_o = np.random.uniform(-0.5, 0.5, (10, 20))   # Weights from hidden layer 2 to output layer
        b_i_h1 = np.zeros((30, 1))    # Biases for hidden layer 1
        b_h1_h2 = np.zeros((20, 1))   # Biases for hidden layer 2
        b_h2_o = np.zeros((10, 1))    # Biases for output layer
        # Train the model from scratch
        w_i_h1, w_h1_h2, w_h2_o, b_i_h1, b_h1_h2, b_h2_o = train_model(w_i_h1, w_h1_h2, w_h2_o, b_i_h1, b_h1_h2, b_h2_o)

    np.savetxt("model_weights_i_h1.txt", w_i_h1)
    np.savetxt("model_weights_h1_h2.txt", w_h1_h2)
    np.savetxt("model_weights_h2_o.txt", w_h2_o)
    np.savetxt("model_bias_i_h1.txt", b_i_h1)
    np.savetxt("model_bias_h1_h2.txt", b_h1_h2)
    np.savetxt("model_bias_h2_o.txt", b_h2_o)
    print("Trained model has been saved!")

if __name__ == "__main__":
    checkmodelexist()

