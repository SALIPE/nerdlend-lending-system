from django.db import models


class Trigger(models.Model):
    cvid = models.AutoField(primary_key=True)  
    ccmessage = models.TextField()  
    cvscheduleid = models.IntegerField(null=False, blank=False)  
    cdcreatedate = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"TriggerLog {self.cvid} - Message: {self.ccmessage}"
