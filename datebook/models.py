from django.db import models
from django.utils import timezone

class Move(models.Model):
    author = models.ForeignKey('auth.User')
    move_date = models.DateField(verbose_name="MOVE DATE")
    company = models.CharField(max_length=2, verbose_name="COM", blank=True)
    type = models.CharField(max_length=10, verbose_name="TYPE", blank=True)
    pk_ld_del = models.CharField(max_length=10, verbose_name="PK/LD/DEL", blank=True)
    weight_rooms = models.CharField(max_length=6, verbose_name="WT/RM")
    men = models.CharField(max_length=4, verbose_name="MEN", blank=True)
    customer = models.CharField(max_length=20, verbose_name="CUSTOMER")
    origin = models.CharField(max_length=15, verbose_name="ORIGIN")
    destination = models.CharField(max_length=15, verbose_name="DESTINATION")
    remarks = models.CharField(max_length=15, verbose_name="REMARKS", blank=True)
    details = models.TextField(verbose_name="", blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    cancelled_date = models.DateTimeField(
        blank=True, null=True)

    def cancel(self):
        self.cancelled_date = timezone.now()
        self.save()

    def __str__(self):
        customer = self.customer.replace(' ', '')
        customer = customer.replace(',', '_')
        return customer + '_' + self.move_date.strftime("%m:%d:%y")

