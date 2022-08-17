from django.core.management.base import BaseCommand

from appVacancies.models import Speciality, Company, Vacancy

from data import jobs


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for job in jobs:
            spec = Speciality.objects.get(code=job['specialty'])
            com = Company.objects.get(id=job['company'])
            Vacancy.objects.create(title=job['title'],
                                   speciality=spec,
                                   company=com,
                                   skills=job['skills'],
                                   description=job['description'],
                                   salary_min=job['salary_from'],
                                   salary_max=job['salary_to'],
                                   published_at=job['posted'])
