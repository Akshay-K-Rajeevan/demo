from django.urls import path
from. import views

urlpatterns =[
    path('',views.add,name ='add'),
    path('delete/<int:taskid>/',views.delete, name ='delete'),
    path('update/<int:taskid>/',views.update, name ='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name= 'cbvhome'),
    path('cbvd/<int:pk>/',views.TaskDetailView.as_view(),name='cbvd'),
    path('update/<int:pk>/',views.TaskUpdateView.as_view(),name= 'update'),
    path('delete/<int:pk>/',views.TaskDeleteView.as_view(), name='delete')
]