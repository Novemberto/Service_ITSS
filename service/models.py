from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.

class Service(models.Model):

    name = models.CharField(_('Titre'), max_length=255)
    description = models.TextField(_('Description'), null = True, blank = True)
    file = models.FileField(_('File'), null = True, blank = True, upload_to='service/')
    icone = models.CharField(max_length=255, null = True, blank = True, verbose_name=_('Icône'))
    is_actif = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})

class Offre(models.Model):

    name = models.CharField(_('Titre'), max_length=255)
    description = models.TextField(_('Description'))
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Offre")
        verbose_name_plural = _("Offres")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Offre_detail", kwargs={"pk": self.pk})
