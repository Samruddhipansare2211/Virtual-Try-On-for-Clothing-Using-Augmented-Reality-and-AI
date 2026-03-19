from flask import Flask, request, render_template, jsonify
import cv2
import numpy as np
import mediapipe as mp
import base64

app = Flask(__name__)

# Mediapipe pose for body landmarks
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

uploaded_cloths = []  # Stores processed cloth images
SIZE_SCALE = {"S":0.9,"M":1.0,"L":1.1,"XL":1.2}

# Remove white background and create alpha channel
def remove_white_background(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    b, g, r = cv2.split(img)
    rgba = cv2.merge([b, g, r, mask])
    return rgba

# Apply cloth on model image
def apply_cloth(model_img, cloth_img, size="M"):
    h, w, _ = model_img.shape
    scale = SIZE_SCALE.get(size, 1.0)
    
    rgb = cv2.cvtColor(model_img, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)
    if not results.pose_landmarks:
        return model_img
    
    lm = results.pose_landmarks.landmark
    l_shoulder = (int(lm[11].x*w), int(lm[11].y*h))
    r_shoulder = (int(lm[12].x*w), int(lm[12].y*h))
    l_hip = (int(lm[23].x*w), int(lm[23].y*h))
    
    # Calculate cloth size and position
    cloth_width = int((abs(r_shoulder[0]-l_shoulder[0])+150) * scale)
    cloth_height = int((abs(l_hip[1]-l_shoulder[1])+180) * scale)
    
    cloth_resized = cv2.resize(cloth_img, (cloth_width, cloth_height))
    x_offset = int((l_shoulder[0]+r_shoulder[0])/2 - cloth_width/2)
    y_offset = int(l_shoulder[1]-50)
    
    # Correct offsets to stay inside image
    x_offset = max(0, x_offset)
    y_offset = max(0, y_offset)
    cloth_width = min(cloth_width, w - x_offset)
    cloth_height = min(cloth_height, h - y_offset)
    
    # Skip if cloth goes outside
    if cloth_width <= 0 or cloth_height <= 0:
        return model_img
    
    cloth_resized = cloth_resized[0:cloth_height, 0:cloth_width]
    alpha = cloth_resized[:, :, 3] / 255.0
    cloth_rgb = cloth_resized[:, :, :3]
    
    result = model_img.copy()
    roi = result[y_offset:y_offset+cloth_height, x_offset:x_offset+cloth_width]
    
    for c in range(3):
        roi[:, :, c] = alpha*cloth_rgb[:, :, c] + (1-alpha)*roi[:, :, c]
    
    result[y_offset:y_offset+cloth_height, x_offset:x_offset+cloth_width] = roi
    return result

@app.route('/')
def home():
    return render_template("index.html", op_list=[])

@app.route('/preds', methods=['POST'])
def submit():
    global uploaded_cloths
    uploaded_cloths = []

    cloth_files = request.files.getlist('cloth')
    model_file = request.files['model']
    size = request.form.get("size","M")

    # Read model image
    model_bytes = np.frombuffer(model_file.read(), np.uint8)
    model_img = cv2.imdecode(model_bytes, cv2.IMREAD_COLOR)

    op_list = []

    for cloth in cloth_files:
        cloth_bytes = np.frombuffer(cloth.read(), np.uint8)
        cloth_img = cv2.imdecode(cloth_bytes, cv2.IMREAD_COLOR)
        cloth_img = remove_white_background(cloth_img)
        uploaded_cloths.append(cloth_img)
        
        # Apply cloth on model image for static preview
        result = apply_cloth(model_img, cloth_img, size)
        _, buffer = cv2.imencode('.png', result)
        op_list.append(base64.b64encode(buffer).decode())

    return render_template("index.html", op_list=op_list)

@app.route('/camera_tryon', methods=['POST'])
def camera_tryon():
    global uploaded_cloths
    if len(uploaded_cloths) == 0:
        return jsonify({"error": "Upload cloth first"})
    
    data = request.json["image"]
    index = int(request.json.get("index",0))
    size = request.json.get("size","M")
    
    img_bytes = base64.b64decode(data.split(",")[1])
    np_arr = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Apply selected cloth on live frame
    cloth = uploaded_cloths[index % len(uploaded_cloths)]
    result = apply_cloth(frame, cloth, size)
    
    _, buffer = cv2.imencode('.png', result)
    return jsonify({"image": base64.b64encode(buffer).decode()})

if __name__ == "__main__":
    app.run(debug=True)