from django.contrib import admin
from django.urls import path, include
from info.views import landing_page, LandingPageView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing_page'),
    path('main_info/', include('info.urls', namespace='main_part')),
	 
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)