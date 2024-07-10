from djongo import models as mongo_models


class Author(mongo_models.Model):
    
    id = mongo_models.ObjectIdField()
    
    name = mongo_models.CharField(
        max_length=100,
        verbose_name='Имя автора'
    )

    surname = mongo_models.CharField(
        max_length=100,
        verbose_name='Фамилия автора'
    )
    
    biography = mongo_models.TextField(
        verbose_name='Биография автора'
    )

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.name
