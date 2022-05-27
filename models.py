from django.db import models

Grade=[
    (1,'excelent'),
    (0,'average'),
    (-1,'lower')
]
class DRF(models.Model):
    email=models.EmailField()
    Author=models.CharField(max_length=100)
    uploaded=models.DateTimeField(auto_now_add=True)
    ratings=models.IntegerField(choices=Grade,default=0)


    class Meta:
        ordering=['uploaded']


    def __str__(self):
        return self.email

# Create your models here.
