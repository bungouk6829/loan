from django.db import models

class Information_post(models.Model):

    password = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    product = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=5000)
    phone_number = models.CharField(max_length=20)
    create_at = models.DateField(auto_now_add=True)
    clicks = models.IntegerField(default=1)
    file_1 = models.FileField(upload_to='files/', null=True, blank=True)
    file_2 = models.FileField(upload_to='files/', null=True, blank=True)
    file_3 = models.FileField(upload_to='files/', null=True, blank=True)
    file_4 = models.FileField(upload_to='files/', null=True, blank=True)
    file_5 = models.FileField(upload_to='files/', null=True, blank=True)

    @property
    def update_clicks(self):
        self.clicks += 1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'information_posts'
