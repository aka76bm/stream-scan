# src/stream_scan/analyzers/readability_analyzer.py
import re

class ReadabilityAnalyzer:
    def analyze(self, prompt: str) -> dict:
        scores = {}

        # Word count
        words = re.findall(r'\S+', prompt)
        word_count = len(words)
        scores['word_count'] = word_count

        if word_count == 0:
            scores['sentence_count'] = 0
            scores['average_word_length'] = 0
            return {"scores": scores}

        # Sentence count
        sentences = re.split(r'[.!?]+', prompt)
        # Filter out empty strings that can result from splitting
        sentence_count = len([s for s in sentences if s.strip()])
        scores['sentence_count'] = sentence_count

        # Average word length
        total_word_length = sum(len(word) for word in words)
        average_word_length = total_word_length / word_count
        scores['average_word_length'] = round(average_word_length, 2)

        return {"scores": scores}
