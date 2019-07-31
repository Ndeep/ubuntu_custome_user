from rest_framework import serializers
from youtubeapp.models import Question
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=('title','status','user')
