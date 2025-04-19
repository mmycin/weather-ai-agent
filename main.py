from lib import *
import asyncio
import os
from typing import Dict

def main() -> None:
    display("Location(Default-Dhaka): ", end="")
    location: str = input() or "Dhaka"
    result: Dict = asyncio.run(getweather(location.capitalize()))
    clear()
    
    def mainloop() -> None:
        while True:
            display("You: ", end="")
            prompt: str = input()
            is_bye: bool = isBye(prompt)
            if is_bye or prompt.__contains__("bye"):
                display("AI: ", "Bye. Have a nice day.")
                break
            response: Final[str] = format(analyze(result, prompt))
            display("AI: ", response)
    mainloop()

if __name__ == "__main__":
    if os.name == 'nt':
       asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    main()