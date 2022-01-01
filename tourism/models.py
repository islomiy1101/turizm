from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
class Customer(models.Model):
    gender_type=(
        ('male','Male'),('female','Female')
    )
    result_type=(
        ('negative', 'Negative'), ('positive', 'Positive')
    )
    custom_id=models.CharField(max_length=250,blank=True)
    fullName=models.CharField(max_length=250)
    passport=models.CharField(max_length=50)
    birthDate=models.DateTimeField(null=True)
    gender=models.CharField(choices=gender_type,max_length=50)
    analysis_date = models.DateTimeField(null=True)
    result=models.CharField(choices=result_type,max_length=50)
    result_date=models.DateTimeField(null=True)
    url=models.CharField(max_length=250,blank=True)
    qr_code=models.ImageField(upload_to='qr_codes',blank=True)

    def __str__(self):
        return str(self.fullName)

    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.url)
        canvas=Image.new('RGB',(370,370),'white')
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname=f'qr{self.passport}.png'
        buffer=BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)