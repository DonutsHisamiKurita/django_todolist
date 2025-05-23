from django.contrib import admin
from django.urls import path
from app.views import todo_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('', todo_list, name='home'),
]