from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Article(models.Model):
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Описание')
    detail = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Подробное описание')
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name='Статус', default='new',
                              choices=status_choices)
    date = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return str(self.pk)
