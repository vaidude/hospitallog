"""hospitallog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('update/',views.update,name='update'),
    path('proupdate/',views.proupdate,name='proupdate'),
    path('dlog/',views.dlog,name='dlog'),
    path('dreg/',views.dreg,name='dreg'),
    path('profiled/',views.profiled,name='profiled'),
    path('listdr/',views.listdr,name='listdr'),
    path('booking/',views.booking,name='booking'),
    path('book/',views.book,name='book'),
    path('listuser/',views.listuser,name='listuser'),
    path('alog/',views.alog,name='alog'),
    path('lablog/',views.lablog,name='lablog'),
    path('alistusers/',views.alistusers,name='alistusers'),
    path('alistdoctors/',views.alistdoctors,name='alistdoctors'),
    path('alistlab/',views.alistlab,name='alistlab'),
    path('ed/<int:id>/',views.ed,name='ed'),
    path('update/',views.update,name='update'),
    path('mybookings/',views.mybookings,name='mybookings'),
    path('ad/',views.ad,name='ad'),
    path('adupdate/',views.adupdate,name='adupdate'),
    path('labservices/',views.labservices,name='labservices'),
    path('labselect/',views.labselect,name='labselect'),
    path('payment/',views.payment,name='payment'),
    path('lablistusers/',views.lablistusers,name='lablistusers'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('booklab/',views.booklab,name='booklab'),
    path('bookinglab/',views.bookinglab,name='bookinglab'),
    path('labbook/',views.labbook,name='labbook'),
    path('payment1/',views.payment1,name='payment1'),
    path('paymenthandler1/', views.paymenthandler1, name='paymenthandler1'),
    path('upload/',views.upload,name='upload'),
    path('uploadresult/',views.uploadresult,name='uploadresult'),
    path('labresult/',views.labresult,name='labresult'),
    path('resultview/',views.resultview,name='resultview'),
    path('listpatients/',views.listpatients,name='listpatients'),
    path('uploadpriscription/',views.uploadpriscription,name='uploadpriscription'),
    path('uploadp/',views.uploadp,name='uploadp'),
    path('priscription/',views.priscription,name='priscription'),
    path('prisview/<int:id>',views.prisview,name='prisview'),
    path('initiate-video-call/<int:appointment_id>/', views.initiate_video_call, name='initiate_video_call'),
    path('video-call/', views.video_call, name='video_call'),
    path("chatbot/", views.chatbot, name="chatbot"),
    path("chatbot/api/", views.chatbot_api, name="chatbot_api"),
    path('chats/', views.chat_list, name='chat_list'),
    path('chat/<str:user_type>/<str:user_email>/', views.chat_detail, name='chat_detail')
]
