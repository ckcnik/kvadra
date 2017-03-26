# Stdlib imports

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _

# Third-party app imports


# Internal apps imports


class Text(models.Model):
    text = models.TextField(_('Text field'))

    class Meta:
        verbose_name = _('Text')
        verbose_name_plural = _('Texts')
