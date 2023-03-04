from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=_('name'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('parent'))

    def __str__(self):
        return self.name
