
import torch
from ultralytics import YOLO

# print(torch.cuda.device_count())
# for i in range(torch.cuda.device_count()):
#     print(torch.cuda.get_device_name(i))
#     print(torch.cuda.device(i))

# print("PyTorch version:", torch.__version__)
# print("CUDA available:", torch.cuda.is_available())
#
# if torch.cuda.is_available():
#     print("CUDA version:", torch.version.cuda)
#     print("cuDNN version:", torch.backends.cudnn.version())

model = YOLO('./yolov8n')
if torch.cuda.is_available():
    print("Running on:", torch.cuda.get_device_name())
else:
    print("Running on: cpu")

# # Manually config to run on cpu
# torch.device("cpu")

results = model.predict('input_videos/08fd33_0.mp4', save=True)
print(results[0])
print('---------------------------------------------------------')
for box in results[0].boxes:
    print(box)


