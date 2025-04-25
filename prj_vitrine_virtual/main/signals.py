from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver
from main.models import Image
from os import path, remove

old_file = ""


@receiver(post_delete, sender=Image)
def delete_image_file(sender, instance: Image, **kwargs):
    if path.exists(instance.file.path):
        remove(instance.file.path)


@receiver(pre_save, sender=Image)
def before_update(sender, instance: Image, **kwargs):
    if instance.id:
        global old_file
        old_file = Image.objects.get(id=instance.id).file.path


@receiver(post_save, sender=Image)
def after_update(sender, instance: Image, created, **kwargs):
    if not created:
        global old_file
        if path.exists(old_file):
            remove(old_file)
            old_file = ""
