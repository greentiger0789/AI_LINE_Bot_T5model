from random import choice
# from time import sleep
import torch
from transformers import T5ForConditionalGeneration
import re


class MockMLAPI:
    def __init__(self):
        # model instanse
        self.model = None

    def load(self, MODEL_DIR):
        """
        when server is activated, load weight or use joblib or pickle for performance improvement.
        then, assign pretrained model instance to self.model.
        """
        model = T5ForConditionalGeneration.from_pretrained(MODEL_DIR)
        return model

    def predict(self, text, model, tokenizer):
        """implement followings
        - Load data
        - Preprocess
        - Prediction using self.model
        - Post-process
        """

        inputs = tokenizer.encode(
            text, return_tensors="pt", max_length=16, truncation=True)
        model.eval()

        with torch.no_grad():
            summary_ids = model.generate(inputs)
            summary = tokenizer.decode(summary_ids[0])
            summary = re.sub(r"\D", "", summary)
        return summary
