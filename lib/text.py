from termcolor import colored
from typing import Final
import re

def display(role: str, text: str = "", end: str = "\n\n"):
    print(colored(role, "green"), end="")
    print(text, end=end)
    
def format(text: str) -> str:
    if text.__contains__("<think>") or text.__contains__("</think>"):
        compiler: Final[re.Pattern] = re.compile(r"<think>.*?</think>\s*", re.DOTALL)
        output: Final[str] = compiler.sub("", text).strip()
        return output
    return text