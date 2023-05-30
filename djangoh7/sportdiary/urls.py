from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
		path('about', DiaryView.as_view()),
		
		path('', DiaryListView.as_view()),
		path('diary/new', DiaryCreateView.as_view()),
		path('diary/<int:pk>', DiaryUpdateView.as_view()),
		path('diary/<int:pk>/delete', DiaryDeleteView.as_view()),

		path('location/', LocationListView.as_view()),
		path('location/new', LocationCreateView.as_view()),

		path('register', RegisterView.as_view()),
		path('accounts/login/', LoginView.as_view()),
		path('logout/', LogoutView.as_view(next_page="/"))
				
]
