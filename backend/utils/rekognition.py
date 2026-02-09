import boto3
import base64

rekognition = boto3.client("rekognition", region_name="us-east-1")

def analyze_face(image_bytes):
    response = rekognition.detect_faces(
        Image={"Bytes": image_bytes},
        Attributes=["ALL"]
    )
    return response["FaceDetails"]

def analyze_base64_image(image_base64):
    image_bytes = base64.b64decode(image_base64.split(",")[1])
    return analyze_face(image_bytes)
