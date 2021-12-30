
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('portfolio-admin/', admin.site.urls),
    path('',include('main.urls')),
    path('',include('blog.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

