


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import user_counts
from .views import  CourseViewSet,UserSignupView, custom_admin_dashboard

router = DefaultRouter()

#Same pattern as teacher
router.register(r'courses', CourseViewSet, basename='course')
#Same as pattern as teacher.



urlpatterns = [
    path('', include(router.urls)),
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('get-user-counts/', user_counts, name='user-counts'),

  path("admin/", custom_admin_dashboard, name="custom-admin")

]
