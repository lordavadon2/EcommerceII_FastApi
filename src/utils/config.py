import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'cart')
LIQPAY_PUBLIC_KEY = os.getenv('LIQPAY_PUBLIC_KEY')
LIQPAY_PRIVATE_KEY = os.getenv('LIQPAY_PRIVATE_KEY')
