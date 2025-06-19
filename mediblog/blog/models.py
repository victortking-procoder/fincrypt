from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    sequence = models.PositiveIntegerField(unique=True)  # 1 to 10
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.sequence}-{self.title}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sequence}. {self.title}"
