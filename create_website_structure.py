# create_website_structure.py

import os

# ==========================================
# BASE PATH
# ==========================================

BASE_DIR = "website"

# ==========================================
# WEBSITE STRUCTURE
# ==========================================

STRUCTURE = {

    "apps": {

        "website": {

            "__init__.py": "",

            "models": {
                "__init__.py": "",
                "page.py": "",
                "banner.py": "",
                "news.py": "",
                "gallery.py": "",
                "menu.py": "",
                "footer.py": "",
                "contact.py": "",
            },

            "serializers": {
                "__init__.py": "",
                "page_serializer.py": "",
                "banner_serializer.py": "",
                "news_serializer.py": "",
                "gallery_serializer.py": "",
            },

            "views": {
                "__init__.py": "",
                "page_views.py": "",
                "banner_views.py": "",
                "news_views.py": "",
                "gallery_views.py": "",
            },

            "urls": {
                "__init__.py": "",
                "page_urls.py": "",
                "banner_urls.py": "",
                "news_urls.py": "",
                "gallery_urls.py": "",
            },

            "admin": {
                "__init__.py": "",
                "page_admin.py": "",
                "banner_admin.py": "",
                "news_admin.py": "",
                "gallery_admin.py": "",
            },

            "services": {
                "__init__.py": "",
                "seo_service.py": "",
                "media_service.py": "",
            },

            "permissions": {
                "__init__.py": "",
                "website_permissions.py": "",
            },

            "selectors": {
                "__init__.py": "",
                "website_selectors.py": "",
            },

            "tests": {
                "__init__.py": "",
                "test_pages.py": "",
                "test_news.py": "",
            },

            "migrations": {
                "__init__.py": "",
            },
        },
    },

    "frontend": {

        "src": {

            "components": {

                "layout": {
                    "Navbar.jsx": "",
                    "Sidebar.jsx": "",
                    "Footer.jsx": "",
                },

                "home": {
                    "HeroSection.jsx": "",
                    "BannerSlider.jsx": "",
                    "LatestNews.jsx": "",
                    "GallerySection.jsx": "",
                },

                "common": {
                    "Loader.jsx": "",
                    "Button.jsx": "",
                    "Card.jsx": "",
                },
            },

            "pages": {
                "Home.jsx": "",
                "About.jsx": "",
                "Contact.jsx": "",
                "Gallery.jsx": "",
                "News.jsx": "",
                "404.jsx": "",
            },

            "services": {
                "api.js": "",
                "websiteService.js": "",
            },

            "routes": {
                "AppRoutes.jsx": "",
            },

            "assets": {
                "images": {},
                "icons": {},
            },

            "styles": {
                "main.css": "",
            },

            "App.jsx": "",
            "main.jsx": "",
        },

        "public": {
            "favicon.ico": "",
            "robots.txt": "",
        },
    },

    "templates": {
        "base.html": "",
        "index.html": "",
    },

    "media": {},

    "static": {

        "css": {},
        "js": {},
        "images": {},
    },

    "requirements.txt": "",

    ".env": "",

    "manage.py": "",
}


# ==========================================
# CREATE STRUCTURE FUNCTION
# ==========================================

def create_structure(base_path, structure):

    for name, content in structure.items():

        path = os.path.join(base_path, name)

        # ==================================
        # IF FOLDER
        # ==================================

        if isinstance(content, dict):

            os.makedirs(path, exist_ok=True)

            create_structure(path, content)

        # ==================================
        # IF FILE
        # ==================================

        else:

            os.makedirs(
                os.path.dirname(path),
                exist_ok=True
            )

            with open(path, "w", encoding="utf-8") as file:

                file.write(content)

            print(f"Created File: {path}")


# ==========================================
# RUN SCRIPT
# ==========================================

if __name__ == "__main__":

    os.makedirs(BASE_DIR, exist_ok=True)

    create_structure(BASE_DIR, STRUCTURE)

    print("\n✅ Website structure created successfully!")