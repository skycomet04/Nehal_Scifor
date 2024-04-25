from django.db import models

class Emailsender(models.Model):
    name=models.CharField(max_length=220)
    email=models.CharField(max_length=300)
    ques=models.TextField(null=True)
    date=models.DateField(null=True)

class StockData(models.Model):
    stock_sym=models.CharField(max_length=50)
    stockprice=models.FloatField()
    def __str__(self):
        return str(self.stock_sym)