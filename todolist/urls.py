from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet

router = DefaultRouter()

app_name = "todolistapp"

router.register(
    prefix="tasks",
    viewset=ToDoViewSet,
    basename="tasks",
)

urlpatterns = router.urls
