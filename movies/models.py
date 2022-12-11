from django.db import models

# Create your models here.

class Moviedata(models.Model):
    # Objectではなくstringを返すように指示
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=200,default='action')
    image = models.ImageField(upload_to='Images/',default="Images/None/Noimg.jpg")
    movie = models.FileField(upload_to='Images/',blank=True)  # 動画ファイル用