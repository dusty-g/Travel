from __future__ import unicode_literals
from ..users_app.models import User
from django.db import models
import datetime


class TripManager(models.Manager):
    def addTrip(self, postData):
        data = {
            'valid': False,
            'errors': [],
        }
        if not postData:
            data['errors'].append('post data only!')
            return data
        # no empty entries
        print "*"*50
        print "types..."
        print type(postData['to_date'])
        
        if len(postData['destination']) < 1:
            data['errors'].append('destination cannot be empty')
        if len(postData['description']) < 1:
            data['errors'].append('description cannot be empty')
        if postData['to_date'] == "":
            data['errors'].append('dates cannot be empty')
            return data
        if len(postData['from_date']) < 1:
            data['errors'].append('dates cannot be empty')
            return data
        start_date = datetime.datetime.strptime(postData['from_date'], '%Y-%m-%d')
        end_date = datetime.datetime.strptime(postData['to_date'], '%Y-%m-%d')
        if not isinstance(start_date, datetime.date):
            data['errors'].append('invalid start date')
        if not isinstance(end_date, datetime.date):
            data['errors'].append('invalid end')
        # future travel dates
        today = datetime.datetime.now()
        if start_date < today:
            data['errors'].append('start date must be in the future')
        if end_date < today:
            data['errors'].append('end date must be in the future')
        if end_date < start_date:
            data['errors'].append('end date must be after start date')
        # to must be after from
        if data['errors']:
            return data
        else:
            data['valid'] = True
            user = User.objects.get(id = postData['user_id'])
            newTrip = Trip.objects.create(destination = postData['destination'], description = postData['description'], from_date = postData['from_date'], to_date = postData['to_date'], planned_by = user)
            print newTrip.id, newTrip.destination, newTrip.planned_by.username
            return data

    def joinTrip(self, postData):
        if not postData:
            return False

        user = User.objects.get(id = postData['user_id'])
        trip = Trip.objects.get(id = postData['trip_id'])
        trip.joined_by.add(user)
        
        return True

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    planned_by = models.ForeignKey(User, related_name='trips_planned')
    joined_by = models.ManyToManyField(User, related_name='trips_joined')


    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = TripManager()