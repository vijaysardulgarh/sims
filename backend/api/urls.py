from django.contrib import admin
from django.urls import path, include

# ==========================================
# MASTER API ROUTER
# Routes requests to the appropriate isolated app
# ==========================================

urlpatterns = [
    # 🔐 Authentication & Users
    path('accounts/', include('apps.accounts.urls')),
    
    # 📚 Core Academics & Structure
    path('academics/', include('apps.academics.urls')),
    path('timetable/', include('apps.timetable.urls')),
    
    # 🧑‍🏫 Staff & Student Management
    path('staff/', include('apps.staff.urls')),
    path('students/', include('apps.students.urls')),
    
    # 💰 Finance & Operations
    path('finance/', include('apps.finance.urls')),
    path('library/', include('apps.library.urls')),
    
    # 🏅 Extracurriculars & Governance
    path('associations/', include('apps.associations.urls')),
    
    # 🌐 Public Website Content (React Frontend pages)
    path('website/', include('apps.website.urls')),
]