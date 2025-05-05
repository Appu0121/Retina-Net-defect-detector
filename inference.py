import cv2
import numpy as np
# from tensorflow.keras.models import load_model

def detect_defect(image_path):
    img = cv2.imread(image_path)
    img_resized = cv2.resize(img, (224, 224)) / 255.0
    input_tensor = np.expand_dims(img_resized, axis=0)
    print("Running inference on:", image_path)
    print("(Simulated) Defect detected at region [x=70, y=50, w=60, h=40]")

if __name__ == '__main__':
    detect_defect('sample_semiconductor.jpg')
