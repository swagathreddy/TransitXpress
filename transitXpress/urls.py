from . import views
from django.urls import path
from django.conf import settings

from django.conf.urls.static import static
# from .views import booking_view
urlpatterns = [
    path('', views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('',views.style),
     path('logout',views.logout,name="logout"),
    path('search',views.DestinationDetails,name="search"),
    path('tickets/', views.tickets_view, name='tickets'),
    path('routes/', views.routes,name='routes'),
    path('conformation/',views.conformation,name="conformation")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)