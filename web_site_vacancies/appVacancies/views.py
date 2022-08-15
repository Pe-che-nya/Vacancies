from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from appVacancies.models import Company,Speciality, Vacancy
# Create your views here.

class MainPage(ListView):
    model = Speciality
    template_name = 'appVacancies/index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['start'] ="fasdasasfasf"
        return context


class AllVacanciesView(ListView):
    model = Company
    template_name = 'appVacancies/vacancies.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['start'] ="fasdasasfasf"
        return context

class CatVacanciesView(ListView):
    model = Company
    template_name = 'appVacancies/vacancies.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['start'] ="fasdasasfasf"
        return context

class DetailCompanyView(DetailView):
    model = Company
    template_name = 'appVacancies/company.html'
    def get_queryset(self):
        return StartModel.objects.filter(pk=1)

def test(request):
    ur='appVacancies/test.html'
    context={"Hello":'Hello'}
    return render(request,ur,context=context)



