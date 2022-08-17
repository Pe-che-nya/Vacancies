from django.shortcuts import get_list_or_404, render

from django.views.generic import DetailView, ListView

from appVacancies.models import Company, Speciality, Vacancy


class MainPage(ListView):
    model = Speciality
    template_name = 'appVacancies/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'specialities': Speciality.objects.values('title', 'logo'),
            'companies': Company.objects.values('logo'),

        })
        return context


class AllVacanciesView(ListView):
    model = Vacancy
    template_name = 'appVacancies/vacancies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "vacancies": Vacancy.objects.all(),
        })
        return context


class CatVacanciesView(ListView):
    model = Vacancy, Speciality
    template_name = 'appVacancies/vacancies-cat.html'

    def get_queryset(self):
        self.name_query = self.kwargs['category']
        self.query = Vacancy.objects.select_related('speciality').filter(speciality__code=self.name_query)
        get_list_or_404(self.query)
        return self.query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = self.query
        context['category'] = Speciality.objects.get(code=self.name_query).title
        return context


class CatCompanyView(ListView):
    model = Vacancy, Speciality, Company
    template_name = 'appVacancies/company.html'

    def get_queryset(self):
        self.name_query = self.kwargs['category']
        self.query = Vacancy.objects.prefetch_related('company').filter(company__id=self.name_query)
        get_list_or_404(self.query)
        return self.query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = self.query
        context['category'] = Company.objects.get(id=self.name_query)
        return context


class DetailVacancyView(DetailView):
    model = Vacancy, Company
    template_name = 'appVacancies/vacancy.html'

    def get_queryset(self):
        return Vacancy.objects

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.get_queryset().get(id=self.kwargs['pk']).company
        return context


def handler404(request, exception):
    return render(request, 'appVacancies/error404.html', status=404)


def handler500(request, *args, **kwargs):

    return render(request, 'appVacancies/error500.html', status=500)
