from django.db import models


class Order(models.Model):

    # ==========================
    # Choices
    # ==========================

    STATUS_CHOICES = [
        ("RECEIVED", "Received"),
        ("AT_LAB", "At Lab"),
        ("READY", "Ready"),
    ]

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    # ==========================
    # Customer Information
    # ==========================

    patient_id = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    customer_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=15)

    address = models.TextField(
        blank=True,
        default=""
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
        default=""
    )

    # ==========================
    # Doctor Information
    # ==========================

    doctor_name = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    # ==========================
    # Frame & Lens
    # ==========================

    frame_details = models.CharField(max_length=100)

    lens_details = models.CharField(max_length=100)

    frame_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    lens_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # ==========================
    # Eye Prescription
    # ==========================

    right_eye_sph = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    right_eye_cyl = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    right_eye_axis = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    left_eye_sph = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    left_eye_cyl = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    left_eye_axis = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    # ==========================
    # PD (Pupillary Distance)
    # ==========================

    pd = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    # ==========================
    # Billing
    # ==========================

    gst = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        blank=True
    )

    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        blank=True
    )

    advance_paid = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        blank=True
    )

    # ==========================
    # Order Information
    # ==========================

    delivery_date = models.DateField(
        null=True,
        blank=True
    )

    remarks = models.TextField(
        blank=True,
        default=""
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="RECEIVED"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # ==========================
    # Calculations
    # ==========================

    @property
    def total_price(self):
        subtotal = self.frame_price + self.lens_price
        gst_amount = subtotal * (self.gst / 100)
        return subtotal + gst_amount - self.discount

    @property
    def balance_due(self):
        return self.total_price - self.advance_paid

    def __str__(self):
        return f"{self.patient_id or 'NEW'} - {self.customer_name}"