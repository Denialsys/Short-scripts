'''
    Simple use of .env files
    Reference: https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1#:~:text=Using%20a%20.,same%20project%20that%20utilizes%20them.
'''

# ## Sample script for loading .env using target file
# from dotenv import load_dotenv
# from pathlib import Path
#
# dotenv_path = Path('path/to/.env')
# load_dotenv(dotenv_path=dotenv_path)

import os
from dotenv import load_dotenv

load_dotenv()

THE_NORM = os.getenv('THE_NORM')
STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')

print(THE_NORM)
print(STORAGE_BUCKET_NAME)