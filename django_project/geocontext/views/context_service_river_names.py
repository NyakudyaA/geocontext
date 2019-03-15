from django.views.generic import ListView, DetailView
from geocontext.models.context_river_names.py import CollectionName


class ContextRiverNameView(ListView):
    model = CollectionName
    results = CollectionName.search(request.GET['latitude, longitude'])
