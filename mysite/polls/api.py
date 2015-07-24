from rest_framework import  serializers, viewsets
from .models import Question, Choise


class ChoiseSerializer(serializers.ModelSerializer):
	class Meta:
		model=Choise 


class QuestionSerializer(serializers.ModelSerializer):
	choises=ChoiseSerializer(many=True,read_only=True)
	class Meta:
		model=Question
		fields=('url','id','pub_date','question_text','choises')


class QuestionViewSet(viewsets.ModelViewSet):
	queryset=Question.objects.all()
	serializer_class=QuestionSerializer


class ChoiseViewSet(viewsets.ModelViewSet):
	queryset=Choise.objects.all()
	serializer_class=ChoiseSerializer
