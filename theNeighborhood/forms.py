from django.contrib.auth.forms import UserCreationForm
from .models import User,Profile
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password')

class Profileform(forms.ModelForm):
     class Meta:
         model= Profile
         exclude = ['user']
