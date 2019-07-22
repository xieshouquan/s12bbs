from django.urls import re_path

from webchat import views
urlpatterns = [
    # url(r'^$/', views.acc_login,name='login' ), 这种写法错误,r'^$/'要改成r'^$'
    re_path(r'^$', views.dashboard,name='chat_dashboard' ),
    re_path(r'^msg_send/$',views.send_msg,name='send_msg' ),
    re_path(r'^new_msgs/$',views.get_new_msgs,name='get_new_msgs' ),
    re_path(r'^file_upload/$',views.file_upload,name='file_uploads' ),
]
