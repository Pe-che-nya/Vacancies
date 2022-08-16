from django.db import models


class Speciality(models.Model):
    code = models.CharField(max_length=120, default=None)
    title = models.CharField(max_length=120, default=None)
    logo = models.URLField(default='https://place-hold.it/100x60')


class Company(models.Model):
    name = models.CharField(max_length=120, default=None)
    location = models.CharField(max_length=120)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()


class Vacancy(models.Model):
    title = models.CharField(max_length=120, default=None)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=250, default=None)
    description = models.TextField(default=None)
    salary_min = models.FloatField(default=None)
    salary_max = models.FloatField(default=None)
    published_at = models.DateTimeField()