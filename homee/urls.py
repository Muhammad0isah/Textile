from django.urls import path
from . import views
urlpatterns = [
	path('home/', views.Home, name = "home"),
	path('form/', views.create, name = "form"),
	path('menu/', views.Menu, name = "menu"),
	path('contact/', views.Contact, name = "contact"),
	path('faq/', views.Faq, name = "faq"),
	path('update/', views.Update, name = "change"),
	path('catalogue/', views.Catalogue, name = "catalogue"),
	path('list/', views.List, name = "list"),
	
]