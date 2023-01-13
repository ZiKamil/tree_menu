from app.models import Menu
from django.views import generic
from django.db.models import Q


class MenuListView(generic.ListView):
    model = Menu
    template_name = 'base_generic.html'


class MenuDetailView(generic.DetailView):
    model = Menu
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        childrens = None
        if kwargs['object'].parent is not None:
            q = Menu.objects.select_related("type").filter(Q(type__sys_name=self.object.type.sys_name) & Q(Q(parent=self.object.id) | Q(parent=self.object.parent.parent))).all()
            menu_name = q.first().type.name
            childrens = []
            parents = []
            for i in q:
                if i.level > self.object.level:
                    childrens.append(i)
                if i.level < self.object.level:
                    parents.append(i)
            currents = [self.object]
        else:
            q = Menu.objects.select_related("type").filter(Q(type__sys_name=self.object.type.sys_name) & Q(Q(level=0) | Q(level=1))).all()
            menu_name = q.first().type.name
            currents = []
            parents = []
            for i in q:
                if i.level == 1:
                    currents.append(i)
                if i.level == 0:
                    parents.append(i)
        context.update({
            'childrens': childrens,
            'currents': currents,
            'parents': parents,
            'menu_name': menu_name
        })

        return context
