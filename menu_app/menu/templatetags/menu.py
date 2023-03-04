from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse

from menu.models import Category


register = template.Library()


caches: list = list()


def get_elem_from_caches(elem):
    for i in caches[0]:
        if i == elem:
            return i
    return None


def get_tree_categories(objs):
    tree = dict()
    for obj in objs[0]:
        tree.update({obj.name: get_children(obj, dict())})
    return tree


def get_children(obj, children):
    query = get_elem_from_caches(obj).category_set.all()
    if query:
        children.update(
            {i.name: get_children(i, dict()) for i in query}
        )
    else:
        children.update({obj.name: None})
    return children


def draw_tree(tree: dict, url):
    html_tags = []
    if tree is not None:
        for k, v in tree.items():
            if v is not None:
                html_tag = '<li class="submenu {}">'.format('active' if k in url else '') +\
                           '<a href="{}">'.format(reverse('category', kwargs={'category_name': k})) + k + '</a>' + \
                           '<ul>' + draw_tree(v, url) + '</ul>' + '</li>'
                html_tags.append(html_tag)
    return ''.join(html_tags)


@register.simple_tag
def draw_menu(request):
    categories = Category.objects.prefetch_related('category_set')
    caches.append(categories)
    categories_tree = get_tree_categories(caches)
    menu = draw_tree(categories_tree, request.path_info)
    return mark_safe('<nav>' + '<ul>' + menu + '</ul>' + '</nav>' + '</div>')
