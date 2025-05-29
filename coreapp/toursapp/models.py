from django.db import models
import uuid

# Tour Models 
class Tour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField()
    departure = models.CharField(max_length=100)
    departure_date = models.DateField()
    image_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title