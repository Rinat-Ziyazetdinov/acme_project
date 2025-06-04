from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    #path('', views.birthday, name='create'),  # было до CBV шаблонов
    path('', views.BirthdayCreateView.as_view(), name='create'),
    #path('list/', views.birthday_list, name='list'), # было до CBV шаблонов
    path('list/', views.BirthdayListView.as_view(), name='list'),
    path('<int:pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    #path('<int:pk>/edit/', views.birthday, name='edit'), # было до CBV шаблонов
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    #path('<int:pk>/delete/', views.delete_birthday, name='delete'), # было до CBV шаблонов
    path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete')
]
