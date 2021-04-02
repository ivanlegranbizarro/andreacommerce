from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('schema', get_schema_view(title='Andrea\'s Ecommerce',
         description='An API for a little shop', version='1.0.0'), name='openapi-schema'),
    path('docs/', include_docs_urls(title='Andrea\'s Ecommerce')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
