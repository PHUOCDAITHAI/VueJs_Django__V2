from django.urls import path

from rest_framework import routers

from .views import *

# from .views import index

router = routers.DefaultRouter()
router.register('students', StudentsViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('students/', index)
# ]