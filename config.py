import os

############################################################################
# Flask-Login
############################################################################
SECRET_KEY = os.urandom(128)
CSRF_SECRET_KEY = os.urandom(256)
############################################################################
# System
############################################################################
SYSTEM_MODE = "DEV"
ROOT_DIR = os.getcwd() + "/"
############################################################################
# Image Formate
############################################################################
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'svg'}
IMAGE_FORMATS = {
    "news": {
        "main_image": {
            "width": "1920",
            "height": "0"
        },
        "teaser_image": {
            "width": "480",
            "height": "480"
        },
        "meta_image": {
            "width": "1920",
            "height": "0"
        }
    },
    "pages": {
        "slider_images": {
            "width": "1920",
            "height": "0"
        },
        "head_image": {
            "width": "1920",
            "height": "0"
        },
        "teaser_image": {
            "width": "480",
            "height": "480"
        },
        "meta_image": {
            "width": "1920",
            "height": "0"
        }
    }
}
