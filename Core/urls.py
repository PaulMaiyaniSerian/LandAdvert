from django.urls import path
from .views import viewLands, contactview, viewOther, viewRanches

urlpatterns = [
    path('viewlands', viewLands, name="viewLands"),
    path('viewproperties', viewOther, name='viewother'),
    path('viewland/<int:id>', viewLands, name="land_detail"),
    path('viewproperty/<int:id>', viewOther, name="property_detail"),
    path('contact_us', contactview, name="contactview"),
    path('ranches', viewRanches, name="viewRanches"),
    path('ranches/<int:id>', viewRanches, name="ranch_detail"),
]
