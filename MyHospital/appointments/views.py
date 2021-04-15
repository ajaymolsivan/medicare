from django.contrib import messages

from .forms import CreateAppointment
from django.shortcuts import render, redirect


def appointment(request):
    if request.method == 'POST':
      f = CreateAppointment(request.POST)
      if f.is_valid():
        f.save()
        messages.add_message(request, messages.INFO, 'Appointment Submitted.')
        return redirect('/')
    else:
        f = CreateAppointment()
    return render(request, 'appointment.html', {'form': f})
