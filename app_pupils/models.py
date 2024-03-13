from django.db import models


# Create your models here.

class pupils(models.Model):
    name = models.CharField(max_length=100)
    grade1 = models.IntegerField()
    grade2 = models.IntegerField()
    grade3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pupils'
