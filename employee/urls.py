from django.urls import path,include
from .import views

urlpatterns=[
        path("",views.home,name='emp'),
        path('del/int:<id>',views.delete,name="del"),
        path('edit/int:<id>',views.edit,name='edit'),
        path('fil/',views.filterr,name="fil")
        ]