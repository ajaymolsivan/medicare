from django.urls import path
from .import views
app_name='feedback'
urlpatterns=[

    path('login',views.login,name='login'),
path('feedback',views.feedback,name='feedback'),
path('aboutus',views.aboutus,name='aboutus'),
path('contact',views.contact,name='contact'),
]