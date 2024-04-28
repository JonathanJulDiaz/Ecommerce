from django import template

from posts.models import Category

register = template.Library()

@register.inclusion_tag("core/menu.html")
def menu():
    categories = Category.objects.all()
    return {
        "categories": categories
    }