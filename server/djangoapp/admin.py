# Uncomment the necessary imports at the top of the file
from django.contrib import admin
from .models import CarMake, CarModel  # Import your models

# Define CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1  # This determines how many empty inline forms to display initially

# Define CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'year', 'car_make']

# Define CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Add CarModelInline to CarMakeAdmin
    list_display = ['name', 'description']  # Display fields for CarMake
    search_fields = ['name']  # Enable search by name

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
