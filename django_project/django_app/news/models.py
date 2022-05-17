from django.db import models
from django.conf import settings
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
        verbose_name='Блог'
    )

    content = models.TextField(
        blank=True,
        db_index=True,
        verbose_name='Контент'
    )

    data = models.DateTimeField(
        auto_now_add=True,
    )

    image = models.ImageField(
        blank=True,
        upload_to='image/%Y/%m/%d'
    )

    # Таблицанын темасынын атын чыгарып берет.
    def __str__(self):
        return self.title


#---------------------------------------------------
                        #postes

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title