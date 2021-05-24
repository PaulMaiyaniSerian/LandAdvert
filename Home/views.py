from django.shortcuts import render
from Core.models import Land, OtherProperty,Ranch

# Create your views here.
def homepage(request):
    if request.method == "GET":
        latestLands = Land.objects.filter(latest=True, available=True).order_by("-date_created")
        latestProperties = OtherProperty.objects.filter(latest=True, available=True).order_by("-date_created")
        latestRanches = Ranch.objects.filter(latest=True, available=True).order_by("-date_created")
        
        context = {
            'latestLands': latestLands,
            'latestProperties': latestProperties,
            'latestRanches': latestRanches,
        }
    else:
        return "INVALID METHOD"
    
    return render(request, 'index.html', context=context)