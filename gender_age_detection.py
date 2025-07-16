import cv2
import os
import tkinter as tk
from tkinter import filedialog

# === Open file dialog to choose an image ===
root = tk.Tk()
root.withdraw()  # Hide the Tkinter window
image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

if not image_path:
    print("No image selected.")
    exit()

print("Selected image:", image_path)

# === Model files ===
age_proto = "age_deploy.prototxt"
age_model = "age_net.caffemodel"
gender_proto = "gender_deploy.prototxt"
gender_model = "gender_net.caffemodel"

# === Labels ===
AGE_LIST = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
GENDER_LIST = ['Male', 'Female']

# === Load networks ===
age_net = cv2.dnn.readNetFromCaffe(age_proto, age_model)
gender_net = cv2.dnn.readNetFromCaffe(gender_proto, gender_model)

# === Load selected image ===
frame = cv2.imread(image_path)
if frame is None:
    print("Image not found or unreadable.")
    exit()

# === Face detection using Haar Cascade ===
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

print(f"Faces detected: {len(faces)}")

# === Process each detected face ===
for (x, y, w, h) in faces:
    face_img = frame[y:y+h, x:x+w]
    blob = cv2.dnn.blobFromImage(face_img, 1.0, (227, 227), [104, 117, 123], swapRB=False)

    # Predict Gender
    gender_net.setInput(blob)
    gender_preds = gender_net.forward()
    gender = GENDER_LIST[gender_preds[0].argmax()]

    # Predict Age
    age_net.setInput(blob)
    age_preds = age_net.forward()
    age = AGE_LIST[age_preds[0].argmax()]

    # Draw rectangle and label
    label = f"{gender}, {age}"
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)

# === Display result ===
cv2.imshow("Gender and Age Detection", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
