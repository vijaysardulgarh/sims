from django.utils.text import slugify


def generate_unique_slug(instance, field_value):
    return slugify(field_value)