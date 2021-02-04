from django.shortcuts import redirect, render
from .models import Tache, Category, TypeDeTache
from .forms import ApplyTach
from django.urls import reverse
# Create your views here.



def tache_type(request,slug):
    type1 = TypeDeTache.objects.get(slug=slug)
    all_type = TypeDeTache.objects.all()
    tache_type = Tache.objects.all()
    context={'type1':type1, 'types':all_type, 'tache_type':tache_type}
    return render(request,'ponctuel.html',context)


def get_acceuil(request):
    all_type = TypeDeTache.objects.all()
    all_tache = Tache.objects.all()
    return render(request,'test.html',{'types':all_type,'all_tache':all_tache})



def add_tache(request):
    
    if request.method=='POST':
        form = ApplyTach(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('taches:add_tache'))
    else:
        form = ApplyTach()
    
    all_type = TypeDeTache.objects.all()
    return render(request,'add_tache.html',{'form':form , 'types':all_type})


def detail(request,id):
    tache_detail = Tache.objects.get(id=id)
    all_type = TypeDeTache.objects.all()
    return render(request,'detail.html',{'detail':tache_detail, 'types':all_type})

