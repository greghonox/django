from django.db import models

class EventMetherologic(models.Model):
    tp_status = (
        ('o', 'observation'), ('a', 'active'), ('e', 'expired'), ('d', 'destroyed')
    )
    position_name = models.CharField(null=True, max_length=200, verbose_name='position name')
    details = models.CharField(null=True, max_length=250, verbose_name='details of event')
    where = models.DateTimeField(null=True, verbose_name='how event', auto_now_add=True)
    position = models.IntegerField(verbose_name='position in graphic', unique=True)
    status = models.CharField(default=tp_status[0][0], max_length=1, 
                    choices=tp_status, verbose_name='status of event')
    
    class Meta:
        db_table='event'
        verbose_name_plural = "event"

    def __str__(self) -> str:
        return '{} {} {} status: {}'.format(self.position_name, self.how, self.position, self.status)