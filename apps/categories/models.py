from django.db import models


class Category(models.Model):
    """ Category Model """
    title = models.CharField(
        max_length=120
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
