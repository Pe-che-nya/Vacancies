from django.core.management.base import BaseCommand

from appVacancies.models import Company

from data import companies


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for company in companies:
            Company.objects.create(name=company['title'],
                                   location=company['location'],
                                   logo=company['logo'],
                                   description=company['description'],
                                   employee_count=company['employee_count'])
