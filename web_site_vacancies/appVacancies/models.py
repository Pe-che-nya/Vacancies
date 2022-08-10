from django.db import models


class StartModel(models.Model):
    start_fields = models.TextField(default='dsfsdsdf')


class Speciality(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    logo = models.ImageField()
    description = models.TextField()
    employee_count = models.IntegerField


class Company(models.Model):
    code = models.CharField(max_length=28)
    title = models.CharField(max_length=120)
    picture = models.ImageField()


class Vacancy(models.Model):
    title = models.CharField(max_length=120)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=120)
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateTimeField()