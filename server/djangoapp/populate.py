# Add this to server/djangoapp/populate.py

from .models import CarMake, CarModel

def initiate():
    # Sample data for CarMake
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "MAZDA", "description": "Great cars. German technology"},
        {"name": "Hyundai", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]
    
    # Create CarMake instances
    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data["name"], description=data["description"]))

    # Sample data for CarModel with a relationship to CarMake
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Altima", "type": "Sedan", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "CX-5", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "Elantra", "type": "Sedan", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3]},
    ]

    # Create CarModel instances
    for data in car_model_data:
        CarModel.objects.create(
            name=data["name"],
            type=data["type"],
            year=data["year"],
            car_make=data["car_make"]
        )
