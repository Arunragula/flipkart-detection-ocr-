import cv2
from ultralytics import YOLO
import numpy as np
import pytesseract
from PIL import Image

# Load the YOLOv8 model
model = YOLO(r'C:\Users\USER\arun\runs\detect\yolov8n_custom\weights\best.pt')

# Function to detect freshness (placeholder)
def detect_freshness(image):
    # Implement your freshness detection logic here
    # This could involve analyzing color, texture, or other features
    # For now, we'll return a random freshness score
    return np.random.uniform(0, 1)

# Function to perform OCR
def perform_ocr(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(Image.fromarray(gray))
    return text

# Open the video capture
cap = cv2.VideoCapture(0)  # Use 0 for default camera

while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    
    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)
        
        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        
        # Detect freshness
        freshness_score = detect_freshness(frame)
        
        # Perform OCR
        ocr_text = perform_ocr(frame)
        
        # Add freshness score and OCR text to the frame
        cv2.putText(annotated_frame, f"Freshness: {freshness_score:.2f}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(annotated_frame, f"OCR: {ocr_text[:20]}...", (10, 70), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()