# Animal Detection System using YOLOv8

A real-time animal detection system built with Python, OpenCV, YOLOv8, and PyTorch, designed to run on Raspberry Pi 5 for wildlife monitoring and agricultural protection applications.

## 🎯 Overview

This project implements an AI-powered animal detection system that can identify and track various animals in real-time using a camera feed. The system uses a custom-trained YOLOv8 model for accurate detection with visual bounding boxes and confidence scores.

## ✨ Features

- **Real-time Detection**: Live animal detection from camera feed
- **Custom YOLOv8 Model**: Trained specifically for animal detection
- **Visual Feedback**: Colored bounding boxes with class names and confidence scores
- **Raspberry Pi 5 Optimized**: Lightweight implementation designed specifically for Raspberry Pi 5
- **Multi-class Detection**: Supports detection of multiple animal species
- **Confidence Filtering**: Adjustable confidence threshold (default: 40%)

## 🛠️ Technologies Used

- **Python 3.x**
- **OpenCV** - Computer vision and image processing
- **Ultralytics YOLOv8** - Object detection model
- **PyTorch** - Deep learning framework
- **Raspberry Pi 5** - Edge computing platform

## 📋 Prerequisites

- Python 3.7 or higher
- Raspberry Pi 5 (8GB RAM recommended for optimal performance)
- USB Camera or Raspberry Pi Camera Module
- Trained YOLOv8 model weights
- PyTorch (automatically installed with Ultralytics)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/animal-detection-yolov8.git
   cd animal-detection-yolov8
   ```

2. **Install required packages**
   ```bash
   pip install ultralytics opencv-python torch torchvision
   ```

3. **Set up the model**
   - Place your trained YOLOv8 model weights in the project directory
   - Update the model path in the code:
   ```python
   yolo = YOLO('path/to/your/best.pt')
   ```

## 📁 Project Structure

```
animal-detection-yolov8/
├── animal_detection.py      # Main detection script
├── weights/
│   └── best.pt             # Trained YOLOv8 model weights
├── README.md
└── requirements.txt
```

## 🎮 Usage

1. **Run the detection system**
   ```bash
   python animal_detection.py
   ```

2. **Controls**
   - Press `q` to quit the application
   - The system will automatically start detecting animals from the camera feed

3. **Customize detection parameters**
   - Modify confidence threshold: Change `box.conf[0] > 0.4` to desired value
   - Adjust camera source: Change `cv2.VideoCapture(0)` to use different camera

## ⚙️ Configuration

### Camera Setup
- **USB Camera**: Use `cv2.VideoCapture(0)` (default)
- **Raspberry Pi Camera**: Use `cv2.VideoCapture(0)` with proper camera enablement
- **IP Camera**: Use `cv2.VideoCapture('rtsp://camera_ip:port/stream')`

### Model Configuration
```python
# Load custom trained model
yolo = YOLO('path/to/your/model.pt')

# Adjust confidence threshold
if box.conf[0] > 0.4:  # 40% confidence threshold
```

## 🎨 Color Coding

The system uses a dynamic color assignment for different animal classes:
- Each detected class gets a unique color
- Colors are generated using a base palette with variations
- Consistent coloring across detection frames

## 📊 Performance

- **Detection Speed**: ~20-45 FPS on Raspberry Pi 5
- **Accuracy**: Depends on trained YOLOv8 model quality
- **Memory Usage**: ~1-2GB RAM
- **CPU Usage**: ~40-60% on Raspberry Pi 5

## 🔧 Troubleshooting

### Common Issues

1. **Camera not found**
   ```bash
   # Check available cameras
   ls /dev/video*
   # Try different camera indices (0, 1, 2...)
   ```

2. **Model loading error**
   - Verify model path is correct
   - Ensure model file is not corrupted
   - Check YOLOv8 version compatibility

3. **Low FPS performance**
   - Reduce input resolution
   - Increase confidence threshold
   - Ensure adequate cooling for Raspberry Pi 5
   - Use lighter YOLOv8 model variant (YOLOv8n instead of YOLOv8x)

## 🚀 Future Enhancements

- [ ] Add data logging and analytics
- [ ] Implement alert system (email/SMS)
- [ ] Add night vision support
- [ ] Multi-camera support
- [ ] Web interface for remote monitoring
- [ ] Integration with IoT platforms

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Navaneeth Krishna** - *Initial work* - [GitHub Profile](https://github.com/yourusername)

## 🙏 Acknowledgments

- Ultralytics team for YOLOv8
- PyTorch team for the deep learning framework  
- OpenCV community
- Raspberry Pi Foundation

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub or contact [navaneethkrishna547@gmail.com](mailto:navaneethkrishna547@gmail.com).

---

⭐ **If this project helped you, please give it a star!** ⭐
