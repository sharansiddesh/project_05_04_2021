from django.urls import path
from app2 import views
app_name="app2"

urlpatterns = [
    path('page1/',views.page1,name='page1'),
    path('page2/',views.page2,name='page2'),
    
]
