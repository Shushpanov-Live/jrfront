from django.db import models


class Voting(models.Model):
    title = models.CharField('Название выборов', max_length=50)
    number_kand = models.IntegerField('Кол-во кандидатов')
    number_izb = models.IntegerField('Кол-во избирателей')
    time = models.DateTimeField('Время')
    email = models.CharField('Почта', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
