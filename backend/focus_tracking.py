import time
from collections import defaultdict
import cv2
import mediapipe as mp

# mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Store focus logs per student
focus_data = defaultdict(lambda: {
    "focus": 0,
    "distract": 0,
    "last_state": None,
    "last_time": time.time()
})


def analyze_focus(student_id, frame):
    """Analyze focus using eye landmarks (mediapipe iris)"""
    results = face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            left_eye = face_landmarks.landmark[468]
            right_eye = face_landmarks.landmark[473]

            # crude gaze check → if eyes aligned = focused
            gaze = "Concentrated ✅" if abs(left_eye.x - right_eye.x) < 0.05 else "Distracted ❌"

            update_focus_log(student_id, gaze)
            return gaze

    update_focus_log(student_id, "Distracted ❌")
    return "Distracted ❌"


def update_focus_log(student_id, state):
    """Update timers"""
    now = time.time()
    elapsed = now - focus_data[student_id]["last_time"]

    if focus_data[student_id]["last_state"] == "Concentrated ✅":
        focus_data[student_id]["focus"] += elapsed
    elif focus_data[student_id]["last_state"] == "Distracted ❌":
        focus_data[student_id]["distract"] += elapsed

    focus_data[student_id]["last_state"] = state
    focus_data[student_id]["last_time"] = now


def get_focus_report(student_id):
    """Return focus stats"""
    data = focus_data[student_id]
    total = data["focus"] + data["distract"]
    focus_percent = (data["focus"] / total * 100) if total > 0 else 0
    return {
        "StudentID": student_id,
        "FocusTime": round(data["focus"], 2),
        "DistractedTime": round(data["distract"], 2),
        "FocusPercent": round(focus_percent, 2)
    }
