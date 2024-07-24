from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home,name="home"),
    path('order',views.order,name="order"),
    path('contac',views.contact,name="contac"),
    path('checkout',views.checkout,name="checkout"),
    path('feedback',views.feedback,name="feedback"),
    path('login',views.loginpage,name="login"),
    path('logout',views.logoutpage,name="logout"),
    path('signup',views.signuppage,name="signup"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('booking',views.booking,name="booking"),
    path('blog',views.Blog,name="blog"),
    path('post/<int:blog_id>/', views.post_detail, name='post_detail'),
]