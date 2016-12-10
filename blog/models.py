from __future__ import unicode_literals
from django.db import models

# QuerySet with Custom Managers for filtering everything that is published
class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	object = EntryQuerySet.as_manager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]


