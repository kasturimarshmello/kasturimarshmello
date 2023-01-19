from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.db.models.signals import pre_save
from .helpers import generate_slug
from django.dispatch import receiver

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField(theme = 'dark', options={
    'toolbarInline': True,
    'charCounterCount': False,
    'toolbarVisibleWithoutSelection': True})
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

@receiver(pre_save, sender=BlogModel)
def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = generate_slug(instance)