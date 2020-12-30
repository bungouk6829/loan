from django.db import models

class Information_post(models.Model):
    password = models.CharField(max_length=20, verbose_name='비밀번호')
    name = models.CharField(max_length=10, verbose_name='이름')
    age = models.IntegerField(verbose_name='나이')
    money = models.IntegerField(verbose_name='희망금액')
    product = models.CharField(max_length=20, verbose_name='상품')
    job = models.CharField(max_length=20, verbose_name='직업')
    title = models.CharField(blank=True, null=True, default='',max_length=500, verbose_name='글제목')
    text = models.TextField(blank=True, null=True, default='', max_length=5000, verbose_name='글내용')
    phone_number = models.CharField(max_length=20, verbose_name='전화번호')
    region_1 = models.CharField(max_length=20, verbose_name='시/도')
    region_2 = models.CharField(max_length=20, verbose_name='구/군')
    create_at = models.DateField(auto_now_add=True, verbose_name='날짜')
    clicks = models.IntegerField(default=1, verbose_name='조회수')

    @property
    def update_clicks(self):
        self.clicks += 1
        self.save()

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'information_postss'
        verbose_name = '문의글'
        verbose_name_plural = '문의글'
