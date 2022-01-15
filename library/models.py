from django.db import models

# Create your models here.
class BookCategory(models.Model):
    GENRE_CHOISE = (
        ('Detective', 'Detective'),
        ('Fantasty', 'Fantasty'),
        ('Horror', 'Horror'),
        ('Dramma', 'Dramma'),
        ('FairyTales', 'FairyTales')

    )

    title = models.CharField(max_length=100)
    descrip = models.TextField()
    image = models.ImageField(upload_to='')
    tom = models.IntegerField()
    genre = models.CharField(choices=GENRE_CHOISE, max_length=100)
    date_write = models.DateField(auto_now_add=True)