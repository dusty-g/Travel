from django.shortcuts import render
from ..trips_app.models import Trip
# Create your views here.
def destination(request, destinationID):
    # display destination data and users 
    print int(destinationID)
    print "type of destination url param"
    trip = Trip.objects.get(id = destinationID)
    print trip.destination
    context = {
        'trip': trip,

    }
    return render(request, 'destinations_app/destination.html', context)