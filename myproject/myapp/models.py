from django.db import models

# Create your models here.

class Enrollment(models.Model):
    number_of_students = models.IntegerField()
    number_of_low_income_students = models.IntegerField()
    year = models.IntegerField()
    percentage_of_low_income_students = models.IntegerField()
    school_number = models.IntegerField()


class District(models.Model):
    district_name = models.CharField(max_length=255, db_column='district_name')

    class Meta:
        db_table = 'district'

    def __str__(self):
        return self.district_name
    
    