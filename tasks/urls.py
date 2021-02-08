from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>',views.taskList, name='task-list'),
    path('sendemail', views.sendEmail, name='send-email'),
    path('view/<int:id>',views.taskView,name="task-view"),
    path('view/deleteFile/<int:id>',views.deleteFile,name = "delete-file"),
    path('edit/<int:id>',views.editTask,name="edit-task"),
    path('changestatus/<int:id>',views.changeStatus,name="change-status"),
    path('delete/<int:id>',views.deleteTask, name="delete-task"),
    path('view/deleteComment/<int:id>', views.deleteComment, name = "delete-comment")
]