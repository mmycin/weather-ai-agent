from smartfunc import backend
from typing import Final, Dict

ai: Final[object] = backend("llama3.2:latest", 
    system="""
    You are an AI agent for weather API. 
    Be least verbose and to the point friendly answer.
    Do not use Markdown format, just normal plain text and keep it as short as possible.
    """)

@ai
def analyze(api: Dict, prompt: str):
    """Analyze the data {{ api }} and do {{ prompt }}"""
    ...

@ai
def isBye(text: str):
    """Check if the text "{{ text }}" indicates farewell (e.g., bye, goodbye, see you, that's all). 
    If yes, return 1. If not, return 0. Return ONLY the number with NO EXTRA TEXT."""
    ...