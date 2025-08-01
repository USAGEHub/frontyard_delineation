# config/config.py

import os

# Define the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Define the parent of the project root directory (one directory up from the project root)
PARENT_DIRECTORY = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))

# Define other configurations relative to the project root
DATA_PATH = os.path.join(PARENT_DIRECTORY, 'data')
OUTPUT_PATH = os.path.join(PROJECT_ROOT, 'outputs')

# # Verify paths for debugging
# print(f"Project Root: {PROJECT_ROOT}")
# print(f"Data Path: {DATA_PATH}")
# print(f"Output Path: {OUTPUT_PATH}")
