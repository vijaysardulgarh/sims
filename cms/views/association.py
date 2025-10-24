from django.shortcuts import render, get_object_or_404, redirect
from cms.utils import get_current_school
from ..models.association import SMCMember
from ..models.association import Association,StaffAssociationRoleAssignment
from ..models.staff import Staff
from django.db.models import Prefetch

def smc_members(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")
    smcmembers = SMCMember.objects.filter(school=school)
    return render(request, "about_us/smc_members.html", {"smcmembers": smcmembers})


def nodal(request):
    school = get_current_school(request)

    if not school:
        return redirect("/")  # Ensure school is set in session

    # Only fetch nodal associations
    nodal_assignments = StaffAssociationRoleAssignment.objects.filter(
        role__association__type__name="Nodal",
        staff__school=school,
    ).select_related(
        "staff", "role", "role__association", "role__association__type"
    )

    # Get distinct staff with preloaded nodal assignments
    staff_members = Staff.objects.filter(
        association_roles__in=nodal_assignments
    ).prefetch_related(
        Prefetch("association_roles", queryset=nodal_assignments, to_attr="nodal_roles")
    ).distinct()

    return render(
        request,
        "about_us/nodal.html",   # ✅ renamed template
        {"staff_members": staff_members, "school": school},
    )




def committee_detail(request, pk):
    committee = get_object_or_404(
        Association.objects.prefetch_related("roles__assigned_staff__staff"),
        pk=pk,
        type__name="Committee"
    )
    return render(request, "committee_detail.html", {"committee": committee})


def staff_association_roles(request):
    staff_members = Staff.objects.prefetch_related(
        "association_roles__role__association__type",
        "association_roles__role__association__school"
    ).all()

    context = {
        "staff_members": staff_members
    }
    return render(request, "staff_association_roles.html", context)


def safety_committee(request): 
    return render(request, "safety_committee.html")

def grievance_committee(request): 
    return render(request, "grievance_committee.html")

def icc_committee(request): 
    return render(request, "icc_committee.html")

def committee_list(request): 
    return render(request, "committee_list.html")

def committee_detail(request): 
    return render(request, "committee_detail.html")

def committee(request): 
    return render(request, "about_us/committee.html")