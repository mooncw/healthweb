from django.db import models

class Exercises(models.Model):
    id_name = models.IntegerField( primary_key=True)
    name_ko = models.CharField(max_length=50)
    name_en = models.CharField(max_length=25)
    dir = models.CharField(max_length=20)
    part = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'exercises'

