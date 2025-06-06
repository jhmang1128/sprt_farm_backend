"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os


from dotenv import load_dotenv
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


#### SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
# SECRET_KEY = os.getenv('api_key') # 예시


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


#### SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']
# LOGOUT_REDIRECT_URL = "/"


#### acess permmision (외부 접속 허용 list)
# CORS_ALLOWED_ORIGINS = True


#### Application definition
AUTH_USER_MODEL = 'users.CustomUser'


#############################################################################################
### INSTALLED_APPS
#############################################################################################
INSTALLED_APPS = [
    #### default
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    
    #### drf
    "rest_framework",
    "rest_framework.authtoken",
    
    
    #### 외부 통신
    'corsheaders', 

    
    #### auth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.kakao", #카카오톡
    
    
    #### app
    "chatbot",
    "post",
    "crawled_data",
    "users",
]


MIDDLEWARE = [
    #### cors
    'corsheaders.middleware.CorsMiddleware',
    
    #### default
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
    #### allauth
    "allauth.account.middleware.AccountMiddleware",
    
]


ROOT_URLCONF = "config.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "config.wsgi.application"


#############################################################################################
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
#############################################################################################

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


#############################################################################################
# kakao
#############################################################################################

SOCIALACCOUNT_PROVIDERS = {
    "kakao": {
        "APP": {
            "client_id": "a6971a25bb35dc1113d81b5713a3ccc7",  # ✅ 여기에 카카오 REST API 키 입력
            "secret": "VFzF6RIRwUK4JZKV7QM8n4PT9qAbE4KE",  # 카카오는 secret key가 필요 없음
            "key": "",
        }
    }
}


#############################################################################################
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
#############################################################################################

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


#############################################################################################
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
#############################################################################################

#### lang
LANGUAGE_CODE = "en-us"
USE_I18N = True

#### time zone
TIME_ZONE = "UTC"
USE_TZ = True



#############################################################################################
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
#############################################################################################

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"



#############################################################################################
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
#############################################################################################

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
] # 카카오톡


SITE_ID = 1  # Django 사이트 ID
# LOGIN_REDIRECT_URL = "users"  # 로그인 후 이동할 페이지


SOCIALACCOUNT_LOGIN_ON_GET = True
# ACCOUNT_LOGOUT_REDIRECT_URL = "users"  # 로그아웃 후 이동할 페이지
ACCOUNT_EMAIL_VERIFICATION = "none"  # 이메일 인증 비활성화
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = True


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
    ),
}

