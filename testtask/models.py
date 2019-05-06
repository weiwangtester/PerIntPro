from django.db import models

# Create your models here.


class Tasksummary(models.Model):
	taskid = models.AutoField(primary_key=True)
	userid = models.IntegerField()
	taskname = models.CharField(max_length=60)
	taskcreatedate = models.DateTimeField(auto_now_add=True)
	taskeditdate = models.DateTimeField(auto_now=True)
	taskdetails = models.TextField()


class Testresult(models.Model):
	resultid = models.AutoField(primary_key=True)
	taskid = models.ForeignKey(Tasksummary, on_delete=models.CASCADE)
	teststarttime = models.DateTimeField()
	testendtime = models.DateTimeField()
	testtime = models.CharField(max_length=20)
	testusernum = models.IntegerField()
	testusersec = models.IntegerField()

