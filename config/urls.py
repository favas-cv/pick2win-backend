from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Your APIs
    path('api/tournaments/', include('tournaments.urls')),
    path('api/matches/', include('matches.urls')),
    path('api/clubs/',include('clubs.urls')),
    path('api/predictions/',include('predictions.urls')),
    path('api/auth/',include('accounts.urls')),
    path('api/admin/',include('admindashboard.urls')),
    path('api/leaderboard/',include('leaderboard.urls')),
    path('api/club-admin/',include('clubadmindashboard.urls')),

    # OpenAPI Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),

    # ReDoc Documentation
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]