from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            'company_name',
            'position',
            'job_location',
            'salary',
            'status',
            'application_date',
            'deadline',
            'notes',
        ]

        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name'
            }),

            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job Position'
            }),

            'job_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job Location'
            }),

            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Salary'
            }),

            'status': forms.Select(attrs={
                'class': 'form-select'
            }),

            'application_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'maxlength': 500,
                'placeholder': 'Notes'
            }),
        }

    # Company validation
    def clean_company_name(self):
        company = self.cleaned_data.get('company_name')

        if not company:
            raise forms.ValidationError(
                "Company name is required."
            )

        return company

    # Position validation
    def clean_position(self):
        position = self.cleaned_data.get('position')

        if not position:
            raise forms.ValidationError(
                "Position is required."
            )

        return position

    # Salary validation
    def clean_salary(self):
        salary = self.cleaned_data.get('salary')

        if salary is not None and salary < 0:
            raise forms.ValidationError(
                "Salary cannot be negative."
            )

        return salary

    # Deadline + Notes validation
    def clean(self):
        cleaned_data = super().clean()

        application_date = cleaned_data.get('application_date')
        deadline = cleaned_data.get('deadline')
        notes = cleaned_data.get('notes')

        if application_date and deadline:
            if deadline < application_date:
                self.add_error(
                    'deadline',
                    "Deadline cannot be earlier than application date."
                )

        if notes and len(notes) > 500:
            self.add_error(
                'notes',
                "Notes cannot exceed 500 characters."
            )

        return cleaned_data