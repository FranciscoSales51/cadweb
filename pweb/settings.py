# settings.py

from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-t_-cl2580se4quu7kbgb3pfsgmvx_966^1xby%l8_2bwfgjf9&'

DEBUG = True  
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.vercel.app']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',  # Se você tiver outros apps, adicione-os aqui.
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Serve os arquivos estáticos
]

ROOT_URLCONF = 'pweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Meu context processor
                'utils.context_processors.data_atual',
            ],
        },
    },
]

WSGI_APPLICATION = 'pweb.wsgi.application'

# Database Configuration
DATABASES = {
    'default': dj_database_url.parse('postgres://neondb_owner:xgtpikmY3bA7@ep-super-cherry-a4ljnzil-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require')
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization settings
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_TZ = False
USE_L10N = True
DECIMAL_SEPARATOR = ','
THOUSAND_SEPARATOR = '.'

# Static files settings
STATIC_URL = '/static/'  # URL base para arquivos estáticos
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Caminho absoluto para o diretório onde arquivos estáticos compilados serão coletados
STATICFILES_DIRS = [BASE_DIR / 'static']  # Diretórios adicionais para procurar arquivos estáticos durante o desenvolvimento
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Usado em produção para servir os arquivos estáticos de maneira eficiente

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication settings
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
