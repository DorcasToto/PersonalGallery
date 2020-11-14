from django.db import models

# Create your models here.
class Location(models.Model):
    locationName = models.CharField(max_length=30)


class Category(models.Model):
    categoryName = models.CharField(max_length=30)

class Image(models.Model):
    imageName = models.CharField(max_length=30)
    imageDescription = models.CharField(max_length=30)
    imageLocation = models.ForeignKey(Location,on_delete = models.CASCADE)
    imageCategory = models.ForeignKey(Category,on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'images/',default = 'images.jpg')

    def saveImage():
        pass

    def deleteImage():
        pass

    def updateImage():
        pass

    def getImagebyId(id):
        pass

    def searchImage(category):
        pass

    def filterimageByLocation(location):
        pass
