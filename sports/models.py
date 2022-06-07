from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils import module_loading


class sports(models.Model):
    sport_name = models.CharField(max_length=20)
    def __str__(self):
        return  f"{self.id}: {self.sport_name}"

class player(models.Model):      
    player_name = models.CharField(max_length=20) 
    age = models.IntegerField()
    #sports_choosen = models.ManyToManyField(sports_name,on_delete=models.CASCADE)
    #sports_choosen = models.ForeignKey(sports_name, on_delete=models.CASCADE)
    def __str__(self):  
        return f"{self.id}: {self.player_name} {self.age} "
    #class Meta:
    #    ordering = ['player_name']


class teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    age = models.IntegerField()
    #teacher_students = models.ManyToManyField(sports_name,on_delete=models.CASCADE)
    #teacher_students = models.ForeignKey(player, on_delete=models.CASCADE)  
    def __str__(self):
        return f"{self.id}:{self.teacher_name} {self.age}"
    #class Meta:
    #    ordering = ['teacher_name']

class player_sport(models.Model):
    player_id = models.ForeignKey(player, on_delete= models.CASCADE)
    sport = models.ManyToManyField(sports,blank=True)
     
    def __str__(self):
        return f"{self.id}:{self.player_id}"

class teacher_sport(models.Model):
    teacher_id = models.ForeignKey(teacher, on_delete= models.CASCADE)
    sport = models.ManyToManyField(sports,blank=True)
     
    def __str__(self):
        return f"{self.id}:{self.teacher_id}"






