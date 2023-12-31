from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    parsed_data = models.JSONField(null=True, blank=True)

class Result(models.Model):
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    result_text = models.TextField()
    topProd = models.TextField()
    monthly_revenue = models.TextField()
    graph = models.TextField()

class Statsprj(models.Model):
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    result_text = models.TextField()
    topProd = models.TextField()
    monthly_revenue = models.TextField()
    graph = models.TextField()