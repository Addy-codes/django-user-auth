from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # firstname = models.CharField(max_length = 80, blank = True)
    # lastname = models.CharField(max_length = 80, blank = True)
    # email = models.CharField(max_length = 200, blank = True)
    age = models.PositiveIntegerField(null=True, blank=True)    
    profile_picture = models.ImageField(default='default.png',upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    contact_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(max_length=300, blank=True)
    
    def __str__(self):
        return self.user.username
    
    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_picture.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.profile_picture.path)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()