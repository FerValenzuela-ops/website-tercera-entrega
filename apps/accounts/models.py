from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserInterest(models.Model):
    # owner
    name = models.CharField(max_length=64, null=True)
    normalized_name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name


class UserPersona(models.Model):
    # owner
    name = models.CharField(max_length=64, null=True)
    normalized_name = models.CharField(max_length=64, null=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    # owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # settings
    is_full_name_displayed = models.BooleanField(default=True)

    # details
    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)
    interests = models.ManyToManyField(UserInterest, blank=True)

    rut = models.CharField("Rut", max_length=50, blank=True)
    direccion = models.CharField("Direccion", max_length=50, blank=True)
    telefono = models.CharField("Telefono", max_length=50, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
