# src/stream_scan/analyzers/toxicity_analyzer.py
import os
import logging
from googleapiclient import discovery
from googleapiclient.errors import HttpError

class ToxicityAnalyzer:
    def __init__(self):
        self.api_key = os.environ.get("PERSPECTIVE_API_KEY")
        self.enabled = bool(self.api_key)
        if not self.enabled:
            logging.warning("PERSPECTIVE_API_KEY environment variable not set. ToxicityAnalyzer is disabled.")
            self.service = None
        else:
            try:
                self.service = discovery.build(
                    "commentanalyzer",
                    "v1alpha1",
                    developerKey=self.api_key,
                    static_discovery=False,
                )
            except Exception as e:
                logging.error(f"Failed to build Perspective API client: {e}")
                self.enabled = False
                self.service = None


    def analyze(self, prompt: str) -> dict:
        if not self.enabled or not self.service:
            return {}

        analyze_request = {
            'comment': {'text': prompt},
            'requestedAttributes': {
                'TOXICITY': {},
                'SEVERE_TOXICITY': {},
                'PROFANITY': {},
                'IDENTITY_ATTACK': {},
            }
        }

        scores = {}
        try:
            response = self.service.comments().analyze(body=analyze_request).execute()
            for attribute, value in response['attributeScores'].items():
                scores[attribute.lower()] = round(value['summaryScore']['value'], 2)
        except HttpError as e:
            logging.error(f"Perspective API request failed: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred during toxicity analysis: {e}")

        return {"scores": scores}
