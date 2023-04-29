import os
from pathlib import Path
from dotenv import load_dotenv
from app import chatbot

curr_folder = os.path.dirname(os.path.realpath(__file__))
root_folder = os.path.dirname(os.path.dirname(curr_folder))

load_dotenv(Path(root_folder) / ".env")

def main():
    chatbot.start()

if __name__ == "__main__":
    main()