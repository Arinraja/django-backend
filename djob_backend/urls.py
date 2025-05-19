# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include('djoser.urls')),
#     path('api/v1/', include('djoser.urls.authtoken')),
#     path('api/v1/jobs/', include('job.urls')),
# ]


from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/jobs/', include('job.urls')),
    
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Redirect root URL to /api/v1/jobs/ or any other path you want
    path('', RedirectView.as_view(url='/api/v1/jobs/', permanent=False)),
]
