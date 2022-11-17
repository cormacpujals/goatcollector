from django.shortcuts import render

goats = [
  {'name': 'Gereon', 'breed': 'goat', 'description': 'Surprisingly goaty', 'age': 5},
  {'name': 'Bob', 'breed': 'goat', 'description': 'Goatastic. What? That is just a pun about goats', 'age': 8},
  {'name': 'Wallace', 'breed': 'goat', 'description': 'Energetic in a goat a goat would be', 'age': 2},
  {'name': 'Billy The', 'breed': 'goat', 'description': 'Small, but cute one', 'age': 0},
]

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def goats_index(request):
  return render(request, 'goats/index.html', {
    'goats': goats
  })