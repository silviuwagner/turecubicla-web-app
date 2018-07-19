from django.conf import settings
from django.db import models
from django.urls import reverse
from .validators import validate_file_extension
# from PIL import Image
# from io import BytesIO
# from django.core.files.uploadedfile import InMemoryUploadedFile
# import sys

class Trail(models.Model):
	title = models.CharField(max_length=255)
	about = models.TextField(verbose_name='Description of the trail')
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
	)

	region = models.CharField(max_length=100, default='Romania')
	distance = models.PositiveIntegerField(default='0', verbose_name='Distance (in KM)')

	EASY = "Easy"
	MODERATE = "Moderate"
	HARD = "Hard"
	EXTREME = "Extreme"

	DIFFICULTY_CHOICES = (
		(EASY, "Easy"),
		(MODERATE, "Moderate"),
		(HARD, "Hard"),
		(EXTREME, "Extreme"),
	)

	difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)

	homepage_staff_pick = models.BooleanField(default=0)

	#image upload
	image = models.ImageField(upload_to='image/', default='imagelink.jpg')
	# def save(self):
	# 	#Opening the uploaded image
	# 	im = Image.open(self.image)

	# 	output = BytesIO()

	# 	#Resize/modify the image
	# 	im = im.resize( (1920,1442) )

	# 	#after modifications, save it to the output
	# 	im.save(output, format='JPEG', quality=100)
	# 	output.seek(0)

	# 	#change the imagefield value to be the newley modifed image value
	# 	self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

	# 	super(Trail,self).save()

	image_uploaded_at = models.DateTimeField(auto_now_add=True)

	#kml/gpx
	track = models.FileField(upload_to='tracks/', default='tracklink.kml', verbose_name='Track (KML file only)', validators=[validate_file_extension])

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