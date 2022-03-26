from django.db import models


class BookInventory(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    author = models.CharField(max_length=200,blank=False, default='')
    dateCreated = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

    def get_author(self):
        return self.title + ' belongs to ' + self.author + ' author.'