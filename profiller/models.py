from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profil(models.Model):    
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profil")
    bio = models.CharField(max_length=300,blank=True,null=True)
    sehir = models.CharField(max_length=120,blank=True,null=True)
    foto = models.ImageField(null=True,blank=True, upload_to='profil_sekilleri/%Y/%m/')

    def __str__(self) -> str:
        return f"{self.user.username}"

    class Meta:
        verbose_name_plural = "Profillər"

    def save(self,*args,**kvargs):
        super().save(*args,**kvargs)
        if self.foto:
            img = Image.open(self.foto.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.foto.path)

class ProfilDurum(models.Model):
    class Meta:
        verbose_name_plural = "Profil Mesajları"
    user_profile = models.ForeignKey(Profil,on_delete=models.CASCADE,related_name="durum")
    durum_mesaji = models.CharField(max_length=240)
    yaratilma_zamani = models.DateTimeField(auto_now_add=True)
    guncellenme_zamani = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user_profile}"