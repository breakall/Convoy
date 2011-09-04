from djangorestframework.resources import ModelResource
from convoyapp.models import User

class UserModelResource(ModelResource):
    model = User
    fields = ('username', 'firstname', 'lastname', 'email', 'phone', 'sms_approved', 'registered_date', 'last_login', 'email_verified')
    ordering = ('username',)

