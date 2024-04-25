from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static



urlpatterns = [
    path('', views.bug_report_home, name='bug_report_home'),
    path('create_report', views.create_report, name='create_report'),
    path('bug_report_home/<int:pk_bug_report>', views.one_bug_report, name='one_bug_report'),
    path('bug_report/<int:pk_bug_report>/download/', views.download_log_file, name='download_log_file'),
    path('bug_report/<int:pk_bug_report>/update_status/', views.update_bug_status, name='update_bug_status'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)