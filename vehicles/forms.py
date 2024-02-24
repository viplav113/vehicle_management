from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Post
from .models import Vendor, Vehicle

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

from django import forms
from .models import Vehicle, QualityCheck

class VehicleInfoForm(forms.ModelForm):
    # Add these fields to include Product information
    # Assuming vendor is a CharField, adjust as needed

    class Meta:
        model = Vehicle
        fields = ["vehicle_number", "vehicle_type", "dc_number", "po_number"]



class QualityCheckForm(forms.ModelForm):
    class Meta:
        model = QualityCheck
        fields = ["po_number", "quality_result"]

    po_number = forms.CharField(max_length=50, required=True)
    quality_result = forms.ChoiceField(choices=[('Pass', 'Pass'), ('Fail', 'Fail')], required=True)


class VendorInfoForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ["name", "company_name", "po_number"]

    def __init__(self, *args, **kwargs):
        super(VendorInfoForm, self).__init__(*args, **kwargs)

        # Retrieve distinct po_numbers from Vehicle model
        po_numbers = Vehicle.objects.values_list('po_number', flat=True).distinct()

        # Create choices list for the po_number field
        choices = [(po_number, po_number) for po_number in po_numbers]

        # Add an empty option at the beginning
        choices.insert(0, ('', 'Select a PO Number'))

        # Set the choices for the po_number field
        self.fields['po_number'].choices = choices
