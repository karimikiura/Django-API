# Django-API
Service Oriented Architecture (SOA) Implementation -  RESTful web APIs using Django &amp; Django REST Framework

# APP 1 - TODO APP
## Backend
Developed in Django REST Framework

## Frontend
Developed using React Framework

# APP 2 - Library APP
Will add desc..
# APP 3 - Blog API 
A browsable web API for creating, editing and deleting blogs.\
Developed using Django REST.

# Awesome Implementation
Following functionality are implemtned on this app.
## 1. Permissions
To secure our API, we use some out-of-the-box permissions settings provided by Django REST. They can be applied at `project-level` or `view-level` or even at `model-level`.\
SYNTAX
```python
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
         ]
        }
```
1. View Level Permissions
Restricts API access to authenticated users only.\
`from rest_framework import generics, permissions`
```python
    class ProductList(generics.ListCreateAPIView):
        permission_classes = (permissions.IsAuthenticated,)
        ...
```
`HTTP 403 Forbidden` status code is returned when you try access the product page without being logged in. Only logged in user can view the API.\

2. Project-Level Permissions
Built in project level permissions include:
- `AllowAny` - any user, authenticated or not, has full access
- `IsAuthenticated` - only authenticated, registered users have access
- `IsAdminUser` - only admins/superusers have access
- `IsAuthenticatedOrReadOnly` - unauthorized users can view any page, but only          authenticated users have write, edit, or delete privileges

## Custom permissions
Internally, Django REST Framework relies on a  `BasePermission` class from which all
other permission classes inherit.
- create a `permisions.py` file in your app.\
SYNTAX
```python
    class BasePermission(object):
        """
        A base class from which all permission classes should inherit.
        """
        def has_permission(self, request, view):
            #Return `True` if permission is granted, `False` otherwise.
            return True
        def has_object_permission(self, request, view, obj):
            #Return `True` if permission is granted, `False` otherwise.
            return True
```


## 2. User Authentication
Authentication which is the process by which a user can register for a new account, log in with it, and log out.\
`HTTP` is a `stateless protocol` -  there is no built-in way to remember if a user is authenticated from one request to the next. Each time a user requests a restricted resource it must verify itself.
#### Django REST Authentication Protocols 
1. Basic Authentication\
When a client makes an HTTP request, it is forced to send an approved authentication
credential before access is granted.\
The complete request/response flow looks like this:\
a. Client makes an HTTP request\
b. Server responds with an HTTP response containing a  `401 (Unauthorized)` status code and `WWW-Authenticate HTTP` header with details on how to authorize\
c. Client sends credentials back via the Authorization HTTP header\
d. Server checks credentials and responds with either `200 OK or 403 Forbidden` status
code

2. Session Authentication\
At a high level, the client authenticates with its credentials (username/password) and then receives a session ID from the server which is stored as a cookie. This session ID is then passed in the header of every future HTTP request.\
Basic flow:\
a. A user enters their log in credentials (typically username/password)\
b. The server verifies the credentials are correct and generates a session object that
is then stored in the database\
c. The server sends the client a session ID—not the session object itself—which is
stored as a cookie on the browser\
d. On all future requests the session ID is included as an HTTP header and, if verified
by the database, the request proceeds\
e. Once a user logs out of an application, the session ID is destroyed by both the
client and server\
f. If the user later logs in again, a new session ID is generated and stored as a cookie
on the client

*Django REST Framework is actually a combination of Basic Authentication and Session Authentication.*

3. Token Authentication\
Token-based authentication is  `stateless`: once a client sends the initial user credentials to the server, a unique token is generated and then stored by the client as either a  `cookie` or in `local storage`.
> __Cookies vs localStorage__\
Cookies are used for reading server-side information. They are smaller _(4KB)_ in
size and automatically sent with each HTTP request. LocalStorage is designed for
client-side information. It is much larger _(5120KB)_ and its contents are not sent by
default with each HTTP request. Tokens stored in both cookies and localStorage are
vulnerable to XSS attacks. The current best practice is to store tokens in a cookie with
the httpOnly and Secure cookie flags.

4. Default Authentication\
SYNTAX\
```javascript
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': [ # new
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication'
        ],
    }
```
> Note\
`Sessions` are used to power the Browsable API and the ability to log in and log out of it.\
`BasicAuthentication` is used to pass the session ID in the HTTP headers for the API
itself.

## 3. Viewsets and Routers
Are additional layer of abstraction on top of views and URLs to speed up API development.\
The primary benefit is that a single viewset can replace multiple related views. And
a router can automatically generate URLs for the developer.

```python
|Endpoint                              |HTTP Verb|
|--------------------------------------|---------|
|/                                     |GET      |
|/:pk/                                 |GET      |
|/rest-auth/registration               |POST     |
|/rest-auth/login                      |POST     |
|/rest-auth/logout                     |GET      |
|/rest-auth/password/reset             |POST     |
|/rest-auth/password/reset/confirm     |POST     |
```

##### Viewsets
A viewset is a way to combine the logic for multiple related views into a single class.\
`from rest_framework import viewsets`
SYNTAX\
```python
    class UserViewSet(viewsets.ModelViewSet):
        queryset = get_user_model().objects.all()
        serializer_class = UserSerializer
```

##### Routers
Routers work directly with viewsets to automatically generate URL patterns.\
REST Default Routers:
- SimpleRouter
- DefaultRouter

SYNTAX
```python
_urls.py_
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, ProductViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', ProductViewSet, basename='products')

urlpatterns = router.urls
```
## Schemas and Documentation
A schema is a machine-readable document that outlines all available API endpoints,
URLs, and the HTTP verbs (GET, POST, PUT, DELETE, etc.) they support.\
Documentation is something added to a schema that makes it easier for humans to read and consume.

### Schemas
`127.0.0.1:8000/schema/`

```python
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Prod API') 
urlpatterns = [
    path('schema/', schema_view),
]

```

### Documentation
`127.0.0.1:8000/docs/`\
Django REST Framework also comes with a built-in API documentation feature that translates schema into a much friendlier format for fellow developers.\
```python
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path('docs/', include_docs_urls(title='Blog API')),
]
```

### 1. Django REST Swagger
`http://127.0.0.1:8000/swagger`\
current best-practice approach for documenting a RESTful API.
```python
pip install -U drf-yasg
INSTALLED_APPS = [
   ...
   'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
   'drf_yasg',
   ...
]
```
`urls.py`
```javascript
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
    ...
    path('swagger/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

# USAGE
`127.0.0.1:8000/api/v1/`
### Register 
`127.0.0.1:8000/api/v1/rest-auth/register/`
### Confirm Pass 
`127.0.0.1:8000/api/v1/rest-auth/password/reset/confirm`

### Login 
`127.0.0.1:8000/api/v1/rest-auth/login/`

### Logout 
`127.0.0.1:8000/api/v1/rest-auth/logout`
### Rester Pass 
`127.0.0.1:8000/api/v1/rest-auth/password/reset`

### Get all products 
`127.0.0.1:8000/api/v1/`

### A single product 
`127.0.0.1:8000/api/v1/1`

### View Schema 
`127.0.0.1:8000/schema/`

### View documentation 
`http://127.0.0.1:8000/swagger`
