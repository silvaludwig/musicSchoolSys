from django.urls import include, path
from rest_framework.routers import DefaultRouter
from students.views import StudentViewSet
from teachers.views import TeacherViewSet
from scheduling.views import SchedulingViewSet

router = DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"teatchers", TeacherViewSet)
router.register(r"scheduling", SchedulingViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
