from django.urls import path
from bukapp import views 
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('search/', views.book_search, name='book_search'),
    path('buy_books/', views.buy_books, name='buy_books'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]
    
