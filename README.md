
# 👗 Virtual Try-On for Clothing Using Augmented Reality and AI

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Flask-Web_Framework-orange?style=for-the-badge&logo=flask"/>
<img src="https://img.shields.io/badge/OpenCV-Image_Processing-red?style=for-the-badge&logo=opencv"/>
<img src="https://img.shields.io/badge/MediaPipe-Pose_Detection-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/TailwindCSS-Frontend-purple?style=for-the-badge&logo=tailwind-css"/>
</p>

---

## 🌟 Project Overview

Online apparel shopping often creates uncertainty because customers cannot try clothes physically, leading to **high return rates** and **low satisfaction**.  

This project implements a **Virtual Try-On System** that allows users to:

* Upload full-body images or use a webcam.
* Select multiple outfits and **switch between them seamlessly**.
* See **AI-powered realistic previews** in real-time.
* Interact via a **modern 3-column interface** (Upload | Image Result | Live Camera Try-On).

---

## 🎯 Key Features

| Feature                     | Description                                                 |
| --------------------------- | ----------------------------------------------------------- |
| **AI Body Detection**       | Uses MediaPipe to detect user body landmarks for precise cloth placement. |
| **Multiple Outfit Support** | Upload multiple cloth images and switch outfits instantly. |
| **Live Camera Try-On**      | Real-time try-on via webcam with AI overlay.               |
| **Previous/Next Buttons**   | Seamlessly browse uploaded clothes in both static and live mode. |
| **Instant Results**         | Processed images displayed immediately without page reload. |

---

## 🏗️ Architecture

```mermaid
flowchart LR
    User --> WebApp[Flask Application]
    WebApp --> AI[Pose Detection & Cloth Overlay]
    AI --> Assets[Cloth & Model Images]
    WebApp --> Browser[Display Try-On Result / Live Camera Preview]
````

---

## 🔁 Application Flow

```mermaid
sequenceDiagram
    participant User
    participant Browser
    participant FlaskApp
    participant AI

    User->>Browser: Upload Images / Start Camera
    Browser->>FlaskApp: Send Image Data
    FlaskApp->>AI: Apply Cloth Overlay on Body Landmarks
    AI-->>FlaskApp: Return Processed Image
    FlaskApp-->>Browser: Display Result (Static or Live)
```

---

## 📂 Project Structure

```
Virtual-Try-On-Application/
│
├── assets/
│   ├── cloth/             # Cloth images for upload
│   └── image/             # Example model images / captured frames
│
├── client-side/
│   ├── templates/
│   │   └── index.html     # Frontend template
│   ├── styles.css         # Tailwind + custom styles
│   ├── app.py             # Flask backend
│   └── requirements.txt   # Python dependencies
```

---

## 🛠️ Setup Instructions

### 1️⃣ Open Project in VS Code

Open the **Virtual-Try-On-Application** folder in VS Code.

---

### 2️⃣ Create Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Core Packages:**

* Flask – Web framework
* numpy – Array operations
* OpenCV (`opencv-python`) – Image processing
* MediaPipe – Pose detection
* Pillow – Image manipulation

---

### 4️⃣ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🖼️ Screenshots & Demo

| Upload Try-On                                                | Camera Try-On                                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![Upload Result](Project%20Screenshot/Screenshot_upload.png) | ![Camera Result](Project%20Screenshot/screenshot_camera.png) |

🎥 **Demo Video:** [demo_virtual_try_on.mp4](demo_virtual_try_on.mp4)

---

## ⚡ How to Use

### Upload Try-On

1. Click **Choose File** to select cloth and model images.
2. Click **Apply Try-On** to see the result in the **Image Result panel**.
3. Switch between clothes using **Previous/Next buttons**.

### Live Camera Try-On

1. Click **Start Live** to enable webcam.
2. Click **Capture** to apply the selected cloth on your live feed.
3. Change outfits seamlessly using **Previous/Next buttons**; result updates instantly.

---

## 💡 Future Improvements

* Fully **real-time live overlay** without manual capture.
* Mobile-optimized responsive design.
* Enhanced **lighting and shading** for more realistic clothing visualization.
* Direct **integration with e-commerce platforms** for instant purchase.

---

## 👩‍💻 Author

**Samruddhi Pansare – Software Engineer | AI & Computer Vision Enthusiast**

<p align="center">
<a href="https://www.linkedin.com/in/samruddhi-pansare-b34371328" target="_blank">
<img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>
&nbsp;&nbsp;
<a href="https://github.com/Samruddhipansare2211" target="_blank">
<img alt="GitHub" src="https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github&logoColor=white"/>
</a>
</p>

**Highlights:**

* ✅ Real-time **AI-powered virtual try-on** for clothes.
* ✅ **Python, Flask, OpenCV, MediaPipe, Tailwind CSS** – full-stack expertise.
* ✅ Built for **ease-of-use, realistic previews, and practical online shopping solutions**.

