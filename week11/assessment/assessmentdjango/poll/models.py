from django.db import models
class Poll(models.Model):
    question=models.CharField(max_length=300)
    option_one=models.CharField(max_length=200)
    option_two=models.CharField(max_length=200)
    one_vote=models.IntegerField(default=0)
    two_vote=models.IntegerField(default=0)
    def __str__(self):
        return self.question