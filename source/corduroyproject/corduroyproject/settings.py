from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key
SECRET_KEY = 'django-insecure-%)fu@_2t7v-w79m25s&8a&v!0)-qlcje+1#d&&!1oq3(&=nf=w'

# Debug mode
DEBUG = True

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # This is my API and the only non-default app 
    'corduroyserver',
    # CORS headers for React
    'corsheaders',
    'rest_framework',
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS Middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'corduroyproject.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'corduroyproject.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'corduroydb',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'corduroydb',
        'PORT': '5432',
    }
}

# Password validation (weakened for testing, should be re-enabled for production)
AUTH_PASSWORD_VALIDATORS = []

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# MEDIA files (useful for serving images, etc.)
MEDIA_URL = '/media/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication settings
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# Allowed hosts (adjust for production)
ALLOWED_HOSTS = ['*']  # '*' allows all hosts, use caution in production

# Session settings
SESSION_COOKIE_AGE = 1800
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# CORS configuration
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins for development

# Optional: To allow specific origins instead - Does not work so hot with GCS and dynamic IP's
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000',
#     'http://127.0.0.1:3000',
# ]

# Optional: Allow credentials (if needed)
# CORS_ALLOW_CREDENTIALS = True
