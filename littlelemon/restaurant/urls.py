from django.contrib import admin 
from rest_framework.routers import DefaultRouter
from django.urls import path, include 
from rest_framework.authtoken.views import obtain_auth_token
from . import views 

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
  
urlpatterns = [ 
    #path('', views.sayHello, name='sayHello'), 
    path('', views.home, name='home'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]