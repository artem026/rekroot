from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Компания', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    salary = models.CharField('Зарплата', max_length=50)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/pagination/{self.id}'

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'