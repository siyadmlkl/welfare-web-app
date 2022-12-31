from django.db import models


class transaction(models.Model):
    type = models.CharField(max_length=100,null="False",blank="False")
    particulars=models.TextField(max_length=256,null="False",blank="False")
    addBy=models.CharField(max_length=100,null="False")
    transDate=models.DateTimeField(null="False")
    amount=models.FloatField(null="False",blank="False")
    image_file = models.FileField(
        null='True', blank='True', upload_to="")


