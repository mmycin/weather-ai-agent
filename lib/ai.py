from smartfunc import backend
from typing import Final, Dict

ai: Final[object] = backend("gemma3:1b", 
    system="""
    You are an AI agent for weather API. 
    Be least verbose and to the point friendly answer.
    Do not use Markdown format, just normal plain text and keep it as short as possible.
    You are not going to answer ANY question that is not relevent to Weather. Maintain it strictly.
    """)

@ai
def analyze(api: Dict, prompt: str):
    """Analyze the data {{ api }} and do {{ prompt }}"""
    ...

@ai
def bye(text: str):
    """Check if the text "{{ text }}" indicates farewell (e.g., bye, goodbye, see you, that's all) 
    of the conversation. 
    If yes, return 1. If not, return 0. Return ONLY the number with NO EXTRA TEXT."""
    ...
    
def isBye(text: str) -> bool:
    response: str = bye(text)
    output: bool = bool(int(response)) or False
    return output