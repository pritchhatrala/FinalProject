from django.contrib import admin
from django.urls import path, include
from adminapp import views


urlpatterns = [
    path("", views.admin_index),
    path("admin_home/", views.admin_home, name="admin_home"),
    path("admin_userinfo/", views.admin_userinfo, name="admin_userinfo"),
    path("admin_notesinfo/", views.admin_notesinfo, name="admin_notesinfo"),
    path("notes_approve/<int:id>", views.notes_approve, name="notes_approve"),
    path("notes_reject/<int:id>", views.notes_reject, name="notes_reject"),
]