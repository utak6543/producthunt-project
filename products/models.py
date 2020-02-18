from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    body = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default = 1)
    hunter = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    def summary(self):
        return self.body [:70]
    def pub_date_pretty(self):
        return self.pub_date.strftime('%c')
