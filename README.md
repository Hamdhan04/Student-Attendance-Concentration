---

# Student Attendance & Concentration Tracking System (AWS Rekognition)

An AI-powered web application that performs **automatic attendance marking** and **real-time concentration monitoring** using facial recognition and eye-state analysis. The system detects multiple faces via webcam, identifies enrolled students using **AWS Rekognition**, tracks focus vs distraction time, and logs attendance into an **Excel sheet**—only once per student per day.

---

##  Features

*  **Face Enrollment** using reference images
*  **Real-time Multi-Face Detection**
*  **Concentration Detection** (Focused / Distracted using eyes-open analysis)
*  **Green Box** → Focused
*  **Red Box** → Distracted
*  **Live Focus & Distraction Statistics**
*  **Automatic Attendance Logging (Excel)**
*  Attendance marked **only once per day**
*  **Download Attendance Excel Sheet**
*  Secure AWS integration using IAM credentials

---

## 🛠️ Tech Stack

**Frontend**

* HTML5, CSS3, JavaScript
* Webcam API
* Canvas Overlay

**Backend**

* Python (Flask)
* AWS Rekognition (Face Recognition)
* OpenPyXL (Excel handling)
* Pillow (Image processing)

**Cloud**

* AWS Rekognition
* AWS IAM

---


##  System Workflow

1. **Enroll Student**

   * Upload reference image
   * Store face in AWS Rekognition collection
   * Save student ID & name locally

2. **Live Detection**

   * Webcam captures frames every 2 seconds
   * AWS detects faces + eye state
   * Faces are identified from the collection

3. **Attendance Logging**

   * Attendance marked **once per student per day**
   * Stored in `attendance.xlsx`

4. **Concentration Tracking**

   * Eyes open → Focused
   * Eyes closed → Distracted
   * Time tracked per student

---

##  Attendance Excel Format

| StudentID   | Name    | Date       | Time     | Status  | Concentration |
| ----------- | ------- | ---------- | -------- | ------- | ------------- |
| student_001 | Hamdhan | 2025-08-21 | 10:32:15 | Present | Concentrated  |

---

##  AWS Configuration

### Required AWS Services

* **AWS Rekognition**
* **AWS IAM**

### IAM Permissions (Minimum)

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "rekognition:CreateCollection",
      "rekognition:DescribeCollection",
      "rekognition:IndexFaces",
      "rekognition:SearchFacesByImage",
      "rekognition:DetectFaces"
    ],
    "Resource": "*"
  }]
}
```

### Configure AWS Locally

```bash
aws configure
```

---

##  How to Run the Project

### 1️ Install Dependencies

```bash
pip install -r requirements.txt
```

###  Start Flask Server

```bash
python app.py
```

### 3️ Open Browser

```
http://127.0.0.1:5000
```

---

##  API Endpoints

| Endpoint               | Method | Description              |
| ---------------------- | ------ | ------------------------ |
| `/`                    | GET    | Web interface            |
| `/enroll`              | POST   | Enroll student face      |
| `/detect`              | POST   | Detect & mark attendance |
| `/download_attendance` | GET    | Download Excel file      |

---
##  Author

**Mohamed Hamdhan**
AI & Data Science Undergraduate
Focus: Computer Vision • AI Systems • Cloud AI

---
