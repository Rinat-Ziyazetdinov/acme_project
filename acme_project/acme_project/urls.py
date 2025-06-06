# Импортируем настройки проекта.
from django.conf import settings
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static

from django.contrib import admin
# К импортам из django.urls добавьте импорт функции reverse_lazy
from django.urls import include, path, reverse_lazy

# Добавьте новые строчки с импортами классов.
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from users.forms import CustomUserCreationForm  # Импортируем свою форму

handler404 = 'core.views.page_not_found' 

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    # Подключаем urls.py приложения для работы с пользователями.
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,  # Используем свою форму
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
    # В конце добавляем к списку вызов функции static.
]

# Подключаем дебаг-панель:
if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов 
    # из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
