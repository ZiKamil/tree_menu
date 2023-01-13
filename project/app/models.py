from django.db import models


class TypeMenu(models.Model):
    sys_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.sys_name}'


class Menu(models.Model):
    type = models.ForeignKey(TypeMenu, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    level = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.parent:
            q = Menu.objects.filter(id=self.parent.id).first()
            self.level = q.level+1
        else:
            self.level = 0
        return super().save(force_insert, force_update, using, update_fields)
