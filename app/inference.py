import cv2
import torch
from mtcnn import MTCNN
from torchvision import transforms


def extract_faces(video_path, target_frames=20):
    detector = MTCNN()

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return []

    # fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_interval = max(total_frames // target_frames, 1)

    face_images = []

    for i in range(0, total_frames, frame_interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if not ret:
            continue

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = detector.detect_faces(rgb_frame)

        for face in faces:
            if face["confidence"] < 0.9:
                continue
            x, y, w, h = face["box"]
            x, y = max(x, 0), max(y, 0)
            face_img = rgb_frame[y : y + h, x : x + w]

            if face_img.size == 0:
                continue

            face_img = cv2.resize(face_img, (224, 224))
            face_images.append(face_img)

    cap.release()
    return face_images


transform_vedio = transforms.Compose(
    [
        transforms.ToPILImage(),
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5], std=[0.5]),
    ]
)


# def predict_vedio(video_path, model_vedio):
#     pred_list = []
#     prob_list = []

#     faces = extract_faces(video_path, target_frames=20)

#     transformed_faces = [transform_vedio(face) for face in faces]
#     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#     model_vedio.to(device)

#     for face in transformed_faces:
#         face = face.to(device).unsqueeze(0)

#         with torch.no_grad():
#             logit = model_vedio(face)
#             prob = torch.sigmoid(logit)
#             pred = int(prob.item() > 0.5)
#             pred_list.append(pred)
#             prob_list.append(prob)

#     count = 0
#     for ele in pred_list:
#         if ele == 0:
#             count += 1

#     predicted_class = 0 if count > 3 else 1
#     return {"class": predicted_class}

def predict_video(video_path, model_vedio):
    # pred_list = []
    prob_list = []

    faces = extract_faces(video_path, target_frames=20)

    if not faces:
        return {
            "class": None,
            "confidence": {"Real": 0.0, "Fake": 0.0},
            "message": "No faces detected in video."
        }

    transformed_faces = [transform_vedio(face) for face in faces]
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_vedio.to(device)

    for face in transformed_faces:
        face = face.to(device).unsqueeze(0)

        with torch.no_grad():
            logit = model_vedio(face)
            prob = torch.sigmoid(logit).item()  # Probability of 'Real'
            prob_list.append(prob)

    # Average probability across frames
    avg_prob = sum(prob_list) / len(prob_list)

    # Class decision: Real if avg_prob > 0.5 else Fake
    predicted_class = "Real" if avg_prob > 0.5 else "Fake"

    # Confidence distribution
    confidence = {
        "Real": round(avg_prob, 3),
        "Fake": round(1 - avg_prob, 3)
    }

    return {
        "class": predicted_class,
        "confidence": confidence
    }
