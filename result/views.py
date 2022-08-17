from django.shortcuts import render
from django.db.models import Sum

from .models import AnnouncedLgaResults, AnnouncedPuResults
from units.models import PollingUnit, Lga, States
from units.forms import PollResultForm
# Create your views here.


def poll_results(request, pk):
    results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=pk)

    context = {
        'results': results
    }
    return render(request, 'result/poll-results.html', context)


def direct_results(request):
    if request.method == 'POST':
        result = request.POST.get('result')

        results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=result)

        context = {
            'results': results
        }
        return render(request, 'result/poll-results.html', context)



def new_poll_result(request):
    form = PollResultForm()

    if request.method == 'POST':
        form = PollResultForm(request.POST)

        if form.is_valid():
            poll = form.save(commit=False)
            user = form.cleaned_data['entered_by_user']
            user_ip_address = form.cleaned_data['user_ip_address']
            date_entered = request.POST.get('date_entered')
            p_abbrv = request.POST.getlist('party_abbreviation[]')
            p_score = request.POST.getlist('party_score[]')

            poll.date_entered = date_entered
            poll.save()

            unique = PollingUnit.objects.get(date_entered=date_entered)

            uniqueid = unique.uniqueid

            if (len(p_abbrv)==len(p_score)):
                mapped = zip(p_abbrv, p_score)
                mapped = list(mapped)

                for el in mapped:
                    if el[0] and el[1]:
                        poll_result, created = AnnouncedPuResults.objects.get_or_create(
                            polling_unit_uniqueid=uniqueid,
                            party_abbreviation=el[0],
                            party_score=el[1],
                            entered_by_user=user,
                            date_entered=date_entered,
                            user_ip_address=user_ip_address
                        )
        else:
            print('error', form.errors)

    context = {
        'form': form
    }
    return render(request, 'result/new-result.html', context)



def total_lga_pu(request):
    state = States.objects.get(state_name='Delta')
    lgas = Lga.objects.filter(state_id=state.state_id)
    total = ''
    parties = ''
    current = ''

    if request.method == 'POST' and request.POST.get('lga') != None and request.POST.get('lga') != '':
        current = request.POST.get('lga')

        polls = PollingUnit.objects.filter(lga_id=current)
        print(polls)

        results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid__in=polls)
        print(results)

        parties = results.values('party_abbreviation').annotate(Sum('party_score')).order_by('party_abbreviation')
        print(parties)

        total = results.aggregate(total=Sum('party_score'))
        print(total)

        current = lgas.get(lga_id=current)

    context = {
        'lgas': lgas,
        'state': state,
        'total': total,
        'parties': parties,
        'current': current
    }
    for field in context.values():
        print(field)
    return render(request, 'result/total-lga-pu.html', context)