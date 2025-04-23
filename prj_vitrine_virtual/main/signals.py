from django.db.models.signals import post_delete
from django.dispatch import receiver
from main.models import Image
from os import path, remove


@receiver(post_delete, sender=Image)
def delete_image_file(sender, instance: Image, **kwargs):
    if path.exists(instance.file.path):
        remove(instance.file.path)
