from django.contrib import admin
from .models import gallery, Photo, gallerytype

# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display=(
        "caption",
    )

@admin.register(gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display =(
        "name",
    )

@admin.register(gallerytype)
class GallerytypeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )
