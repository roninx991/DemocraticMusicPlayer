from django.db import models
from django.db.models.signals import pre_save,post_save
from songs.utils import unique_slug_generator
# Create your models here.

class Song(models.Model):
	Name 		= models.CharField(max_length=200,unique=False)
	Singer		= models.CharField(max_length=120,null=True,blank=True,unique=False)
	Genre 		= models.CharField(max_length=120,null=True,blank=True,unique=False)
	slug		= models.SlugField(null=True,blank=True)
	Votes		= models.BigIntegerField(default=0,unique=False)
	
	def __str__(self):
		return self.Name
		
	@property
	def title(self):
		return self.Name
		
def rl_pre_save_receiver(sender,instance,*args,**kwargs):
#	print('saving...')
#	print(instance.Name)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
		instance.save()
	
#def rl_post_save_receiver(sender,instance,*args,**kwargs):
#	print('saved')
#	print(instance.Name)
	
pre_save.connect(rl_pre_save_receiver, sender=Song)

#post_save.connect(rl_post_save_receiver, sender=Song)
