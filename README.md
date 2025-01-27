

# Product Detection and Analysis

This repository contains Python scripts for collecting product images, training a YOLOv8 model for product detection, and performing real-time product detection with features like freshness detection and Optical Character Recognition (OCR).

## Table of Contents
1. [Installation](#installation)
2. [Scripts](#scripts)
3. [Usage](#usage)
4. [Dependencies](#dependencies)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/product-detection-analysis.git
   cd product-detection-analysis
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the YOLOv8 pre-trained weights:**
   ```bash
   wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt
   ```

## Scripts

### 1. `products.py`
This script utilizes the Google Custom Search API to search for and download product images, creating a dataset for training the object detection model.

### 2. `split.py`
This script divides the collected dataset into training and validation sets, preparing the data for model training.

### 3. `train.py`
This script trains a YOLOv8 model on the prepared dataset, resulting in a custom product detection model.

### 4. `detection.py`
This script performs real-time product detection using the trained model, featuring additional capabilities like freshness detection and OCR.

## Usage

1. **Collect product images:**
   ```bash
   python products.py
   ```
   **Note:** You need to set up a Google Custom Search API and obtain the necessary API key and search engine ID.

2. **Split the dataset:**
   ```bash
   python split.py
   ```

3. **Train the model:**
   ```bash
   python train.py
   ```

4. **Run real-time detection:**
   ```bash
   python detection.py
   ```

## Dependencies

- `opencv-python`
- `ultralytics`
- `numpy`
- `pytesseract`
- `Pillow`
- `google-api-python-client`

A complete list of dependencies can be found in the `requirements.txt` file.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any part of this documentation to better fit your project's needs or style! Let me know if you need any further modifications or additional sections.
