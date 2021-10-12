from django.urls import path

from custom_user_app.views import user_profile_view
urlpatterns = [
    path('profile/<int:user_id>/', user_profile_view, name='user_profile' ), 
]