# This file is the entry point for NGINX and Gunicorn for deployment
import sys
import os

from developer_portofolio_backend.wsgi import application
