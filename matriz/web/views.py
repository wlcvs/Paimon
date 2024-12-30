from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
)

from .models import Matriz

class MatrizListView(ListView):
    model = Matriz

class MatrizCreateView(CreateView):
    model = Matriz
    fields = ["name", "num_of_lines_m", "num_of_columns_n"]

    def get_success_url(self):
        return reverse_lazy(
            "matriz-create",
            kwargs = {"pk": self.object.id}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context["matriz"] = Matriz.objects.get(pk = self.object.id)
        return context
