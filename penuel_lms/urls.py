from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        '',
        include('accounts.urls')
    ),
    path(
        'students/',
        include('students.urls')
    ),
    path(
        'lecturers/',
        include('lecturers.urls')
    ),
    path(
        'subjects/',
        include('subjects.urls')
    ),
    path(
        'results/',
        include('results.urls')
    ),
]
