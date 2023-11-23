from django.db import models

# Create your models here.
class District(models.Model):
    district_name = models.CharField(max_length=255, db_column='district_name')

    class Meta:
        db_table = 'district'

    def __str__(self):
        return self.district_name