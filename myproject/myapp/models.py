from django.db import models

# Create your models here.

#Model for Enrollment Table
class Enrollment(models.Model):
    number_of_students = models.IntegerField()
    number_of_low_income_students = models.IntegerField()
    year = models.IntegerField()
    school_number = models.IntegerField(primary_key=True)

#Model for School Table
class School (models.Model):
    aun = models.IntegerField()
    school_name = models.CharField(max_length=255)
    school_number = models.IntegerField(primary_key=True)

#Model for Keystone Exam
class KeystoneExam(models.Model):
    school_number = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    percentage_bio_proficient = models.FloatField()
    percentage_lit_proficient = models.FloatField()
    percentage_alg_proficient = models.FloatField()

#Model for PSSA Exam
class PssaExam(models.Model):
    percentage_eng_proficient = models.FloatField()
    percentage_math_proficient = models.FloatField()
    percentage_science_proficient = models.FloatField()
    school_number = models.IntegerField(primary_key=True)
    year = models.IntegerField()

#Model for County 
class County(models.Model):
    county_id = models.IntegerField(primary_key=True)
    county_name = models.CharField(max_length=255)



    class Meta:
        db_table = 'district'

    def __str__(self):
        return self.district_name
    
    