from django.db import models


class TradeCode(models.Model):
    trade_code = models.CharField(max_length=250)


class Trade(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=250)
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date) + " " + self.trade_code

    class Meta:
        get_latest_by = ["created"]

    def save(self, *args, **kwargs):
        try:
            obj = TradeCode.objects.get(trade_code=self.trade_code)
        except TradeCode.DoesNotExist:
            TradeCode.objects.create(trade_code=self.trade_code)
        super().save(*args, **kwargs)
