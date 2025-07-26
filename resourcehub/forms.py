from django import forms
from .models import Resource, Technology, Category


class ResourceForm(forms.ModelForm):
    """
    A ModelForm for creating and updating Resource objects.
    This form is directly linked to the Resource model.
    """

    class Meta:
        # 1. Specify the model the form is based on.
        model = Resource

        # 2. List the fields to include in the form.
        fields = ["title", "url", "description", "technology", "categories"]

        # 3. Define widgets to customize the appearance of form fields.
        #    This is the best place to add CSS classes for styling.
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "e.g., Awesome Django Packages",
                }
            ),
            "url": forms.URLInput(
                attrs={
                    "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "https://example.com/resource",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "rows": 4,
                    "placeholder": "A brief note about why this resource is useful...",
                }
            ),
            "technology": forms.Select(
                attrs={
                    "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                }
            ),
            "categories": forms.SelectMultiple(
                attrs={
                    "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "size": 5,
                }
            ),
        }


class TechnologyForm(forms.ModelForm):
    """
    A ModelForm for creating and updating Technology objects.
    """

    class Meta:
        model = Technology
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "e.g., Python, React, etc.",
                }
            )
        }


class CategoryForm(forms.ModelForm):
    """
    A ModelForm for creating and updating Category objects.
    """

    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "e.g., Tutorial, Library, Tool",
                }
            )
        }
