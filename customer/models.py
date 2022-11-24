from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from accounts.models import User
# Create your models here.

class Logo(models.Model):

    image = models.ImageField(_('Image'), upload_to="logo/")
    name = models.CharField(_('Nom'), max_length=255)
    description = models.TextField(_('Description'), null= True, blank=True)
    is_active = models.BooleanField(_('Active'), default=False)

    class Meta:
        verbose_name = _("Logo")
        verbose_name_plural = _("Logos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Logo_detail", kwargs={"pk": self.pk})


class Carousel(models.Model):

    image = models.ImageField(_('Image'), upload_to="Carousel/")
    name = models.CharField(_('Nom'), max_length=255)
    description = models.TextField(_('Description'), null= True, blank=True)
    is_active = models.BooleanField(_('Active'), default=False)

    class Meta:
        verbose_name = _("Carousel")
        verbose_name_plural = _("Carousels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Carousel_detail", kwargs={"pk": self.pk})


class Comments(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name= _("User"),
        on_delete= models.CASCADE,
        null = True,
        blank = True
    )

    text = models.TextField(null = True, blank = True)
    stars = models.IntegerField(null = True, blank = True)
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Comments")
        verbose_name_plural = _("Commentss")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Comments_detail", kwargs={"pk": self.pk})

class Partner(models.Model):

    name = models.CharField(max_length=255, verbose_name=_('Nom'))
    logo = models.ImageField(upload_to = 'partner')
    adresse = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Partner_detail", kwargs={"pk": self.pk})
