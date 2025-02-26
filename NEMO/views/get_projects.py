from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

from NEMO.decorators import any_staff_required, staff_member_or_tool_superuser_required
from NEMO.models import User


@staff_member_or_tool_superuser_required
@require_GET
def get_projects_for_training(request):
    return get_projects(request)


@any_staff_required
@require_GET
def get_projects_for_consumables(request):
    return get_projects(request)


def get_projects(request):
    """Gets a list of all active projects for a specific user. This is only accessible by staff members."""
    user = get_object_or_404(User, id=request.GET.get("user_id", None))
    projects = user.active_projects()
    source_template = request.GET.get("source_template")
    if source_template == "training":
        entry_number = int(request.GET["entry_number"])
        return render(request, "training/get_projects.html", {"projects": projects, "entry_number": entry_number})
    return JsonResponse(dict(projects=list(projects.values("id", "name"))))


@any_staff_required
@require_GET
def get_projects_for_tool_control(request):
    user_id = request.GET.get("user_id")
    user = get_object_or_404(User, id=user_id)
    return render(
        request, "tool_control/get_projects.html", {"active_projects": user.active_projects(), "user_id": user_id}
    )


@login_required
@require_GET
def get_projects_for_self(request):
    """Gets a list of all active projects for the current user."""
    return render(
        request,
        "tool_control/get_projects.html",
        {"active_projects": request.user.active_projects(), "user_id": request.user.id},
    )
