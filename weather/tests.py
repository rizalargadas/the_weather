from dotenv import load_dotenv
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Support env variables from .env file if defined
env_path = load_dotenv(os.path.join(BASE_DIR, '.env'))
load_dotenv(env_path)

SECRET_KEY = os.getenv('SECRET_KEY')
API_KEY = os.getenv('WEATHER_API_KEY')
print(SECRET_KEY)
