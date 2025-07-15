# Player Re-identification (Single Camera)

This project performs **player re-identification** using deep learning and tracking in a single-camera setup. It detects players in video frames, extracts features, and re-identifies players over time using appearance-based matching.

---

## 📁 Project Structure

```
player-reid-single-camera/
├── models/
│   └── best.pt             # (Download manually - see link below)
├── videos/
│   └── 15sec_input_720p.mp4  # (Download manually - see link below)
├── src/
│   ├── detector.py
│   ├── reid_model.py
│   └── main.py             # Your main execution script
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📦 Downloads Required

Some large files are not included in the repo due to GitHub size restrictions. Download and place them in the correct folders:

### 🔗 Download Model File (`best.pt`)
➡️ [Download best.pt](https://your-download-link.com/best.pt)  
📁 Place it inside: `models/best.pt`

### 🔗 Download Sample Video (`15sec_input_720p.mp4`)
➡️ [Download video](https://your-download-link.com/15sec_input_720p.mp4)  
📁 Place it inside: `videos/15sec_input_720p.mp4`

> Replace the links above with actual Google Drive or Dropbox links if hosting.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/nafisa404/player-reid-single-camera.git
cd player-reid-single-camera
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate         # On Windows
# source venv/bin/activate    # On Linux/macOS
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Code

```bash
python src/main.py
```

Make sure the model and video files are downloaded and placed in the correct directories first.

---

## 🧹 .gitignore Highlights

These files are intentionally excluded from the repo:

- `venv/`
- `models/best.pt`
- `videos/15sec_input_720p.mp4`
- Large binaries: `.dll`, `.lib`, `.pyd`

---


---

## 📬 Contact

If you have any issues running the code, feel free to reach out!

