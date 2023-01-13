from django.db import models


class Plate(models.Model):
    number = models.CharField(
        max_length=9,
        verbose_name='Номер автомобиля в строчном формате',
        help_text='Допускается указание номера региона в формате двух или трех знаков'
    )

    # в будущем можно добавить категории автомобилей и применять различные форматы к номерам

    class Meta:
        verbose_name = 'Автомобильный номер'
        verbose_name_plural = 'Автомобильные номера'
        ordering = ['-id']

    def __str__(self):
        return self.number
