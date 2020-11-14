from django.db import models

# Create your models here.
class Location(models.Model):
    locationName = models.CharField(max_length=30)

    def saveLocation(self):
        self.save()

    def deleteLocation(self):
        self.delete()

    def updateLocation():
        pass

    def __str__(self):
        return self.locationName


class Category(models.Model):
    categoryName = models.CharField(max_length=30)

    def saveCategory(self):
        self.save()

    def deleteCategory(self):
        self.delete()

    def updateCategory():
        pass

    def __str__(self):
        return self.categoryName

class Image(models.Model):
    imageName = models.CharField(max_length=30)
    imageDescription = models.CharField(max_length=30)
    imageLocation = models.ForeignKey(Location,on_delete = models.CASCADE)
    imageCategory = models.ForeignKey(Category,on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'images/',default = 'images.jpg')

    def saveImage(self):
        self.save()

    def deleteImage(self):
        self.delete()

    def updateImage():
        pass

    def getImagebyId(id):
        pass
    
    @classmethod
    def searchImage(cls,category):
        category = cls.objects.filter(imageCategory__icontains=category)
        return category

    def filterimageByLocation(cls,location):
        location = cls.objects.filter(imageLocation = location)
        return location

    def __str__(self):
        return self.imageName
