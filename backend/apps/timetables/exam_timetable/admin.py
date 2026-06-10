from django.contrib import admin
from .models import *

admin.site.register(list(globals().values())[0])
