from django.urls import path, include
from rest_framework import routers
from . views import Test1view

router = routers.DefaultRouter()
router.register('',Test1view)

urlpatterns =[
    path ('test/',include(router.urls)),
]