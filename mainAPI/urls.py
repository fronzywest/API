from django.urls import include, path
from rest_framework import routers
from . import views

router = router.DefaulthRouter()
router.register('vehicls', views.vehiclviewset)

urlpatters = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

