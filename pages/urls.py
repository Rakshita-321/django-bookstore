from django.urls import path

from . import views


app_name = 'pages'
urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]
