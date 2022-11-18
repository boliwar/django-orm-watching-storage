import locale
from django.db import models
from django.utils.timezone import localtime as dj_localtime, now as dj_now
from datetime import datetime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

def get_strdate_timezone(visit):
    locale.setlocale(locale.LC_ALL, '')
    visit_date = dj_localtime(visit.entered_at)
    date_str = datetime.strftime(visit_date, '%d %B %Y г. %H:%M')
    return date_str

def get_duration(visit):
    return dj_now() - dj_localtime(visit.entered_at)

def format_duration(duration):
    total_seconds = duration.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds - (hours*3600 + minutes* 60))
    return f'{hours}:{minutes:02d}:{seconds:02d}'