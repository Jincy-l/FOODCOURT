from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
import random

from .models import Register, OTP


# --------------------------
# HOME PAGE
# --------------------------
def home(request):
    return render(request, "home.html")


# --------------------------
# REGISTER
# --------------------------
def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        dob = request.POST.get("dob")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        address = request.POST.get("address")

        # Checking password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        # Checking duplicate email
        if Register.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("register")

        # Creating user
        Register.objects.create(
            name=name,
            dob=dob,
            email=email,
            password=password,
            address=address,
        )

        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    return render(request, "register.html")


# --------------------------
# SEND OTP FUNCTION
# --------------------------
def send_otp_to_email(email):
    otp_code = str(random.randint(100000, 999999))

    OTP.objects.create(
        email=email,
        otp_code=otp_code,
        is_verified=False
    )

    send_mail(
        subject="Your OTP Code",
        message=f"Your OTP is {otp_code}. It is valid for 5 minutes.",
        from_email="jincydhiya2022@gmail.com",
        recipient_list=[email],
        fail_silently=False,
    )

    return otp_code


# --------------------------
# LOGIN
# --------------------------
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Register.objects.get(email=email, password=password)
        except Register.DoesNotExist:
            return render(request, "login.html", {"msg": "Invalid credentials"})

        # Sending OTP
        send_otp_to_email(email)

        # Store email temporarily
        request.session["email"] = email

        return redirect("verify_otp")

    return render(request, "login.html")


# --------------------------
# VERIFY OTP
# --------------------------
def verify_otp(request):
    email = request.session.get("email")

    if not email:
        return redirect("login")

    if request.method == "POST":
        entered_otp = request.POST.get("otp")

        try:
            otp_obj = OTP.objects.filter(email=email, is_verified=False).latest("created_at")
        except OTP.DoesNotExist:
            return render(request, "otp.html", {"msg": "OTP not found. Please login again."})

        # Check expiry
        if otp_obj.is_expired():
            return render(request, "otp.html", {"msg": "OTP expired. Please login again."})

        # Check OTP match
        if otp_obj.otp_code == entered_otp:
            otp_obj.is_verified = True
            otp_obj.save()

            request.session["logged_in"] = True
            request.session["email"] = email

            messages.success(request, "Login successful!")
            return redirect("home")

        return render(request, "otp.html", {"msg": "Incorrect OTP"})

    return render(request, "otp.html")


# --------------------------
# LOGOUT
# --------------------------
def logout_view(request):
    request.session.flush()
    return redirect("login")
def dashboard(request):
    return render(request, "dashboard.html")
def admin_dashboard(request):
    return render(request,"admin_dashboard.html")
