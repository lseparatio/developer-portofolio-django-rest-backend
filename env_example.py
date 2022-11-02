import os

os.environ.setdefault('SECRET_KEY', 'a secret key generated or just some rondom caracters')
os.environ.setdefault('DEVELOPMENT', 'True')
os.environ.setdefault('DATABASE_URL', 'postgres url')
os.environ.setdefault('ALLOWED_HOSTS', '127.0.0.1')

# Rechapcha keys: https://www.google.com/recaptcha/

os.environ.setdefault('RECAPTCHA_PUBLIC_KEY', 'your rechapcha key')
os.environ.setdefault('RECAPTCHA_PRIVATE_KEY', 'your rechapcha key')

# Email settings

os.environ.setdefault('EMAIL_USE_SSL' , 'True')
os.environ.setdefault('PORT' , '465')
os.environ.setdefault('EMAIL_HOST' , 'your email host')
os.environ.setdefault('EMAIL_HOST_USER' , 'email address')
os.environ.setdefault('DEFAULT_FROM_EMAIL' , 'default email address')
os.environ.setdefault('EMAIL_HOST_PASSWORD' , 'email password')

# Stripe Key

os.environ.setdefault('STRIPE_PUBLIC_KEY' , 'provided by stripe')
os.environ.setdefault('STRIPE_SECRET_KEY' , 'provided by stripe')
os.environ.setdefault('STRIPE_CURRENCY' , 'GBP')
os.environ.setdefault('STRIPE_WH_SECRET' , 'Provided by stripe')

# Database Settings on Local Host

os.environ.setdefault('DB_NAME' , 'database name')
os.environ.setdefault('DB_USER' , 'database user')
os.environ.setdefault('DB_PASSWORD' , 'database password')
os.environ.setdefault('DB_HOST' , 'localhost')
os.environ.setdefault('DB_PORT' , 'database port')
