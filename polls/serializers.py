from rest_framework import serializers

from .models import Question, Choice

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "question_text", "pub_date")