from rest_framework import serializers
from . models import sports,player,teacher,player_sport,teacher_sport

# Name the class as (model name + 'Serializer')
class sportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = sports
        fields = '__all__'


class playerSerializer(serializers.ModelSerializer):
    class Meta:  
        model = player  
        fields = '__all__'
        
class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = '__all__'

class player_sportSerializer(serializers.ModelSerializer):
    class Meta:
        model = player_sport
        fields = '__all__'

class teacher_sportSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher_sport
        fields = '__all__'
