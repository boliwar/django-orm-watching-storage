from datacenter.models import Visit
from datacenter.models import get_duration, format_duration, is_visit_long
from django.shortcuts import render
from datetime import datetime


def storage_information_view(request):

    unclosed_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for unclosed_visit in unclosed_visits:
        non_closed_visits.append({
            'who_entered': unclosed_visit.passcard.owner_name,
            'entered_at': datetime.strftime(unclosed_visit.entered_at, '%d %B %Y г. %H:%M'),
            'duration': format_duration(get_duration(unclosed_visit)),
            'is_strange': is_visit_long(unclosed_visit),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
