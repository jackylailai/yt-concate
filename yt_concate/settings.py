from dotenv import load_dotenv

load_dotenv()
import os
API_KEY = os.getenv("API_KEY")

DOWNLOADS_DIR = "downloads"
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR , "captions")
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR , "videos")
#拿api