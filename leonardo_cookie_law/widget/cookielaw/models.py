# -#- coding: utf-8 -#-

from django.utils.translation import ugettext_lazy as _
from django.db import models
from leonardo.widgets import Widget

STYLE_CHOICES = (
    ('dark_bottom', _('Dark bottom')),
    ('dark_floating_tada', _('Dark floating with tada effect')),
    ('dark_floating', _('Dark floating')),
    ('dark_inline', _('Dark inline')),
    ('dark_top', _('Dark top')),
    ('light_bottom', _('Light bottom')),
    ('light_floating', _('Light floating')),
    ('light_top', _('Light top'))
)

class CookieLawWidget(Widget):

    style = models.CharField(verbose_name=_("Style and position"), max_length=255, blank=True, choices=STYLE_CHOICES)

    class Meta:
        abstract = True
        verbose_name = _("Cookie Law")
        verbose_name_plural = _("Cookie Law")
