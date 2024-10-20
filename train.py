from ultralytics import YOLO
import os

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Define paths
data_yaml_path = r'C:\Users\USER\arun\myenv\data.yaml'
output_dir = r'C:\Users\USER\arun\myenv\model_output'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Train the model on your custom dataset
results = model.train(
    data=data_yaml_path,
    epochs=100,
    imgsz=640,
    batch=16,
    name='yolov8n_custom'  # This will create a directory named 'yolov8n_custom' where the model is saved
)

# The model is automatically saved during training, but we can manually save it as well
model_save_path = os.path.join(output_dir, 'yolov8n_custom.pt')
model.save(model_save_path)

print(f"Model trained and saved to {model_save_path}")

# Optional: You can also export the model to other formats if needed
# For example, to export to ONNX format:
# model.export(format='onnx')