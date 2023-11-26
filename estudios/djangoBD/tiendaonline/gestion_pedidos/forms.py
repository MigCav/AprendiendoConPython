from django import forms

class formulario_contacto(forms.Form):
    
    asunto= forms.CharField()
    email= forms.EmailField()
    mensaje= forms.CharField()
    
    #formulario_contacto.cleaned_data   para recuperrar en shell solo la informacion
    
    