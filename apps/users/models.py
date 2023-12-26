from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    display_name = models.CharField(
        max_length=100,
        verbose_name="Имя, Фамилия",
    )
    avatar = models.ImageField(
        upload_to=f"users/{display_name}/images/",
        verbose_name="Аватар",
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
    )
    phone_number = models.CharField(
        max_length=13,
        verbose_name="Номер телефона",
    )
    is_buyer = models.BooleanField(
        default=False,
        verbose_name="Продавец",
    )

    def __str__(self):
        return f"{self.username}"
