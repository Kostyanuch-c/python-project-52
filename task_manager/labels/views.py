from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation.trans_real import gettext as _
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from task_manager.common.mixin import MessagesLoginRequiredMixin
from task_manager.labels.form import (
    LabelForm,
    LabelListForm,
)
from task_manager.labels.models import Label


class LabelListView(MessagesLoginRequiredMixin, ListView):
    template_name = "labels/label_list.html"
    model = Label
    extra_context = {
        "form": LabelListForm,
    }


class LabelCreateView(
    MessagesLoginRequiredMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = "labels/label_create.html"
    form_class = LabelForm
    model = Label
    success_url = reverse_lazy("label_list")
    success_message = _("Label successfully created.")

    extra_context = {
        "title_form": _("Create Label"),
        "name_button_in_form": _("Create"),
    }


class LabelUpdateView(
    MessagesLoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    template_name = "labels/label_update.html"
    form_class = LabelForm
    model = Label
    success_url = reverse_lazy("label_list")
    success_message = _("Label successfully updated.")

    extra_context = {
        "title_form": _("Edit label"),
        "name_button_in_form": _("Update"),
    }


class LabelDeleteView(
    MessagesLoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "labels/label_delete.html"
    success_message = _("Label successfully deleted.")
    success_url = reverse_lazy("label_list")
    model = Label
    extra_context = {
        "entity_name": _("label's"),
        "object_field": "name",
    }

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                _("Cannot delete label because it is in use"),
            )
            return redirect(self.success_url)
