from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Event(models.Model):
    """
    Model to store a generic event object that can be serialized for use in the
    calendar on the frontend.
    """

    title = models.CharField(_("Title"), max_length=255)
    notes = models.CharField(_("Notes"), max_length=255, blank=True)
    start = models.DateTimeField(_("Start"))
    end = models.DateTimeField(_("End"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)