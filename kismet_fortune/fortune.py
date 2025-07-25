"""Core fortune generation functionality."""
import os
from typing import Optional
from google import genai
from google.genai import types


class FortuneGenerator:
    """Generates fortunes using Google's Gemini API."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        self.client = genai.Client(api_key=self.api_key)
        self.system_instruction = (
            "You are Kismet, the evolution of Slackware's venerable fortune-mod oracle. "
            "Respond with 'Kismet reveals:' or similar variations, then provide an "
            "aphorism, proverb, quote, or short wisdom. It can be witty, deep, funny, capriciously flirtaeous,"
            "or insightful in tone. Include an attribution at the end."
        )
    
    def generate(self, prompt: str = "Tell me my fortune") -> str:
        """Generate a fortune based on the given prompt."""
        try:
            chat = self.client.models.generate_content_stream(
                model='gemini-2.5-flash-exp',
                config=types.GenerateContentConfig(system_instruction=self.system_instruction),
                contents=prompt
            )
            
            full_text = ""
            for message in chat:
                full_text += message.text
            
            return full_text.strip() if full_text else "Kismet is silent."
            
        except Exception as e:
            raise RuntimeError(f"Fortune generation failed: {e}")