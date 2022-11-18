from datacenter.models import Visit
from datacenter.models import get_duration, format_duration, get_strdate_timezone
from django.shortcuts import render


def storage_information_view(request):

    unclosed_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for unclosed_visit in unclosed_visits:
        non_closed_visits.append({
            'who_entered': unclosed_visit.passcard.owner_name,
            'entered_at': get_strdate_timezone(unclosed_visit),
            'duration': format_duration(get_duration(unclosed_visit)),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
