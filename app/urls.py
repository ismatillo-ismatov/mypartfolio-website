from django.urls import path
from .views import home,posts,post,sendEmail,registerPage,loginPage,logoutUser,userAccount,profile,updateProfile

app_name = 'app'


urlpatterns = [
    path('',home,name='home'),
    path('posts',posts,name='posts'),
    path('post/<str:slug>/',post, name="post"),
    # user register urls
    path('register/',registerPage,name='register'),
    path('login/',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('user-accounts',userAccount,name='user-account'),
    path('profile',profile,name='profile'),
    path('update_profile',updateProfile,name='update_profile'),
    path('send_email/',sendEmail,name='send-email')




]
