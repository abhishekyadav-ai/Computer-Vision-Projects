# Computer Vision Projects

A collection of computer vision projects built with Python and OpenCV. Each project lives in its own folder with its own README and `requirements.txt`, so it can be run independently.

## Projects

| Project | Description | Tech |
|---------|-------------|------|
| [Burglar Detection](Burglar-Detection/) | Detects motion in video footage using frame differencing, draws bounding boxes and saves the frames where motion occurs | Python, OpenCV |

More projects will be added here as I build them.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/abhishekyadav-ai/Computer-Vision-Projects.git
cd Computer-Vision-Projects
```

Create and activate a virtual environment (Windows):

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS or Linux, activate it with `source venv/bin/activate` instead.

Then open the folder of the project you want to run and follow its README. Dependencies are listed per project:

```bash
cd Burglar-Detection
pip install -r requirements.txt
```

## Repository Structure

```
Computer-Vision-Projects/
├── Burglar-Detection/
│   ├── burglar_detection.py
│   ├── motion_frame_5.jpg
│   ├── requirements.txt
│   └── README.md
├── .gitignore
└── README.md
```

## Author

Abhishek Yadav
GitHub: [abhishekyadav-ai](https://github.com/abhishekyadav-ai)