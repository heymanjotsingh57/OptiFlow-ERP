from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils import timezone

from .forms import OrderForm
from .models import Order


# ==========================
# HOME PAGE
# ==========================
@login_required(login_url="login")
def home(request):

    search = request.GET.get("search", "")

    orders = Order.objects.all().order_by("-id")

    if search:
        orders = orders.filter(
            Q(customer_name__icontains=search) |
            Q(phone_number__icontains=search)
        )

    context = {
        "orders": orders,
        "total": Order.objects.count(),
        "received": Order.objects.filter(status="RECEIVED").count(),
        "lab": Order.objects.filter(status="AT_LAB").count(),
        "ready": Order.objects.filter(status="READY").count(),
        "search": search,
    }

    return render(request, "orders/home.html", context)


# ==========================
# ADD CUSTOMER
# ==========================
@login_required(login_url="login")
def add_customer(request):

    if request.method == "POST":

        form = OrderForm(request.POST)

        print("POST RECEIVED")

        if form.is_valid():

            print("FORM VALID")
            # Create instance but don't commit so we can set patient_id
            customer = form.save(commit=False)

            # Generate Patient ID based on last order id
            last_order = Order.objects.order_by("-id").first()
            if last_order:
                customer.patient_id = f"PAT{last_order.id + 1:06d}"
            else:
                customer.patient_id = "PAT000001"

            customer.save()

            return redirect("/dashboard/")

        else:
            print("FORM INVALID")
            print(form.errors)

    else:
        form = OrderForm()

    return render(request, "orders/add_customer.html", {"form": form})

# ==========================
# EDIT CUSTOMER
# ==========================
@login_required(login_url="login")
def edit_customer(request, id):

    customer = get_object_or_404(Order, id=id)

    form = OrderForm(instance=customer)

    if request.method == "POST":

        form = OrderForm(
            request.POST,
            instance=customer
        )

        if form.is_valid():
            form.save()
            return redirect("/dashboard/")
        else:
            print(form.errors)

    return render(
        request,
        "orders/edit_customer.html",
        {
            "form": form
        }
    )


# ==========================
# DELETE CUSTOMER
# ==========================
@login_required(login_url="login")
def delete_customer(request, id):

    customer = get_object_or_404(Order, id=id)

    customer.delete()

    return redirect("/dashboard/")

# ==========================
# PRINT RECEIPT
# ==========================
@login_required(login_url="login")
def receipt(request, id):

    customer = get_object_or_404(Order, id=id)

    subtotal = customer.frame_price + customer.lens_price
    grand_total = customer.total_price
    balance_due = customer.balance_due

    context = {
        "customer": customer,
        "total": subtotal,
        "grand_total": grand_total,
        "balance_due": balance_due,
        "today": timezone.now(),
        "invoice_no": f"INV-{customer.id:05d}",
    }

    return render(
        request,
        "orders/receipt.html",
        context
    )

# ==========================
# CUSTOMER ORDER TRACKING
# ==========================
def track_order(request):

    phone = request.GET.get("phone", "").strip()

    orders = []
    message = ""

    if phone:

        orders = Order.objects.filter(
            phone_number__icontains=phone
        ).order_by("-id")

        if not orders.exists():

            message = (
                "No order found with this phone number. "
                "Please check the number and try again or contact our staff."
            )

    context = {
        "phone": phone,
        "orders": orders,
        "message": message,
    }

    return render(
        request,
        "orders/track_order.html",
        context
    )