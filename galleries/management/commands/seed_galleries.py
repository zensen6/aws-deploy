from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from galleries import models as galleries_model
from random import choice

NAME = "Gallery"

class Command(BaseCommand):

    help = f"this created {NAME}"

    def add_arguments(self,parser):
        parser.add_argument(
            "--number", default=5, type=int, help=f"how many {NAME} you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        gallery_type_all = galleries_model.gallerytype.objects.all()
        seeder.add_entity(
            galleries_model.gallery, number, {
                "name": lambda x: seeder.faker.sentence(),
                "gallery_type": lambda x: choice(gallery_type_all)
            }

        )
        gallery_id = seeder.execute()
        gallery_id = flatten(gallery_id.values())

        


        for pk in gallery_id:
            G = galleries_model.gallery.objects.get(pk=pk)


            for i in range(30):
                galleries_model.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    subject=G,
                    file=f"gallery_photos/{i}.webp"
                )
