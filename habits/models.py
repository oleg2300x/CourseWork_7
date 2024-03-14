from django.db import models
from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class NiceHabit(models.Model):
    """Хорошие привычки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=50, **NULLABLE, verbose_name='Место')
    action = models.CharField(max_length=50, verbose_name='Действие')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Хорошая привычки'
        verbose_name_plural = 'Хорошие привычки'


class Habit(models.Model):
    """Model for Habit"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    time = models.TimeField(verbose_name='Время')
    place = models.CharField(max_length=50, verbose_name='Место')
    action = models.CharField(max_length=50, verbose_name='Действие')
    reward = models.CharField(max_length=50, **NULLABLE, verbose_name='Вознаграждение')
    associated_nice_habit = models.ForeignKey(NiceHabit, on_delete=models.SET_NULL,
                                              **NULLABLE, verbose_name='Признак полезной привычки')
    periodicity = models.PositiveIntegerField(verbose_name='Переодичнось')
    is_public = models.BooleanField(default=False, verbose_name='Публичность')
    duration_time = models.TimeField(verbose_name='Время действия')
    next_date = models.DateField(**NULLABLE, verbose_name="Дата следующего напоминания")

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
