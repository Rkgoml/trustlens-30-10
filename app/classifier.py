# deepfake_predictor.py
import os
import tempfile

import torch
from huggingface_hub import hf_hub_download
from PIL import Image
from safetensors.torch import load_file
from transformers import ImageClassificationPipeline, pipeline

from app.inference import predict_video
from app.model import ImprovedEfficientViT


class DeepfakePredictor:
    def __init__(self):
        self.model, self.device = self._load_model()
        self.image_classifier = self._load_image_model()

    def _load_model(self):
        """Load EfficientViT model for video classification"""
        checkpoint_path = hf_hub_download(
            repo_id="faisalishfaq2005/deepfake-detection-efficientnet-vit",
            filename="model.safetensors",
        )
        state_dict = load_file(checkpoint_path, device="cpu")
        model = ImprovedEfficientViT()
        model.load_state_dict(state_dict)
        model.eval()
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model.to(device)
        return model, device

    def _load_image_model(self):
        """Load Hugging Face image classification model"""
        image_classifier: ImageClassificationPipeline = pipeline(
            "image-classification",
            model="dima806/deepfake_vs_real_image_detection",
            trust_remote_code=True,
        )
        return image_classifier

    def analyze_image(self, image: Image.Image):
        """Run deepfake detection on an image"""
        results = self.image_classifier(image)
        output = []
        for result in results:
            label = result["label"]
            score = result["score"]
            emoji = "🟢" if "real" in label.lower() else "🔴"
            output.append({"label": label, "score": score, "emoji": emoji})
        return output

    def analyze_video(self, uploaded_file):
        """Run deepfake detection on a video"""
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            temp_file.write(uploaded_file.read())
            video_path = temp_file.name

        try:
            result = predict_video(video_path, self.model)
        finally:
            os.remove(video_path)
        return result
