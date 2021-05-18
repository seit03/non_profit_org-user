from django.urls import path

from npo_law import views

urlpatterns = [
    path('api/v1/law/', views.NPOUserAPIView.as_view()),
    path('api/v1/law/<int:id>/', views.NPOUserDetailAPIView.as_view()),
]