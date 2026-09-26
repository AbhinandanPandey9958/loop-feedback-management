from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'content',
        'channel',
        'sentiment',
        'status',
        'created_at',
    )

    list_filter = (
        'channel',
        'sentiment',
        'status',
    )

    search_fields = (
            'content',
            'customer_label',
            'theme',
            'feature_area',
                )

    ordering = ('-created_at',)