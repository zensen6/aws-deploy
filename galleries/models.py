from django.db import models
from core.models import TimeStampedModel
from random import randint
# Create your models here.

class BaseModel(TimeStampedModel):
    name = models.CharField(blank=True, max_length = 30)
    def __str__(self):
        return self.name
    class Meta:
        abstract = True

class Photo(BaseModel):
    caption = models.CharField(max_length=50, default=True)
    file = models.ImageField(upload_to="gallery_photos", default=True)
    subject = models.ForeignKey("gallery", related_name="photos", on_delete = models.CASCADE, default=True)

    def __str__(self):
        return self.caption

class gallerytype(BaseModel):

    class Meta:
        verbose_name = "gallery_type"


class gallery(BaseModel):

    gallery_type = models.ForeignKey("gallerytype", related_name ="gallery",on_delete=models.CASCADE, default=True)

    
    def get_photos(self):
        
        rad = randint(0,20)
        photo, = self.photos.all()[rad:rad+1]
        return photo.file.url

    def get_caption(self):

        photo = self.photos.get(pk=99)
        return photo.caption

    