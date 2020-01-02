from django.urls import path
from .views import homepage, new_post, reply, delete, edit, approve

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', homepage, name='homepage'),
    path('new/', new_post, name='new_post'),
    path('reply/<int:id>', reply, name='reply'),
    path('delete/<int:id>', delete, name='delete'),
    path('delete_reply/<int:id>', delete, name='delete_reply'),
    path('edit/<int:id>', edit, name='edit'),
    path('approve/', approve, name='approve'),
    #path('approveReply/', approveReply, name='approveReply')
    ]