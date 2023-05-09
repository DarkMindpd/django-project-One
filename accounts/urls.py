from django.urls import path
from accounts import views
from django.views.generic import TemplateView

urlpatterns = [
    path('account', views.enter_acc, name='enter_acc'),
    path('register_successful', TemplateView.as_view(template_name = 'accounts\index_success.html'), name='successful_singup'),
    path('Logout_successful', views.log_out, name='successful_logout'),
    path('<str:username>/profile', views.profile_detail, name='profile_detail'),
    path('followToggle/<str:author>', views.followToggle, name='followToggle')

]

