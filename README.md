# 🧠 Gender & Age Detection Using OpenCV & Tkinter

This is a Python-based GUI application that detects **gender and age** from uploaded images using **OpenCV** and **Tkinter**. The project leverages **deep learning models** for accurate predictions and offers a simple, user-friendly interface.

---

## 🚀 Technologies Used

- **Python**
- **OpenCV**
- **Tkinter (GUI)**
- **Deep Learning Models (.caffemodel & .prototxt)**

---

## 💡 Features

- 🖼️ **Image Upload:** Users can upload an image directly from their device.
- 🧑‍🤝‍🧑 **Gender & Age Prediction:** Detects the gender and predicts the age range using pre-trained deep learning models.
- 🧩 **Model Integration:** Integrated `.caffemodel` and `.prototxt` files for deep learning-based predictions.
- 🛡️ **Robust Error Handling:** Handles invalid or unsupported inputs gracefully.
- 🖥️ **User-Friendly GUI:** Easy-to-use interface designed using Tkinter.

---

## 📁 Project Structure
├── age_gender_detector.py # Main Python script with GUI and logic <br>
├── models/ <br>
│ ├── deploy_age.prototxt # Age model configuration<br>
│ ├── age_net.caffemodel # Pre-trained age detection model<br>
│ ├── deploy_gender.prototxt # Gender model configuration<br>
│ ├── gender_net.caffemodel # Pre-trained gender detection model<br>
├── sample_images/ # Optional: Store sample input images<br>
├── README.md # Project documentation<br>

## 🛠️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gender-age-detector.git
   cd gender-age-detector

## 📌 Note
Ensure you have the .caffemodel and .prototxt files in the correct models/ directory.
The application currently supports static image input only (not live webcam feed).
Works with images containing clear, front-facing human faces.

## 🧠 Model Information
#### Gender Classification:
Labels: ['Male', 'Female']
#### Age Classification:
Labels: ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

## 🙋‍♂️ Author
### Wahid Jamdar
Computer Science & Engineering | DY Patil Agriculture & Technical University, Kolhapur <br>
GitHub: @wahid-jamadar <br>
Mail: wahidjamadar2020@gmail.com
LinkedIn: https://www.linkedin.com/in/wahid-jamadar-183a762b1/
