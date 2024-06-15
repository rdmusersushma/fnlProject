#from django.db.models.signals import post_save
#from account.models import CustomUser
#from account.dispatch import receiver
#
#@receiver(post_save, sender=User)
#def create_profile(sender, instance, created, **kwargs):
#	if created:
#		TeacherProfile.objects.create(user=instance)
#		StudentProfile.objects.create(user=instance)
#
#@receiver(post_save, sender=User)
#def save_profile(sender, instance, **kwargs):
#	instance.profile.save()
