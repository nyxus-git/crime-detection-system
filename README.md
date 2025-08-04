
# Crime Detection System

This project uses a pretrained model to detect weapons in real-time using object detection techniques. The system captures video from your local camera feed and processes each frame to identify weapons. It can be used for real-time surveillance and security applications.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [Pretrained Model](#pretrained-model)
- [Usage](#usage)
- [License](#license)

---

## Prerequisites

To run this project locally, you will need:

- **Python 3.7+** installed on your machine.
- A **virtual environment** to isolate dependencies.
- A pretrained model for weapon detection (`best.pt`).

### Required Python Libraries:

The following Python libraries are required and are specified in the `requirements.txt` file:
- `torch`
- `opencv-python`
- Any other dependencies (as listed in `requirements.txt`).

---

## Setup Instructions

### 1. Clone the Repository

Start by cloning the repository to your local machine:
```bash
git clone https://github.com/yourusername/crime-detection-system.git
cd crime-detection-system
```

### 2. Create and Activate a Virtual Environment

It's best to create a virtual environment to manage dependencies. To do this:

#### On Linux/MacOS:
```bash
python3 -m venv crime_detection_env
source crime_detection_env/bin/activate
```

#### On Windows:
```bash
python -m venv crime_detection_env
crime_detection_env\Scripts\activate
```

### 3. Install the Dependencies

Once the virtual environment is activated, install the required dependencies listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Pretrained Model Setup

Download the pretrained model `best.pt` (trained for weapon detection) and place it in the root of your project directory (`crime-detection-system` folder).

You can adjust the model's path in the Python code if it's located elsewhere.

---

## Running the Project

### 1. Activate the Virtual Environment

Make sure the virtual environment is activated before running the project:

#### On Linux/MacOS:
```bash
source /home/nyxus/Documents/crime-detection-system/crime_detection_env/bin/activate
```

#### On Windows:
```bash
crime_detection_env\Scripts\activate
```

### 2. Run the Weapon Detection System

Now that your environment is set up, you can run the weapon detection system with the following command:

```bash
python crime_detection.py
```

This will start capturing video from your webcam and run the pretrained model to detect weapons in real-time.

---

## Pretrained Model

This project relies on a pretrained model (`best.pt`) that has been trained to detect weapons. Ensure that:
1. You have downloaded the pretrained model and placed it in the project folder.
2. The Python code in `crime_detection.py` points to the correct path of the model.

If you're using a different model, you may need to adjust the model loading process in the Python code.

---

## Usage

### Real-Time Detection

After running the `crime_detection.py` script, the system will use your camera feed to detect weapons in real-time. The detected weapons will be highlighted in the video feed.

- **Press 'q'** to quit the application and stop the video feed.

### Customization

You can modify the script to:
- Use an external camera instead of the default webcam by changing the `cv2.VideoCapture()` parameter.
- Save the processed video frames or detection results to a file.
- Adjust the detection threshold or other model parameters.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

---

### What’s included in this README:
1. **Prerequisites**: Explains what’s needed to run the project.
2. **Setup Instructions**: Step-by-step instructions to clone the repo, set up a virtual environment, install dependencies, and handle the pretrained model.
3. **Running the Project**: Detailed steps to activate the virtual environment and run the detection system.
4. **Pretrained Model**: Information on handling the model (`best.pt`), including path and usage.
5. **Usage**: How to use and customize the system.
6. **License**: MIT License information.

This `README.md` is designed to make it easy for someone to set up and run your project, ensuring they have everything they need. Let me know if you need any modifications or additions!
