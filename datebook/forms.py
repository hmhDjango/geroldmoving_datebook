from django import forms
from .models import Move

class MoveForm(forms.ModelForm):
    class Meta:
        model = Move
        widgets = { 'move_date': forms.DateInput(attrs={'class':'datepicker'}),
                  }
        fields = ('move_date', 'weight_rooms', 'origin', 'destination', 'customer', 'company', 'type', 'pk_ld_del', 'men', 'remarks', 'details')


