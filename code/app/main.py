#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)
import os
# from dotenv import load_dotenv
from pathlib import Path

# # Get the folder this file is in:
# this_file_folder = os.path.dirname(os.path.realpath(__file__))
# # Get the parent folder of this file's folder:
# parent_folder = os.path.dirname(this_file_folder)

# load_dotenv(Path(parent_folder) / ".env")

from app import bot

def main():
    bot.start()

if __name__ == "__main__":
    main()