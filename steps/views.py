from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def sandwich_steps(request):
    steps = [
        "Gather ingredients: bread, peanut butter, jelly.",
        "Spread peanut butter on one slice of bread.",
        "Spread jelly on the other slice.",
        "Put the slices together and enjoy."
    ]
    return JsonResponse({'steps': steps})

def sandwich_ingredients(request):
    ingredients = [
        "2 slices of bread",
        "Peanut butter",
        "Jelly"
    ]
    return JsonResponse({'ingredients': ingredients})
