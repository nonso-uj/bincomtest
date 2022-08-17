from django.shortcuts import render
from .models import Agentname, Party, PollingUnit, Lga, Ward, States

# Create your views here.



def states_view(request):
    states = States.objects.all()

    context = {
        'states': states
    }
    return render(request, 'units/states.html', context)


def lga_view(request):
    state = States.objects.get(state_name='Delta')
    lgas = Lga.objects.filter(state_id=state.state_id)

    context = {
        'lgas': lgas,
        'state': state
    }
    return render(request, 'units/lgas.html', context)


def ward_view(request, pk):
    wards = Ward.objects.filter(lga_id=pk)

    context = {
        'wards': wards
    }
    return render(request, 'units/wards.html', context)


def polls_view(request, pk):
    polls = PollingUnit.objects.filter(ward_id=pk)

    context = {
        'polls': polls
    }
    return render(request, 'units/polling-units.html', context)

