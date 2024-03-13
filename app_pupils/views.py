from django.shortcuts import render, get_object_or_404
from .models import pupils


# Create your views here.

def pupils_list(request):
    pupil = pupils.objects.all()
    return render(request, 'information.html', {'pupils': pupil})


def pupils_detail(request, id):
    pupil = get_object_or_404(pupils, id=id)
    return render(request, 'pupil_detail.html', {'pupil': pupil})
