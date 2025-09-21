# scanner.py
from .models import ScanResult
from .analyzers import (
    KeywordAnalyzer,
    InjectionAnalyzer,
    ReadabilityAnalyzer,
    ToxicityAnalyzer,
)

class StreamScanner:
    def __init__(self):
        self.analyzers = []
        self.register_default_analyzers()

    def register_default_analyzers(self):
        self.register_analyzer(KeywordAnalyzer())
        self.register_analyzer(InjectionAnalyzer())
        self.register_analyzer(ReadabilityAnalyzer())
        self.register_analyzer(ToxicityAnalyzer())

    def register_analyzer(self, analyzer):
        self.analyzers.append(analyzer)

    def scan(self, prompt: str) -> ScanResult:
        all_flags = []
        all_scores = {}
        details_list = []

        for analyzer in self.analyzers:
            # Each analyzer will have an `analyze` method
            result = analyzer.analyze(prompt)
            
            flags = result.get('flags', [])
            if flags:
                all_flags.extend(flags)
                details_list.extend(flags) # Add flags to details for now

            all_scores.update(result.get('scores', {}))

        # Determine overall validity
        is_valid = len(all_flags) == 0
        details_msg = "\n".join(details_list)

        return ScanResult(
            is_valid=is_valid,
            flags=all_flags,
            scores=all_scores,
            details=details_msg
        )
