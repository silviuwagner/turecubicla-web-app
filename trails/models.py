from django.conf import settings
from django.db import models
from django.urls import reverse
from .validators import validate_file_extension

class Trail(models.Model):
	title = models.CharField(max_length=255)
	about = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
	)

	region = models.CharField(max_length=100, default='Romania')
	distance = models.PositiveIntegerField(default='0')

	difficulty = models.CharField(max_length=10,default='Easy')

	homepage_staff_pick = models.BooleanField(default=0)

	#image upload
	image = models.ImageField(upload_to='image/', default='imagelink.jpg')
	image_uploaded_at = models.DateTimeField(auto_now_add=True)

	#kml/gpx
	track = models.FileField(upload_to='tracks/', default='tracklink.kml', validators=[validate_file_extension])

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('trail_detail', args=[str(self.id)])

class Comment(models.Model):
	trail = models.ForeignKey(Trail, on_delete=models.CASCADE, related_name='comments')
	comment = models.CharField(max_length=140)
	author = models.ForeignKey(
			settings.AUTH_USER_MODEL,
			on_delete=models.CASCADE,
		)

	def __str__(self):
		return self.comment

	def get_absolute_url(self):
		return reverse('trail_list')

# 
# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.ImageField(upload_to='media/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)