from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),           # Home page (index.html)
    path('sell/', views.sell, name='sell'),        # Sell Books page (sell.html)
    path('buy/', views.buy, name='buy'),           # Buy Books page (buy.html)
    path('profile/', views.profile, name='profile'), # Profile page (profile.html)
    path('login/', views.login, name='login'),     # Login page (login.html)
]
