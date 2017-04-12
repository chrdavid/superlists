from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('-text',)
