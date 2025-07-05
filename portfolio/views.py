from django.shortcuts import render
from .supabase_client import supabase
# Create your views here.
# def home(request):
#     return render(request,'index.html')



def home(request):
    # Fetch skills data
    skills_response = supabase.table('skills').select("*").execute()
    skills = skills_response.data  # List of dicts

    return render(request, 'index.html', {'skills': skills})
