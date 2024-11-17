from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.
    """
    def create_user(self, email, username, password=None, **extra_fields):
        """
        Create and return a regular user with the given email, username, and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Create and return a superuser with the given email, username, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser.
    """
    email = models.EmailField(unique=True)  # Make email mandatory and unique
    date_of_birth = models.DateField(null=True, blank=True)  # Optional date of birth
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)  # Profile picture

    objects = CustomUserManager()  # Assign the custom manager

    REQUIRED_FIELDS = ['email', 'date_of_birth']  # Fields required during superuser creation
    USERNAME_FIELD = 'username'  # Field used for authentication

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"