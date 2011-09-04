from django.db import models

# Create your models here.

    




class User(models.Model):
	def __unicode__(self):
		return self.username
	username = models.CharField('user name', max_length=50)
	password = models.CharField(max_length=50)
	firstname = models.CharField('user\'s first name', max_length=50)
	lastname = models.CharField('user\'s last name', max_length=50)
	email = models.CharField('user\'s email addres', max_length=100)
	phone = models.CharField(max_length=50)
	sms_approved = models.IntegerField()
	registered_date = models.DateTimeField('date that the user registered')
	last_login = models.DateTimeField('last date that the user logged in')
	email_verified = models.BooleanField('has the user verified their email')


class Trip(models.Model):
	def __unicode__(self):
		return self.url
	created_by_user = models.ForeignKey(User, related_name='trip_user')
	controlling_user = models.ForeignKey(User)
	active = models.BooleanField()
	url = models.CharField('URL that this trip can be shared at', max_length=100)
	private = models.BooleanField()



	
	

class TripDestination(models.Model):
	def __unicode__(self):
		return self.location
	trip = models.ForeignKey(Trip, related_name='tripdestination_parent')
	location = models.CharField('location of the destination', max_length=1000)
	order = models.IntegerField('order among all destinations')

class TripMember(models.Model):
	def __unicode__(self):
		return self.user
	trip = models.ForeignKey(Trip, related_name='tripmember_parent')
	user = models.ForeignKey(User)
	last_known_loc = models.CharField('user\'s last known location', max_length=1000)
	trip_destination_id = models.ForeignKey(TripDestination)


class FriendRel(models.Model):
	def __unicode__(self):
		return self.user1
	user1 = models.ForeignKey(User, related_name='user_friend1')
	user2 = models.ForeignKey(User, related_name='user_friend2')
	accepted = models.BooleanField('has the user accepted the friend request')
	date_added = models.DateTimeField('date that the friend request was added')




