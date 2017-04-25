from django.shortcuts import render, redirect
from models import Trip
from django.contrib import messages
from ..users_app.models import User
# Create your views here.
def travels(request):
    # not sure if request.session will work here
    user = User.objects.get(id = request.session['user_id'])
    
    trips = Trip.objects.filter(planned_by = user) | Trip.objects.filter(joined_by = user)
    other_trips = Trip.objects.exclude(planned_by = user).exclude(joined_by = user)
    context = {
        'trips': trips,
        'other_trips': other_trips
    }
    return render(request, 'trips_app/travels.html', context)
def add(request):
    return render(request, 'trips_app/add.html')

def process(request):
    add_result = Trip.objects.addTrip(request.POST)
    if add_result['valid']:
        return redirect('travels:travels')
    else:
        for error in add_result['errors']:
            messages.error(request, error)
        
        return redirect('travels:add')
def join(request):
    
    result = Trip.objects.joinTrip(request.POST)
    if result:
        return redirect("travels:travels")