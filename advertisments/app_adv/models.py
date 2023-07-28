from django.db import models

# Create your models here.
class Advertisements(models.Model):
    title=models.CharField("Заголовок", max_length=128)
    description=models.TextField("Описание")
    price=models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction=models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    # def __str__(self):