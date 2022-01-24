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

    def __str__(self):
        return self.title


class Book_libComent(models.Model):
    books = models.ForeignKey(BookCategory,on_delete=models.CASCADE,
                              related_name='book_lib_comment')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.books.title

class Expert(models.Model):
    name = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    info_exp = models.TextField()

    def __str__(self):
        return self.name


class ExpertRecomendation(models.Model):
    book_recomendation = models.TextField()
    expert_selection = models.ForeignKey(Expert, on_delete=models.CASCADE)
    book_selection = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name='books')



