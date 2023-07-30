from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from Ecommerce.utils.enums import GenderEnum


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class UserProfile(models.Model):
    NAMES_MAX_LEN = 30
    PHONE_NUMBER_MAX_LEN = 14
    CITY_MAX_LEN = 20

    first_name = models.CharField(
        max_length=NAMES_MAX_LEN,
        null=False,
        blank=True
    )

    last_name = models.CharField(
        max_length=NAMES_MAX_LEN,
        null=False,
        blank=True
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LEN,
        null=False,
        blank=True
    )

    address = models.TextField(
        null=False,
        blank=True
    )

    city = models.CharField(
        max_length=CITY_MAX_LEN,
        null=False,
        blank=True
    )

    gender = models.CharField(
        choices=GenderEnum.get_values(),
        max_length=GenderEnum.get_longer_value(),
        null=False,
        blank=False
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.user.email}\'s Profile'