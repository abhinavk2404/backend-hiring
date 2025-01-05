from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Site
from .serializers import SiteSerializer
import redis
import json

redis_conn = redis.StrictRedis(host='localhost', port=6379, db=0)

class SubmitJobView(APIView):
    """
    API to submit a job to the Redis job queue.
    """
    def post(self, request):
        try:
            data = request.data
            site_id = data.get('site_id')
            job_type = data.get('job_type')

            if not site_id or not job_type:
                return Response(
                    {"error": "Both 'site_id' and 'job_type' are required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            redis_conn.rpush('job_queue', json.dumps({
                'site_id': site_id,
                'job_type': job_type
            }))

            return Response({"message": "Job submitted successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ListSitesView(APIView):
    """
    API to list all sites.
    """
    def get(self, request):
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class JobQueueStatusView(APIView):
    """
    API to check the status of the job queue.
    """
    def get(self, request):
        try:
            queue = redis_conn.lrange('job_queue', 0, -1)
            jobs = [json.loads(job) for job in queue]
            return Response(jobs, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
