from django.urls import path
from .views import home
from .views import about
from .views import ShopNow
from .views import shopNowsub
from .views import Anniversary
from .views import loveNromance
from .views import feed1
from .views import login



urlpatterns=[
                path('',home,name='home'),
                path('about/',about,name='about'),
                path('shopNow/',ShopNow,name='ShopNow'),
                path('shopNowsub/',shopNowsub,name='shopNowsub'),
                path('Anniversary/',Anniversary,name='Anniversary'),
                path('loveNromance/',loveNromance,name='loveNromance'),
                path('feed1/',feed1,name='feed1'),
                path('login/',login,name='login'),
]
