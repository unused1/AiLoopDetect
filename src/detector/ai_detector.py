from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
from typing import Tuple, Dict
import re

class AIContentDetector:
    def __init__(self):
        # Load RoBERTa model fine-tuned for AI text detection
        self.model_name = "roberta-base"  # We'll fine-tune this for AI detection
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.max_length = 512

    def _get_statistical_features(self, text: str) -> Dict[str, float]:
        """
        Extract statistical features from text that might indicate AI generation
        """
        # Normalize text
        text = text.lower()
        
        # Calculate various statistical features
        features = {
            'avg_word_length': np.mean([len(word) for word in text.split()]),
            'sentence_length_variance': np.var([len(sent.split()) for sent in text.split('.')]),
            'unique_words_ratio': len(set(text.split())) / len(text.split()),
            'punctuation_ratio': len(re.findall(r'[.,!?;]', text)) / len(text),
        }
        
        return features

    def _get_model_prediction(self, text: str) -> Tuple[float, float]:
        """
        Get AI generation probability using the transformer model
        """
        # Tokenize and prepare input
        inputs = self.tokenizer(text, 
                              return_tensors="pt",
                              max_length=self.max_length,
                              truncation=True,
                              padding=True)
        
        # Get model prediction
        with torch.no_grad():
            outputs = self.model(**inputs)
            probabilities = torch.softmax(outputs.logits, dim=1)
            ai_prob = probabilities[0][1].item()  # Assuming binary classification
            
            # Calculate confidence based on probability distance from 0.5
            confidence = abs(ai_prob - 0.5) * 2
            
        return ai_prob, confidence

    def analyze_text(self, text: str) -> Dict[str, float]:
        """
        Analyze text to determine if it's AI-generated
        Returns: Dictionary with probability and confidence scores
        """
        # Get model-based prediction
        model_prob, model_conf = self._get_model_prediction(text)
        
        # Get statistical features
        stats = self._get_statistical_features(text)
        
        # Combine model and statistical analysis
        # We could train a meta-classifier here, but for now use a weighted average
        final_probability = model_prob * 0.7 + (stats['unique_words_ratio'] < 0.4) * 0.3
        
        return {
            'ai_probability': final_probability,
            'confidence': model_conf,
            'statistical_features': stats
        }

    def analyze_relationships(self, text: str, known_sources: list) -> list:
        """
        Analyze potential relationships with other content
        """
        # TODO: Implement citation and reference detection
        return []