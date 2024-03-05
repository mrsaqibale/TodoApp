"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import tbTodoListView
from base.views import tbTodoDetailView
from base.views import tbTodoCreateView
from base.views import tbTodoUpdateView
from base.views import tbTodoDeleteView
from base.views import DeletedTaskShow
from base.views import completdTaskShow
from base.views import LoginView
from base import views

# from base import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  tbTodoListView.as_view(), name='task'),
    path('detail/<int:pk>/',  tbTodoDetailView.as_view(),name = 'detail'),
    path('create/', tbTodoCreateView.as_view(), name = 'create'), 
    path('update/<int:pk>/',  tbTodoUpdateView.as_view(),name = 'update'),
    path('delete/<int:delId>/',  views.tbTodoDeleteView ,name = 'delete'),
    path('login/',  LoginView.as_view(),name = 'login'),
    path('logout/', views.logouts , name = 'logout'),

    # extra method paths
    path('deleted/',  DeletedTaskShow.as_view(), name='deleted'),
    path('completed/',  completdTaskShow.as_view(), name='completed'),
]
