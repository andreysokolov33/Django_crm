from django.contrib import admin
from django.urls import path, include
from info.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('main_info/', include('info.urls', namespace='main_part'))
]
