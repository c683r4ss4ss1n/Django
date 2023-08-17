from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1  = Destination()
    dest1.name = 'Bali'
    dest1.desc = 'What The Hell is this'
    dest1.price = 700
    dest1.img = 'destination_1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Bali 2'
    dest2.desc = 'What The Hell is this 2'
    dest2.price = 702
    dest2.offer = True 
    dest2.img = 'destination_2.jpg'

    dest3 = Destination()
    dest3.name = 'Bali 3'
    dest3.desc = 'What The Hell is this 3'
    dest3.price = 703
    dest3.offer = True
    dest3.img = 'destination_3.jpg'

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})