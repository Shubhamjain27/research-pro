from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import os


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,null=True, blank=True)
    location = models.CharField(max_length=30,null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True,
                                      width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    skills_needed = models.CharField(max_length=10000,null=True, blank=True)
    other_info = models.TextField(max_length=10000,null=True, blank=True)
    Description = models.TextField(max_length=10000,null=True, blank=True)


    def __str__(self):
        return str(self.user)

@receiver(post_save,  sender=settings.AUTH_USER_MODEL)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Profile2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    University = models.CharField(max_length=100, null=True)
    Country = models.CharField(max_length=100, null=True)


@receiver(post_save,  sender=settings.AUTH_USER_MODEL)
def update_user_profile2(sender, instance, created, **kwargs):
    if created:
        Profile2.objects.create(user=instance)
    instance.profile.save()


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)
    cover_letter = models.TextField(max_length=10000, null=True, blank=True)

    @classmethod
    def make_friend(cls, current_user, new_friend, cover_letter):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.cover_letter = cover_letter


class Applicant2(models.Model):
    user = models.ForeignKey(User, related_name="student", null=True)
    prof = models.ForeignKey(User, related_name="prof", null=True)
    cover_letter = models.TextField(max_length=10000, null=True, blank=True)
    user2 = models.TextField(max_length=10000, null=True, blank=True)


    class Meta:
        unique_together = (('user', 'prof'),)
    @classmethod
    def make_friend2(cls, current_user, prof):
        application2, created = cls.objects.get_or_create(user=current_user)
        application2.prof = prof





