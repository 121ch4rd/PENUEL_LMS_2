from django.urls import path
from . import views

urlpatterns = [

    path(
        'upload/',
        views.upload_result,
        name='upload_result'
    ),

    path(
        'student/',
        views.student_results,
        name='student_results'
    ),
    path(
    'pdf/',
    views.download_result_pdf,
    name='download_result_pdf'
    )
]
