from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from travel.views import *
from travel.yasg import urlpatterns as doc_urls

#urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/countrylist/', CountryApiView.as_view()),
#     path('api/v1/countrylist/<int:pk>/', CountryUpdateView.as_view()),
#     path('api/v1/countrydetail/<int:pk>/', CountryDetailView.as_view()),

#     path('api/v1/countrylist/', CountryViewSet.as_view({'get': 'list'})),
#     path('api/v1/countrylist/<int:pk>/', CountryViewSet.as_view({'put': 'update'}))
# ]

#router = routers.SimpleRouter()
#router.register(r'country', CountryViewSet)

router = routers.DefaultRouter()
router.register(r'country',CountryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
#   path('api/v1/drf-auth/', include('rest_framework.urls')), # session-based auth

#   path('api/v1/auth/', include('djoser.urls')), # token authentication djoser
#   re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # token authentication JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
#   path('o/', include(oauth2_urls)), # OAuth - toolkit
#   re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='social'))
]
urlpatterns += doc_urls
