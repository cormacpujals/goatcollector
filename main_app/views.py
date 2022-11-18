from django.shortcuts import render, redirect
from .models import Goat, Toy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import FeedingForm
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def goats_index(request):
  goats = Goat.objects.all()
  return render(request, 'goats/index.html', {
    'goats': goats
  })

def goats_detail(request, goat_id):
  goat = Goat.objects.get(id=goat_id)
  id_list = goat.toys.all().values_list('id')
  toys_goat_doesnt_have = Toy.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'goats/detail.html', { 
    'goat': goat,
    'feeding_form': feeding_form,
    'toys': toys_goat_doesnt_have,
    })

class GoatCreate(CreateView):
  model = Goat
  fields = ['name', 'breed', 'description', 'age']

class GoatUpdate(UpdateView):
  model = Goat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'breed', 'description', 'age']

class GoatDelete(DeleteView):
  model = Goat
  success_url = '/goats'

def add_feeding(request, goat_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.goat_id = goat_id
    new_feeding.save()
  return redirect('detail', goat_id=goat_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'

def assoc_toy(request, goat_id, toy_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Goat.objects.get(id=goat_id).toys.add(toy_id)
  return redirect('detail', goat_id=goat_id)

def unassoc_toy(request, goat_id, toy_id):
  Goat.objects.get(id=goat_id).toys.remove(toy_id)
  return redirect('detail', goat_id=goat_id)