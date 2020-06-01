from django.forms import ModelForm, EmailInput

from personas.models import Persona


class PersonaFormPersonalizado(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email' : EmailInput(attrs={'type' : 'email'})
        }
