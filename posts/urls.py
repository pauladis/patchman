from django.urls import path
from .views import homepageView, new_postView, replyView, deleteView, delete_replyView, editView, approveView


urlpatterns = [
    path('', homepageView.as_view(), name='homepage'),
    path('new/', new_postView.as_view(), name='new_post'),
    path('reply/<int:id>', replyView.as_view(), name='reply'),
    path('delete/<int:id>', deleteView.as_view(), name='delete'),
    path('delete_reply/<int:id>', delete_replyView.as_view(), name='delete_reply'),
    path('edit/<int:id>', editView.as_view(), name='edit'),
    path('approve/', approveView.as_view(), name='approve'),
    ]