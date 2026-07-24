from django.contrib import admin
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'company_name',
        'position',
        'job_location',
        'status',
        'application_date',
        'deadline',
        'created_at',
    )

    list_filter = (
        'status',
        'application_date',
        'deadline',
    )

    search_fields = (
        'company_name',
        'position',
        'job_location',
    )

    ordering = (
        '-created_at',
    )