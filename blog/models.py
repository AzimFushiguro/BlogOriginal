from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Posts(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  # 1 ni mavjud category ID bilan almashtiring
    created_at = models.DateTimeField(auto_now=True)
    read_time = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
