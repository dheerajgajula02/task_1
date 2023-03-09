from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer, BlipProcessor, BlipForConditionalGeneration

import torch
from PIL import Image

model_name = "bipin/image-caption-generator"

model = VisionEncoderDecoderModel.from_pretrained(model_name)

torch.save(model, "models_1/vision_encoder.pt")
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
torch.save(feature_extractor, "models_1/feature_extractor.pt")

tokenizer = AutoTokenizer.from_pretrained("gpt2")
torch.save(tokenizer, "models_1/tokenizer.pt")



processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

torch.save(processor, "models_2/processor.pt")

model_generation = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
torch.save(model_generation, "models_2/model_generation.pt")





