from django.db import models

# Create your models here.

class Goal(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(blank=True)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=30)

    time_created = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    def reach(self):
        reach = self.step_set.last()
        if reach:
            return reach.amount
        else:
            return 0
    
    def reach_percentage(self):
        return round(self.reach()/self.quantity*100)


    def __str__(self):
        return self.name


class Step(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    amount = models.IntegerField()

    time_created = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

