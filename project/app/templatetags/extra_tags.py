from django import template
from django.template.loader import render_to_string
from ..models import Menu
from django.db.models import Q

register = template.Library()


@register.simple_tag
def draw_menu(name):
    context = {}
    q = Menu.objects.select_related("type").filter(Q(type__sys_name=name) & Q(Q(level=0) | Q(level=1))).all()
    currents = []
    parents = []
    for i in q:
        if i.level == 1:
            currents.append(i)
        if i.level == 0:
            parents.append(i)

    context.update({
        'parents': parents,
        'currents': currents,
        'menu_name': q.first().type.name
    })
    return render_to_string('index.html', context, None)
