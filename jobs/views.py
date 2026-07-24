from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import JobApplication
from .forms import JobApplicationForm


# ==========================
# Home Dashboard
# ==========================
def home(request):

    total = JobApplication.objects.count()

    applied = JobApplication.objects.filter(
        status='Applied'
    ).count()

    interview = JobApplication.objects.filter(
        status='Interview'
    ).count()

    offer = JobApplication.objects.filter(
        status='Offer'
    ).count()

    accepted = JobApplication.objects.filter(
        status='Accepted'
    ).count()

    rejected = JobApplication.objects.filter(
        status='Rejected'
    ).count()

    context = {
        'total': total,
        'applied': applied,
        'interview': interview,
        'offer': offer,
        'accepted': accepted,
        'rejected': rejected,
    }

    return render(request, 'home.html', context)


# ==========================
# List All Jobs
# ==========================
def job_list(request):

    jobs = JobApplication.objects.all()

    context = {
        'jobs': jobs
    }

    return render(request, 'jobs/list.html', context)


# ==========================
# Create Job
# ==========================
def job_create(request):

    if request.method == 'POST':

        form = JobApplicationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Job Application Added Successfully."
            )

            return redirect('job_list')

    else:

        form = JobApplicationForm()

    context = {
        'form': form
    }

    return render(
        request,
        'jobs/create.html',
        context
    )


# ==========================
# Job Detail
# ==========================
def job_detail(request, id):

    job = get_object_or_404(
        JobApplication,
        id=id
    )

    context = {
        'job': job
    }

    return render(
        request,
        'jobs/detail.html',
        context
    )


# ==========================
# Update Job
# ==========================
def job_update(request, id):

    job = get_object_or_404(
        JobApplication,
        id=id
    )

    if request.method == 'POST':

        form = JobApplicationForm(
            request.POST,
            instance=job
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Application Updated Successfully."
            )

            return redirect('job_list')

    else:

        form = JobApplicationForm(
            instance=job
        )

    context = {
        'form': form,
        'job': job
    }

    return render(
        request,
        'jobs/update.html',
        context
    )


# ==========================
# Delete Job
# ==========================
def job_delete(request, id):

    job = get_object_or_404(
        JobApplication,
        id=id
    )

    if request.method == 'POST':

        job.delete()

        messages.success(
            request,
            "Application Deleted Successfully."
        )

        return redirect('job_list')

    context = {
        'job': job
    }

    return render(
        request,
        'jobs/delete.html',
        context
    )