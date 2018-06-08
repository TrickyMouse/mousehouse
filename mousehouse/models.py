from django.db import models
from django.db.models import permalink
from tinymce.models import HTMLField

# Create your models here.
class Blog(models.Model):
    PG = 1
    ADULT = 2
    ADULT_PLUS = 3
    STANDARD = 4

    TYPES = (
        (PG, 'PG Post'),
        (ADULT, 'Adult Post'),
        (ADULT_PLUS, 'Adult Plus Post'),
        (STANDARD, 'Standard Post')
    )

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = HTMLField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('mousehouse.Category')
    image_link = models.CharField(max_length=255, unique=False, null=True, blank=True)
    album_link = models.CharField(max_length=255, unique=False, null=True, blank=True)
    permission_type = models.SmallIntegerField(choices=TYPES, blank=True, null=True)

    class Meta:
        permissions = (
            ("view_pg", "Can see PG Posts"),
            ("view_adult", "Can see Adult Posts"),
            ("view_adult_plus", "Can see Adult Plus Posts"),
            ("view_standard", "Can see Standard Posts"),
        )

    
    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })