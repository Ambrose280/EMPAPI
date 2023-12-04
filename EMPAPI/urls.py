# samsung URL Configuration
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from employees import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    
	openapi.Info(
        title='Employee API By Ifiok Ambrose',
        default_version='v1',
        description='This is A RestFul API to get Create, Retrieve, Update, and Delete Employees',
        terms_of_service='https://www.github.com/Ambrose280/employee-rest-api',
        contact=openapi.Contact(email='ifiokambrose@gmail.com'),
        license=openapi.License(name='Test License')
               ),
        
	public=True,
    # permission_classes=(permissions.IsAuthenticated),

)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('admin/', admin.site.urls),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	path('employees/', views.employee_list, name='employee_list'),
    path('accounts/', include('allauth.urls')),
	re_path(r'^employees/(?P<id>[0-9]+)/$', views.employee_detail, name='employee_detail'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
