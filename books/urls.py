from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BookListView.as_view(), name='list'),
    path('<uuid:pk>', views.BookDetailView.as_view(), name='detail'),
    path('search/', views.SearchResultsListView.as_view(), name='search_results'),
]