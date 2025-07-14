# 🏃‍♂️ Player Re-Identification (Single Camera Feed) – Liat.ai Assignment

## 📌 Overview
This project implements a basic player re-identification system in sports video analytics using object detection (YOLOv5) and tracking (SORT). The objective is to maintain consistent player IDs across a single 15-second video feed, even when players leave and re-enter the frame.

---

## 📁 Project Structure

```
player-reidentification-liatai/
├── models/                        # Place YOLOv5 model here
│   └── yolov5_player_ball.pt
├── video/                         # Place input video here
│   └── 15sec_input_720p.mp4
├── output/                        # Tracked video output will be saved here
│   └── output_with_ids.mp4
├── src/
│   ├── detect.py                  # Player detection using YOLOv5
│   ├── track.py                   # SORT-based tracking
│   └── main.py                    # End-to-end inference pipeline
├── requirements.txt
├── README.md
└── report.md
```

---

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

### 2. Add Required Files

- Download the **YOLOv5 model** and place it into the `models/` folder:
  ```
  models/yolov5_player_ball.pt
  ```

- Download the **input video** and place it into the `video/` folder:
  ```
  video/15sec_input_720p.mp4
  ```

---

## ▶️ Run the Project

```bash
python src/main.py
```

The output video will be saved to:

```
output/output_with_ids.mp4
```

---

## 🛠️ Dependencies

All dependencies are listed in `requirements.txt` including:

- `ultralytics` (for YOLOv5 inference)
- `sort-tracker` (SORT tracker)
- OpenCV, NumPy, Matplotlib, etc.

---

## 📬 Contact

If you have any issues running the code, feel free to reach out!

