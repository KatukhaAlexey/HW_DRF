from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время начала измерений')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время последнего измерения')
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='measurements',
        default=None
    )
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'{self.sensor.name} {self.temperature}'
