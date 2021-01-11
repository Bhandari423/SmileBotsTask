from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError('User must enter email')

        email = self.normalize_email(email)
        user = self.model(name=name, email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)

        user.is_superuser = True
        user.is_staff=True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    post = models.ForeignKey('PostDetail', models.CASCADE, blank=True, null=True)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email


class PostDetail(models.Model):
    post_image = models.ImageField()
    post_title = models.CharField(max_length=255)
    post_description = models.TextField()
    comment = models.ForeignKey('CommentDetail', models.CASCADE, blank=True, null=True)


class CommentDetail(models.Model):
    comment = models.TextField()