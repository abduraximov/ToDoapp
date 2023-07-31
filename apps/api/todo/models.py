from django.db import models
from apps.api.common.models import BaseModel
from django.utils.text import slugify


class Todo(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, max_length=128)
    desc = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Todo, self).save(*args, **kwargs)

