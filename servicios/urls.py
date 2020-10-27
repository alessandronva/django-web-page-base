from django.urls import path
from . import views #if this path doesn`t work use a point "."
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('services/',views.services, name="Services"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)