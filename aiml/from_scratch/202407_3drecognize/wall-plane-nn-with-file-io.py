import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import os, re

def normalize_data(text):
    return text.translate(str.maketrans({'(': '', ')': '', ' ': ''}))

def init_model():
        w_i_h1 = np.random.uniform(-0.5, 0.5, (100, 240))  # Weights from input layer to hidden layer
        w_h1_o = np.random.uniform(-0.5, 0.5, (120, 100))   # Weights from hidden layer to output layer
        b_i_h = np.zeros((100, 1))    # Biases for hidden layer
        b_h2_o = np.zeros((120, 1))    # Biases for output layer

def train_model(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            tmp = line.split(", output,")
            parts = tmp[0].split(", input,")
            vertices_str = normalize_data(parts[1])
            plane_points = normalize_data(tmp[1])
            
            vertices = [tuple(map(float, v.strip('()').split(','))) for v in vertices_str.split('),') if v.strip()]
            plane_points = [tuple(map(float, p.strip('()').split(','))) for p in plane_points_str.split('),') if p.strip()]
            

    return data

class DataFormat():
    def __init__(self, id, input_vertices, output_vertices):
        


def main():
    input_file = 'input_data2.txt'
    output_file = 'output_results.txt'
    model_filename_prefix = 'wall_center_plane_model'

    data = read_data(input_file)
    model = check_model_exist(model_filename_prefix)

    train_model(model, data, num_epochs=3, learning_rate=0.001)
    save_model(model, model_filename_prefix)

    results = []
    for id, vertices, _ in data:
        predicted_plane_points = predict(model, vertices)
        results.append((id, vertices, predicted_plane_points))
    
    write_output(output_file, results)
    print(f"Results written to {output_file}")

if __name__ == "__main__":
    main()
