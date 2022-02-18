from django.db import models

# Create your models here.


class User(models.Model):
    # user = models.CharField(max_length=40,null=True)
    # id=models.AutoField(primary_key=True)
    # user=models.TextField()


class Cars(models.Model):
    pass


class Appointments(models.Model):
    pass


class Feedback(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=40,null=True)
    feedback = models.TextField()
    def _str_(self):
        return self.feedback



