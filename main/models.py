from django.db import models
from ckeditor.fields import RichTextField
class Category(models.Model):
    title = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural='Chủ đề'
    def __str__(self):
        return self.title
#News model

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    image = models. ImageField(upload_to='imgs/')
    detail = RichTextField()
    add_time = models. DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Tin tức'
        
    def __str__(self):
        return self.title

#Comments
class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='Bình luận'

    def __str__(self):
        return self.comment
