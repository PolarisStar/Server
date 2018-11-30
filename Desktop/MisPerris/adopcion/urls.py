from django.conf.urls import url
from adopcion.views import PerritoList
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('perritos/', PerritoList.as_view(), name='perritolist'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
