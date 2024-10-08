from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )
    position = models.CharField(
        max_length=100,
        verbose_name="Должность"
    )
    photo = models.ImageField(
        upload_to='photo_image/'
    )
    bio = models.TextField(
        verbose_name='Биография сотрудника'
    )