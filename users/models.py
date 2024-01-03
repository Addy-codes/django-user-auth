from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # firstname = models.CharField(max_length = 80, blank = True)
    # lastname = models.CharField(max_length = 80, blank = True)
    # email = models.CharField(max_length = 200, blank = True)
    age = models.PositiveIntegerField(null=True, blank=True)    
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    contact_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(max_length=300, blank=True)
    
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()