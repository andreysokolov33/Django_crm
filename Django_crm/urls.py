from django.contrib import admin
from django.urls import path, include
from info.views import landing_page, LandingPageCiew

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageCiew.as_view(), name='landing_page'),
    path('main_info/', include('info.urls', namespace='main_part'))
]
