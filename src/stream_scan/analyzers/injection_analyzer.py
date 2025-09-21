# src/stream_scan/analyzers/injection_analyzer.py

class InjectionAnalyzer:
    def __init__(self):
        self.injection_phrases = [
            "ignore the above instructions",
            "ignore previous instructions",
            "ignore all previous instructions",
            "disregard the above instructions",
            "disregard previous instructions",
            "act as",
            "you are a",
            "your instructions are",
            "system prompt",
            "jailbreak",
            "forget everything and start over",
            "you are now in",
            "you are an unfiltered",
        ]

    def analyze(self, prompt: str) -> dict:
        flags = []
        prompt_lower = prompt.lower()
        for phrase in self.injection_phrases:
            if phrase in prompt_lower:
                flags.append(f"Potential prompt injection: found phrase '{phrase}'")
        
        return {"flags": flags}
