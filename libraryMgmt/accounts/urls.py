from django.urls import path
from .views import register, login_user, admin_dashboard,logout_user,user_dashboard,manage_users,edit_user,delete_user
from . import views

urlpatterns = [
    path('', register, name='accounts_home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('logout/', logout_user, name='logout'),
    path('manage-users/', manage_users, name ='manage_users'),
    path('edit-user/<int:user_id>/', edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/',delete_user, name='delete_user'),

]
