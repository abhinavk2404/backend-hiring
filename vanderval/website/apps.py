from django.apps import AppConfig
import threading


class WebsiteConfig(AppConfig):
    name = "website"
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from .tasks import worker_function
        print("Before Threading starts")
        thread = threading.Thread(target=worker_function, daemon=True)
        thread.start()
        print(f"Worker thread started: {thread.is_alive()}")
