from django.urls import path
from . import views

urlpatterns = [
    path('get-all-entries', views.get_all_entries),
    path('new-entry', views.new_entry),
    path('delete-entry', views.delete_entry),

]
