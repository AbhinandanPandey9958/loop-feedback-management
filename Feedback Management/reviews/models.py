# from django.db import models

# Create your models here.


from django.db import models


class Feedback(models.Model):

    CHANNEL_CHOICES = [
        ('SUPPORT', 'Support Ticket'),
        ('APP_STORE', 'App Store'),
        ('SURVEY', 'Survey'),
        ('SALES', 'Sales Call'),
        ('SOCIAL', 'Social Media'),
    ]

    SENTIMENT_CHOICES = [
        ('POS', 'Positive'),
        ('NEU', 'Neutral'),
        ('NEG', 'Negative'),
    ]

    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('REVIEWED', 'Reviewed'),
        ('ACTIONED', 'Actioned'),
    ]

    content = models.TextField()
    channel = models.CharField(
        max_length=20,
        choices=CHANNEL_CHOICES
    )
    source_ref = models.CharField(
        max_length=255,
        blank=True
    )
    customer_label = models.CharField(
        max_length=100,
        blank=True
    )

    sentiment = models.CharField(
        max_length=3,
        choices=SENTIMENT_CHOICES,
        default='NEU'
    )

    sentiment_score = models.FloatField(
        default=0.0
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='NEW'
    )

    theme = models.CharField(
        max_length=100,
        blank=True
    )

    feature_area = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.content[:60]