from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .forms import RegisterForm, VehicleInfoForm, QualityCheckForm, VendorInfoForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Vehicle, Vendor, Product, QualityCheck
from .models import Vehicle, Product  # Import Product model
from .forms import VehicleInfoForm, QualityCheckForm
from django.db.models import Prefetch
@login_required(login_url="/login")
def home(request):
    posts = Vehicle.objects.filter(user=request.user)

    if request.method == "POST":
        post_id = request.POST.get("post-id")

        if post_id:
            post = Vehicle.objects.filter(id=post_id, user=request.user).first()
            if post:
                post.delete()

    return render(request, 'vehicles/home.html', {"posts": posts})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

@login_required(login_url="/login")
#@permission_required("vehicles.add_post", login_url="/login", raise_exception=True)
 # Assuming you have a form for creating vehicles




def create_post(request):
    if request.method == 'POST':
        form = VehicleInfoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("/home")
    else:
        form = VehicleInfoForm(initial={'author_id': request.user.id})

    return render(request, 'vehicles/create_post.html', {"form": form})


@login_required(login_url="/login")
def add_vendor(request):
    if request.method == 'POST':
        form = VendorInfoForm(request.POST)
        if form.is_valid():
            # Save the vendor information to the database
            vendor = form.save()
            return redirect('/home')  # Redirect to home or another page as needed
    else:
        form = VendorInfoForm()

    return render(request, 'vehicles/add_vendor.html', {"form": form})


@login_required(login_url="/login")
#@permission_required("vehicles.change_qualitycheck", login_url="/login", raise_exception=True)


def perform_quality_check(request):
    if request.method == 'POST':
        form = QualityCheckForm(request.POST)
        if form.is_valid():
            po_number = form.cleaned_data['po_number']
            quality_result = form.cleaned_data['quality_result']

            vehicle = get_object_or_404(Vehicle, po_number=po_number)

            if quality_result == 'Pass':
                # Delete the vehicle with the specified po_number
                vehicle.delete()
                return redirect('home')  # Replace with the actual URL name or path
            elif quality_result == 'Fail':
                message = f"Vehicle with PO Number {po_number} is under maintenance."
                return render(request, 'vehicles/maintenance_message.html', {'message': message})

    else:
        form = QualityCheckForm()

    return render(request, 'vehicles/quality_check.html', {'form': form})