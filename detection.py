"""
Animal Detection System using YOLOv8
=====================================
Real-time animal detection using custom trained YOLOv8 model and OpenCV
"""

import cv2
from ultralytics import YOLO

# Load the trained YOLOv8 model
yolo = YOLO('C:/group_project/runs/detect/train17/weights/best.pt')

# Initialize video capture from default camera (index 0)
videoCap = cv2.VideoCapture(0)

def getColours(cls_num):
    """
    Generate unique colors for different animal classes
    
    Args:
        cls_num (int): Class number from YOLO detection
        
    Returns:
        tuple: BGR color tuple for OpenCV
    """
    # Base color palette (BGR format for OpenCV)
    base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    
    # Select base color using modulo to cycle through palette
    color_index = cls_num % len(base_colors)
    
    # Color increment patterns to create variations
    increments = [(1, -2, 1), (-2, 1, -1), (1, -1, 2)]
    
    # Generate unique color by modifying base color with increments
    color = [base_colors[color_index][i] + increments[color_index][i] *
    (cls_num // len(base_colors)) % 256 for i in range(3)]
    
    return tuple(color)

# Main detection loop
while True:
    # Read frame from camera
    ret, frame = videoCap.read()
    
    # Skip iteration if frame reading failed
    if not ret:
        continue
    
    # Run YOLO detection and tracking on the frame
    results = yolo.track(frame, stream=True)
    
    # Process each detection result
    for result in results:
        # Get class names dictionary from the model
        classes_names = result.names
        
        # Process each detected bounding box
        for box in result.boxes:
            # Only process detections with confidence > 40%
            if box.conf[0] > 0.4:
                # Extract bounding box coordinates
                [x1, y1, x2, y2] = box.xyxy[0]
                
                # Convert coordinates to integers
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # Get the detected class number
                cls = int(box.cls[0])
                
                # Get the class name from the classes dictionary
                class_name = classes_names[cls]
                
                # Generate color for this class
                colour = getColours(cls)
                
                # Draw bounding rectangle around detected animal
                cv2.rectangle(frame, (x1, y1), (x2, y2), colour, 2)
                
                # Add text label with class name and confidence score
                cv2.putText(frame, f'{classes_names[int(box.cls[0])]} {box.conf[0]:.2f}', 
                           (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, colour, 2)
               
    # Display the frame with detections
    cv2.imshow('frame', frame)
    
    # Exit loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up resources
videoCap.release()
cv2.destroyAllWindows()
