from django.db import models

# Create your models here.
class Post(models.Model) :
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self) :
        return self.postname

class Test(models.Model):
    test_name = models.CharField(max_length=100)
    naeyong = models.TextField()

