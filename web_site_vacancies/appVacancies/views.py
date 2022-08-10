from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from appVacancies.models import StartModel
# Create your views here.

class MainPage(ListView):
    model = StartModel
    template_name = 'appVacancies/index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['start'] ="fasdasasfasf"
        return context


class AllVacanciesView(ListView):
    model = StartModel
    template_name = 'appVacancies/vacancies.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['start'] ="fasdasasfasf"
        return context

class CatVacanciesView(ListView):
    model = StartModel
    template_name = 'appVacancies/vacancies.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['start'] ="fasdasasfasf"
        return context

class DetailCompanyView(DetailView):
    model = StartModel
    template_name = 'appVacancies/company.html'
    def get_queryset(self):
        return StartModel.objects.filter(pk=1)

def test(request):
    ur='appVacancies/test.html'
    context={"Hello":'Hello'}
    return render(request,ur,context=context)



