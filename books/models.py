from django.db import models
from django.contrib.auth.models import User




class Books(models.Model):
    Category = (
    ('Statistic' , 'Statistic'),
    ('Mechanics' , 'Mechanics'),
    ('Networks' , 'Networks'),
    ('Electronics' , 'Electronics'),
    ('Machine Learning' , 'Machine Learning'),
    ('Biology' , 'Biology'),
    ('Physics' , 'Physics'),
    ('Computer Science' , 'Computer Science'),
    ('Big Data' , 'Big Data'),
)

    Title = models.CharField( max_length=50) 
    Category = models.CharField(choices=Category , default='Statistic' ,max_length=50)
    Views = models.IntegerField(default=0)
    ISBN = models.CharField( max_length=50) 
    Author = models.CharField(max_length=50)
    Yop = models.CharField( max_length=50)
    Publisher = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Bookies")

    def __str__(self):
        return self.Title
    
    def get_avg_rating(self):
        all_reviews = self.book_rate.all()
        all_rating = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_rating += review.rate
            return round(all_rating/len(all_reviews),2)
        else:
            return '0.0'

    def book_check(self):
        if self.book_rate > 0:
            return None



class Ratings(models.Model):
    Rating_Choises =(
    (1.0 , '1.0'),
    (2.0 , '2.0'),
    (3.0 , '3.0'),
    (4.0 , '4.0'),
    (5.0 , '5.0'),
    )
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    books = models.ForeignKey(Books , related_name='book_rate', on_delete=models.CASCADE)
    rate = models.FloatField(choices=Rating_Choises,default=0.0)

    class Meta:
        verbose_name = ("Rating")
        verbose_name_plural = ("Ratings")

    def __str__(self):
        return str(self.user.username)




