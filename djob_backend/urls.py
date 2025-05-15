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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/jobs/', include('job.urls')),

    # Redirect root URL to /api/v1/jobs/ or any other path you want
    path('', RedirectView.as_view(url='/api/v1/jobs/', permanent=False)),
]
