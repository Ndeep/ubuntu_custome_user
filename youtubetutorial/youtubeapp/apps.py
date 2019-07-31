from django.apps import AppConfig
from django.core.signals import request_started
from youtubeapp.views import log_request
class YoutubeappConfig(AppConfig):
    name = 'youtubeapp'

    def ready(self):
        request_started.connect(log_request())
