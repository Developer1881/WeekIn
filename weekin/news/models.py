from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django_countries.fields import CountryField
from django.core.urlresolvers import reverse



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')



class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
        unique_for_date='week_end')
    author = models.ForeignKey(User, related_name='news_post')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10,
        choices=STATUS_CHOICES,
        default='draft')

    week_start = models.DateField()
    week_end = models.DateField()

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    #country_field = CountryField()

    class Meta:
        ordering = ('-week_end',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:post_detail', args=[self.week_end.year,
                                                 self.week_end.strftime('%m'),
                                                 self.week_end.strftime('%d'),
                                                 self.slug])

class SubPost(models.Model):
    headline = models.CharField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.headline

    class Meta:
         ordering = ('headline',)



# Create your models here.
