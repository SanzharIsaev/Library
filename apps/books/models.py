from djongo import models as mongo_models


class Book(mongo_models.Model):
    
    id = mongo_models.ObjectIdField()
    
    name = mongo_models.CharField(
        max_length=100,
        verbose_name='Название книги'
    )

    author = mongo_models.CharField(
        max_length=100,
        verbose_name='Автор'
    )
    
    description = mongo_models.TextField(
        verbose_name='Описание книги'
    )
    
    year_of_publishing = mongo_models.PositiveIntegerField(
        verbose_name='Год издания'
    )

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.name
