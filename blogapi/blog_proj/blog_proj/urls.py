
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.documentation import include_docs_urls 
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from posts.permissions import IsAuthorOrReadOnly

API_TITLE = 'iNES aPI'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'

'''
    A schema is a machine-readable document that outlines all available API endpoints,
URLs, and the HTTP verbs (GET, POST, PUT, DELETE, etc.) they support. Documentation is
something added to a schema that makes it easier for humans to read and consume.
'''
# schema_view = get_schema_view(title = API_TITLE)# using old schema

# swagger
# schema_view = get_swagger_view(title = API_TITLE) 
schema_view = get_schema_view(
    openapi.Info(
    title = API_TITLE,
    default_version = 'v1',
    description = API_DESCRIPTION,
    terms_of_service = "https://www.karimikiura.com/policies/terms",
    contact = openapi.Contact(email='contact@kk.com'),
    license = openapi.License(name='BSD License'),
),
public = True,
permission_classes = (IsAuthorOrReadOnly,)
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/register', include('rest_auth.registration.urls')),
    
    path('docs/', include_docs_urls(title = API_TITLE, description=API_DESCRIPTION)),
    # path('schema/', schema_view),
    path('swagger/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
