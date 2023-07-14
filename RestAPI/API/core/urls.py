from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.endpoint,name="home"),
    path('advocates/',views.advocates_list,name = "al"),
    path('advocates/<str:username>',views.AdvocatesDetails.as_view(),name="ad"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]