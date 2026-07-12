from django.db import models

class HouseModel(models.Model):
  name = models.CharField(max_length=50, verbose_name="Name")
  info = models.TextField(verbose_name="information")
  country = models.CharField(max_length=50, verbose_name="Country")
  address = models.CharField(max_length=100, verbose_name="Address")
  room_count = models.PositiveIntegerField(default=0, verbose_name="Room`s count")
  people_count = models.PositiveIntegerField(default=0, verbose_name="People`s count")
  square = models.PositiveIntegerField(default=0, verbose_name="Square")
  price_by_day = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Payment")
  rating = models.PositiveIntegerField(verbose_name="Rating")

  is_booked = models.BooleanField(default=False, verbose_name='Is booked')

  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name} - {self.country} for ${self.price_by_day} per day with rating: {self.rating}"
  
  class Meta:
    verbose_name = "Будинок"
    verbose_name_plural = "Будинки"
    ordering = ["-created_at"]


class BookingModel(models.Model):
  STATUS_CHOICES = [
    ("in_progress", "В обробці"),
    ("confirmed", "Підтверджено"),
    ("done", "Виконано"),
    ("canceled", "Скасовано"),
  ]
  house = models.ForeignKey(HouseModel, on_delete=models.CASCADE, verbose_name="House", related_name="bookings")
  arrival_date = models.DateField(verbose_name="Arrival date")
  departure_date = models.DateField(verbose_name="Departure date")
  status = models.CharField(choices=STATUS_CHOICES, max_length=20, default="in_progress", verbose_name="Status")
  comment = models.CharField(max_length=150, blank=True, null=True, verbose_name="Comment")

  user_first_name = models.CharField(max_length=50, verbose_name="First name")
  user_last_name = models.CharField(max_length=50, verbose_name="Last name")
  user_phone_number = models.CharField(max_length=20, verbose_name="Phone number")

  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.house.name} booked from {self.arrival_date} to {self.departure_date}"
  
  class Meta:
    verbose_name = "Бронювання"
    verbose_name_plural = "Бронювання"
    ordering = ["-created_at"]
