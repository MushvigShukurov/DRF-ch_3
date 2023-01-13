from django.contrib.auth.models import User
from profiller.models import Profil, ProfilDurum
from django.db.models.signals import post_save 
from django.dispatch import receiver


@receiver(post_save,sender=User)
def create_profil(sender,instance,created,**kvargs):
    # print(instance.username," __Created: ",created)
    if created:
        Profil.objects.create(user=instance)

@receiver(post_save,sender=Profil)
def create_profildurum(sender,instance,created,**kvargs):
    if created:
        ProfilDurum.objects.create(user_profile=instance,durum_mesaji=f"Heyyy! {instance.user.username}")