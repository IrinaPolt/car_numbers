import uuid
from django.db import models


class Plate(models.Model):
    plate = models.CharField(
        max_length=9,
        verbose_name='Номер автомобиля в строчном формате',
        help_text='Допускается указание номера региона в формате двух или трех знаков'
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    # в будущем можно добавить категории автомобилей и применять различные форматы к номерам

    class Meta:
        verbose_name = 'Автомобильный номер'
        verbose_name_plural = 'Автомобильные номера'

    def __str__(self):
        return self.plate
