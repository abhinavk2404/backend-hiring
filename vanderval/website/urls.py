from django.urls import path
from .views import SubmitJobView, ListSitesView, JobQueueStatusView

urlpatterns = [
    path('submit-job/', SubmitJobView.as_view(), name='submit_job'),
    path('list-sites/', ListSitesView.as_view(), name='list_sites'),
    path('job-queue-status/', JobQueueStatusView.as_view(), name='job_queue_status'),
]
