from django.core.management.base import BaseCommand

from appVacancies.models import Speciality

from data import specialties


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for speciality in specialties:
            Speciality.objects.create(code=speciality['code'],
                                      title=speciality['title'],
                                      logo=f"specty_{speciality['code']}.png")
