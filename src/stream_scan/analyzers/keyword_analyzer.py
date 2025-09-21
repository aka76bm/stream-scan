# src/stream_scan/analyzers/keyword_analyzer.py

class KeywordAnalyzer:
    def __init__(self):
        self.sensitive_keywords = {
            "medical_advice": ["medical", "doctor", "physician", "diagnosis", "symptoms", "treatment", "prescription"],
            "financial_advice": ["financial", "investment", "stock", "market", "portfolio", "trading", "credit", "loan"],
            "legal_advice": ["legal", "lawyer", "attorney", "court", "judge", "lawsuit", "contract"],
        }

    def analyze(self, prompt: str) -> dict:
        flags = []
        prompt_lower = prompt.lower()
        for theme, keywords in self.sensitive_keywords.items():
            for keyword in keywords:
                if keyword in prompt_lower:
                    flags.append(f"Potential {theme.replace('_', ' ')} content")
                    break # Move to the next theme once one keyword is found
        
        return {"flags": flags}