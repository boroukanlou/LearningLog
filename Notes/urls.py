from django.urls import URLPattern, path

from . import views

app_name = 'Notes'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('topics', views.topics, name='topics'), 
    path('topics/<topicId>/', views.topic, name='topic'),
    path('new_topic', views.new_topic, name='new_topic'),
    path('new_entry/<topicId>', views.new_entry, name='new_entry'), 
    path('edit_entry/<entryId>', views.edit_entry, name='edit_entry')
]