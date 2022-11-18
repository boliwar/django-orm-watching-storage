from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration, get_strdate_timezone, is_visit_long
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in passcard_visits:
        this_passcard_visits.append({
            'entered_at': get_strdate_timezone(visit),
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
