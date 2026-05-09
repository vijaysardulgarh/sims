from django.contrib import admin
from django.urls import path, include

# ==========================================
# MASTER API ROUTER
# Routes requests to the appropriate isolated app
# ==========================================

urlpatterns = [
    
    # ✅ Django Admin
    path('admin/', admin.site.urls),

    # 🔐 Authentication & Users
    path('users/', include('apps.users.urls')),
    
    # 📚 Core Academics & Structure
    path('academics/', include('apps.academics.urls')),
    
    # 🧑‍🏫 Staff & Student Management
    path('staff/', include('apps.staff.urls')),
    path('students/', include('apps.students.urls')),
    
    # 💰 Finance & Operations
    path('finance/', include('apps.finance.urls')),
    path('library/', include('apps.library.urls')),
    
    # 🏅 Extracurriculars & Governance
    path('associations/', include('apps.associations.urls')),
    
    # 🌐 Public Website Content (React Frontend pages)

    path("api/website/", include("apps.website.urls")),
    path("api/documents/", include("apps.documents.urls")),
    path("api/finance/", include("apps.finance.urls")),
    path("api/",include("apps.students.urls")
),

]