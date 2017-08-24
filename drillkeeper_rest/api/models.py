from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Show(models.Model):
    """This class represents the marching band show model."""
    name = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)

class Set(models.Model):
    """This class represents the marching band set model."""
    # Initialize constants
    FRONT_HASH = 'FH'
    BACK_HASH = 'BH'
    FRONT_SIDELINE = 'FS'
    BACK_SIDELINE = 'BS'

    HASH_LINE_CHOICES = (
        (FRONT_HASH, 'Front Hash'),
        (BACK_HASH, 'Back Hash'),
        (FRONT_SIDELINE, 'Front Sideline'),
        (BACK_SIDELINE, 'Back Sideline'),
    )

    # Identifying information
    number = models.IntegerField()
    subset = models.IntegerField()
    counts = models.IntegerField()

    # Horizontal position
    yard_line = models.IntegerField()
    side = models.IntegerField()
    x = models.FloatField()

    # Vertical position
    hash_line = models.CharField(max_length=2, choices=HASH_LINE_CHOICES)
    y = models.FloatField()

    # Reference to show it belongs to
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
