from django.contrib import admin
from django.urls import path
from .views import blog, index, new_post, posting, remove_post
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('blog/<int:pk>/', posting),
    path('blog/new_posting/', new_post),
    path('blog/<int:pk>/remove_post/', remove_post)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)