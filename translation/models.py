from django.db import models
from django.utils.translation import ugettext_lazy as _


class Article(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    content = models.TextField(_("Content"))
