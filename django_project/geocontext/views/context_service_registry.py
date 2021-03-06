# coding=utf-8
"""View for CSR."""

from django.views.generic import ListView, DetailView
from geocontext.models.context_service_registry import ContextServiceRegistry


class ContextServiceRegistryListView(ListView):
    """List view for CSR."""

    model = ContextServiceRegistry
    template_name = 'geocontext/context_service_registry_list.html'
    context_object_name = 'csr_list'
    paginate_by = 10


class ContextServiceRegistryDetailView(DetailView):
    """Detail view for CSR."""

    model = ContextServiceRegistry
    template_name = 'geocontext/context_service_registry_detail.html'
    context_object_name = 'csr'
    slug_field = 'key'
