from torch import  load, cuda
from PIL import Image
import torch


class model_1:
    def __init__(self, path):
        self.path = path
        pass


    def ret_caption(self):
        model = load("models_1/vision_encoder.pt")
        feature_extractor = load("models_1/feature_extractor.pt")
        
        tokenizer = load("models_1/tokenizer.pt")
        device = torch.device("cuda" if cuda.is_available() else "cpu")

        path = self.path

        img = Image.open(path)

        if img.mode != 'RGB':
            img = img.convert(mode='RGB')

        
        pixel_values = feature_extractor(images=[img], return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(device)

        max_length=128
        num_beams=5

        output_ids = model.generate(pixel_values, num_beams=num_beams, max_length=max_length)

        # decode the generated prediction
        preds = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return preds




class model_2:
    def __init__(self, path, text):
        self.path  = path
        self.text = text
        pass

    def ret_caption(self):
        processor = load("models_2/processor.pt")

        model = load("models_2/model_generation.pt")

        raw_image = Image.open(self.path)

        inputs = processor(raw_image, self.text, return_tensors="pt")

        out = model.generate(**inputs)
        return processor.decode(out[0], skip_special_tokens= True)
    


        


