from django.db import models

from apps.communications.communication_templates.models import (
    CommunicationTemplate
)


class Notification(
    models.Model
):

    EMAIL = 'EMAIL'
    SMS = 'SMS'
    APP = 'APP'
    WHATSAPP = 'WHATSAPP'

    TYPE_CHOICES = [

        (EMAIL, 'Email'),

        (SMS, 'SMS'),

        (APP, 'App Notification'),

        (WHATSAPP, 'WhatsApp'),
    ]

    template = models.ForeignKey(
        CommunicationTemplate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications'
    )

    subject = models.CharField(
        max_length=255
    )

    message = models.TextField()

    notification_type = (
        models.CharField(
            max_length=20,
            choices=TYPE_CHOICES
        )
    )

    scheduled_at = (
        models.DateTimeField(
            null=True,
            blank=True
        )
    )

    status = models.CharField(
        max_length=50,
        default='PENDING'
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        db_table = 'notifications'

        ordering = ['-created_at']

    def __str__(self):

        return self.subject