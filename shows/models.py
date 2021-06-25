from django.db import models

# Create your models here.
class Network(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # shows = a list of shows associated with a given network

    def __repr__(self):
        return f"Network: (ID: {self.id}) -> {self.title}"

class Show(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    network = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Show: (ID: {self.id}) -> {self.title} = {self.description} by {self.network}"