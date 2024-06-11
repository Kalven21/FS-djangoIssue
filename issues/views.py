from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.core.exceptions import ObjectDoesNotExist
from .models import Issue, Status
from accounts.models import Role
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


class IssueListView(ListView):
    template_name = "issues/board.html"
    model = Issue
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue_board"] = (
            Issue.objects
            .order_by("created_on").reverse()
        )
        return context
    
class IssueDetailView(LoginRequiredMixin,UserPassesTestMixin, DetailView):
    template_name = "issues/detail.html"
    model = Issue
    
    def test_func(self):
        team = self.request.user.team
        po_role = Role.objects.get(name="prodect owner")
        try:
            reporter = get_user_model().objects.filter(team=team).get(role=po_role)
        except ObjectDoesNotExist as objexc:
            print("Error: Team has no PO")
            reporter = self.request.user
        finally:
            return team == reporter.team
    
    
class IssueCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["name", "summary", "description", "assignee", "priority", "priority"]
    
    def test_func(self):
        user_role = self.request.user.role
        return user_role.name == "product owner"
    
    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)
    
class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_engine = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("board")
    
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user