from django.shortcuts import render
from django.http import HttpResponse
from .models import Taxon

def get_user_obj( request ):
    user_obj = request.user
    if str(user_obj) == 'AnonymousUser':
        return None
    #print("user_obj:", user_obj)
    user_obj.groupname_list = []
    for g in request.user.groups.all():
        user_obj.groupname_list.append(g.name)

    if user_obj.username == 'invisible_admin':
        return user_obj

    return user_obj

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the systax index.")

def taxon_detail(request):
    return HttpResponse("Hello, world. You're at the systax taxon_detail.")

def taxon_add(request):
    return HttpResponse("Hello, world. You're at the systax taxon_detail.")


def taxon_list(request):
    user_obj = get_user_obj( request )
    taxon_list = Taxon.objects.all()

    return render(request, 'systax/taxon_list.html', {'user_obj': user_obj, 'taxon_list': taxon_list} )
    #return HttpResponse("Hello, world. You're at the systax taxon_list.")