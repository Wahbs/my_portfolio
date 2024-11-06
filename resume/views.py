from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from .forms import *
# Create your views here.

def index(request):

    context = {
        'type': 'index',
    }
    return render(request, 'index.html', context)

