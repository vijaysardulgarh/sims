from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('issued', 'Issued'),
        ('lost', 'Lost'),
        ('damaged', 'Damaged'),
    ]

    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255, blank=True, null=True)

    category = models.CharField(max_length=100)
    language = models.CharField(max_length=50, blank=True, null=True)

    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)

    rack_number = models.CharField(max_length=50, blank=True, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )

    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title