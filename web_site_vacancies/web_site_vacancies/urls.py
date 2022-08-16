"""web_site_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appVacancies.views import MainPage, AllVacanciesView, CatVacanciesView, CatCompanyView, DetailVacancyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view()),
    path('vacancies/', AllVacanciesView.as_view()),
    path('vacancies/cat/<str:category>/', CatVacanciesView.as_view()),
    path('companies/<int:category>/', CatCompanyView.as_view()),
    path('vacancies/<pk>/', DetailVacancyView.as_view()),

]
