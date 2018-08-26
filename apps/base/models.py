# -*- coding: utf-8 -*-
from django.db import models, connection
from apps.authentication.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
""" Academic Level."""


class AcademicLevel(models.Model):
    name = models.CharField(primary_key=True, verbose_name=_('Academic Name'), max_length=30, unique=True,
                            db_index=True)
    description = models.CharField(verbose_name=_('Description'), max_length=120, null=True, blank=True)
    enabled = models.BooleanField(verbose_name=_('Enabled'), default=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        app_label = 'base'
        db_table = 'base_academic'
        verbose_name = _('Academic Level')
        verbose_name_plural = _('Academics Levels')


""" Countries."""


class Countries(models.Model):
    name = models.CharField(verbose_name=_('Country Name'), max_length=200)
    country_code = models.CharField(verbose_name=_('Country Code'), max_length=2, default='US')

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'base'
        db_table = 'base_countries'
        verbose_name = _('country')
        verbose_name_plural = _('countries')


""" Cities."""


class Cities(models.Model):
    name = models.CharField(verbose_name=_('City'), max_length=100, default='')
    country = models.ForeignKey(Countries, verbose_name=_('Country'),
                                on_delete=models.CASCADE)

    def __unicode__(self):
        return self.city

    class Meta:
        app_label = 'base'
        db_table = 'base_cities'
        verbose_name = _('city')
        verbose_name_plural = _('cities')


GENDERS = (
    ('male', 'Male'),
    ('female', 'Female')
)

""" User Profiles."""


class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(_('First Name'), max_length=50, null=True)
    first_name = models.CharField(_('First Name'), max_length=50, null=True)
    last_name = models.CharField(_('Last Name'), max_length=50, null=True)
    display_name = models.CharField(_('Display Name'), max_length=100, null=True)
    gender = models.CharField(max_length=6, verbose_name=_('Gender'), choices=GENDERS, null=True, blank=True)
    email = models.EmailField(_('Email Address'), unique=True)
    last_update = models.DateTimeField(_('Last update'), default=now, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=now, blank=True)
    píc = models.ImageField(upload_to='static/images/profiles/', null=True, blank=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(_('Address'), max_length=120, null=True)
    academic_level = models.ForeignKey(AcademicLevel, on_delete=models.CASCADE, null=True, blank=True)
    enabled = models.BooleanField(null=False, blank=False, default=True)
    birth_date = models.DateField(null=True, blank=True)
    description = models.CharField(_('Bio'), max_length=540, null=True)

    @property
    def is_active(self):
        return bool(self.enabled)

    @property
    def display_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        if self.user.first_name:
            full_name = '%s %s' % (self.user.first_name, self.user.last_name)
            return full_name.strip()
        else:
            return str(self.email)

    def __unicode__(self):  # __str__
        return str(self.email)

    class Meta:
        app_label = 'base'
        db_table = 'base_user_profile'
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')
