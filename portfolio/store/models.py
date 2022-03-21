from django.db import models







class Pizza(models.Model):
    objects = models.Manager()
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Salad(models.Model):
    objects = models.Manager()
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Noodle(models.Model):
    objects = models.Manager()
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Employees(models.Model):
    objects = models.Manager()
    name=models.CharField(max_length=200, null=True, blank=True)
    status=models.CharField(max_length=100, null=True, blank=True)
    description=models.TextField(max_length=500, null=True, blank=True)
    image=models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class contactPage(models.Model):
    objects = models.Manager()
    name=models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField(max_length=100,)
    message=models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name