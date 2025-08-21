from ultralytics import YOLO

# Load a YOLO11n PyTorch model
model = YOLO('/home/weights/0728.pt')

# Export the model to TensorRT
model.export(format="engine")
