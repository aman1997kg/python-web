from django.db import models

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