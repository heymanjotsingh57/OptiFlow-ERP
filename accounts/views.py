from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_user(request):

    # If already logged in, go directly to dashboard
    if request.user.is_authenticated:
        return redirect("/dashboard/")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("/dashboard/")

        return render(
            request,
            "accounts/login.html",
            {
                "error": "Invalid Username or Password"
            }
        )

    return render(request, "accounts/login.html")


def logout_user(request):

    logout(request)

    return redirect("login")