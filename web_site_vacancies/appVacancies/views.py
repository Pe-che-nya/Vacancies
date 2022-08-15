from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from appVacancies.models import Company, Speciality, Vacancy
# Create your views here.

class MainPage(ListView):
    model = Speciality
    template_name = 'appVacancies/index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'specialities': Speciality.objects.values('title', 'logo'),
            'companies': Company.objects.values('logo')
        })
        return context


class AllVacanciesView(ListView):
    model = Vacancy
    template_name = 'appVacancies/vacancies.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "vacancies": Vacancy.objects.all()

        })

        return context

class CatVacanciesView(ListView):
    model = Vacancy, Speciality
    template_name = 'appVacancies/vacancies-cat.html'
    def get_queryset(self):


        s = Speciality.objects.filter(code=self.kwargs['category'])
        self.primer = s.values('code')
        #queryset=Vacancy.objects.filter(speciality=int(s))
        return s#Vacancy.objects.filter(cat=self.speciality)
    def get_context_data(self, *, object_list=None, **kwargs):
        context= super().get_context_data(**kwargs)
        context['primer']=self.primer
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



