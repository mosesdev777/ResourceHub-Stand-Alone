from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Q
from datetime import timedelta
from .models import Resource, Category, Technology
from .forms import ResourceForm, CategoryForm, TechnologyForm

from django.views.generic import (
    TemplateView,
    ListView,
    DeleteView,
    UpdateView,
    CreateView,
)

# Create your views here.


class HomeView(TemplateView):
    template_name = "resourcehub/dashboard.html"

    def get_context_data(self, **kwargs):
        """
        This method is used to gather all the data that will be sent to the template.
        It's the standard way to add context to a Class-Based View.
        """
        # First, call the base implementation to get the initial context.
        context = super().get_context_data(**kwargs)

        # --- Statistics Calculation ---
        # The same logic from the function-based view is now here.

        # 1. Total count of all saved resources.
        total_resources = Resource.objects.count()

        # 2. Total count of unique technologies.
        total_technologies = Technology.objects.count()

        # 3. Total count of unique categories.
        total_categories = Category.objects.count()

        # 4. Count of new resources added in the last 30 days.
        thirty_days_ago = timezone.now() - timedelta(days=30)
        new_resources_last_30_days = Resource.objects.filter(
            created_at__gte=thirty_days_ago
        ).count()

        # --- Update Context ---
        # We add our calculated statistics to the context dictionary.
        # Using context.update() is a clean way to add multiple items.
        context.update(
            {
                "total_resources": total_resources,
                "total_technologies": total_technologies,
                "total_categories": total_categories,
                "new_resources_last_30_days": new_resources_last_30_days,
                "section": "dashboard",
                # Optional: for highlighting the active link
            }
        )

        # Finally, return the updated context.
        return context


class ResourceListView(ListView):
    """
    A Class-Based View to display a list of resources.
    It handles filtering by search query, technology, and category.
    """

    # 1. Specify the model to use.
    model = Resource

    # 2. Specify the template to render.
    template_name = "resourcehub/resources/index.html"  # Make sure this path is correct for your project

    # 3. Set the name for the list of objects in the template's context.
    #    This will allow us to loop through {% for resource in resource_list %}
    context_object_name = "resources"

    # 4. (Optional but recommended) Enable pagination.
    #    This will show 9 resources per page.
    paginate_by = 6

    def get_queryset(self):
        """
        Override the default queryset to implement search and filtering logic.
        This method is called to get the list of objects that this view will display.
        """
        # Start with all resources, ordered by the newest first.
        queryset = super().get_queryset().order_by("-created_at")

        # Get filter parameters from the URL's query string (e.g., ?search=...&technology=1)
        search_query = self.request.GET.get("search", None)
        technology_id = self.request.GET.get("technology", None)
        category_id = self.request.GET.get("category", None)

        # Apply search filter if a search_query is provided.
        if search_query:
            # Use Q objects to create a complex query with an OR condition.
            # This will find resources where the search_query appears in either the title OR the description.
            # `icontains` makes the search case-insensitive.
            queryset = queryset.filter(
                Q(title__icontains=search_query)
                | Q(description__icontains=search_query)
            )

        # Apply technology filter if a technology_id is provided and is not empty.
        if technology_id:
            queryset = queryset.filter(technology_id=technology_id)

        # Apply category filter if a category_id is provided and is not empty.
        if category_id:
            # `categories__id` is how you filter based on a field in a ManyToMany relationship.
            queryset = queryset.filter(categories__id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Override to add extra context data needed for the template,
        such as the list of all technologies and categories for the filter dropdowns.
        """
        # Call the base implementation first to get the default context.
        context = super().get_context_data(**kwargs)

        # Add the list of all technologies and categories to the context.
        context["all_technologies"] = Technology.objects.all()
        context["all_categories"] = Category.objects.all()

        # Add the section identifier for the active sidebar link.
        context["section"] = "resources"

        return context


class ResourceCreateView(CreateView):
    """
    A Class-Based View for creating a new Resource instance.
    """

    # 1. Specify the model to create.
    model = Resource

    # 2. Specify the form class to use for validation and rendering.
    form_class = ResourceForm

    # 3. Specify the template to render.
    template_name = "resourcehub/resources/create.html"  # The template you already have

    # 4. Define the URL to redirect to after a successful form submission.
    #    reverse_lazy is used here because the URLs are not loaded when the file is imported.
    #    It redirects to the 'resource_list' page (you need to name this URL in urls.py).
    success_url = reverse_lazy("resourcehub:resources")

    def get_context_data(self, **kwargs):
        """
        Add extra context data for the template.
        """
        context = super().get_context_data(**kwargs)
        # Add the section identifier for the active sidebar link
        context["section"] = "add_resource"
        return context

    def form_valid(self, form):
        """
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        You can add logic here before the object is saved, for example,
        to associate the resource with the logged-in user.
        """
        # For now, we'll just let the parent class handle saving.
        # Later, you could do something like:
        # form.instance.user = self.request.user
        return super().form_valid(form)


class ResourceUpdateView(UpdateView):
    """
    A Class-Based View for updating an existing Resource instance.
    """

    # 1. Specify the model to work with.
    #    UpdateView will automatically fetch the object based on the 'pk' from the URL.
    model = Resource

    # 2. Specify the form class, which we can reuse from the create view.
    form_class = ResourceForm

    # 3. Specify the template to render. We can reuse the same form template.
    template_name = "resourcehub/resources/update.html"

    context_object_name = "resource"

    # 4. Define the URL to redirect to after a successful update.
    #    It redirects to the list view, so the user can see their changes reflected.
    success_url = reverse_lazy("resourcehub:resources")

    def get_context_data(self, **kwargs):
        """
        Add extra context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context["section"] = "resources"
        # We don't set a 'section' here, as this is not a main navigation link,
        # but a sub-page. The sidebar will not have an active item, which is fine.
        return context

    def form_valid(self, form):
        """
        This method is called when valid form data has been POSTed.
        You can add custom logic here before saving the changes.
        """
        # For example, you could log who updated the resource.
        # print(f"Resource '{form.instance.title}' updated by user {self.request.user}")
        return super().form_valid(form)


class ResourceDeleteView(DeleteView):
    """
    A Class-Based View for deleting a Resource instance.
    This view handles the POST request sent from the confirmation modal.
    """

    # 1. Specify the model to work with.
    #    DeleteView will automatically fetch the object based on the 'pk'
    #    passed in the URL.
    model = Resource

    # 2. Define the URL to redirect to after a successful deletion.
    #    After deleting, the user will be sent back to the resource list.
    success_url = reverse_lazy("resourcehub:resources")

    template_name = "resourcehub/resources/delete.html"

    def get_context_data(self, **kwargs):
        """
        Add extra context data for the template if needed.
        """
        context = super().get_context_data(**kwargs)
        # We don't need to set a 'section' here, as this is a confirmation
        # page, not a main navigation item.
        return context


class CategoryListView(ListView):
    """
    Displays a list of all categories.
    """

    model = Category
    # We now point to a specific template for categories.
    template_name = "resourcehub/categories/index.html"

    # Use a more descriptive name for the object list in the template context.
    context_object_name = "categories"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """
        Add extra context data for the template.
        """
        context = super().get_context_data(**kwargs)
        # This is for the active sidebar link logic.
        context["section"] = "categories"
        context["form"] = CategoryForm()
        return context


class CategoryCreateView(CreateView):

    model = Category
    form_class = CategoryForm
    template_name = "resourcehub/categories/category-form.html"
    success_url = reverse_lazy("resourcehub:categories")


class CategoryDeleteView(DeleteView):
    """
    Handles deleting a category after confirmation from a dedicated page.
    """

    model = Category
    # The template that will be rendered on a GET request.
    template_name = "resourcehub/categories/delete.html"
    # The URL to redirect to after the object is successfully deleted.
    success_url = reverse_lazy("resourcehub:categories")

    def get_context_data(self, **kwargs):
        """
        Add extra context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context["section"] = "categories"
        return context


class CategoryUpdateView(UpdateView):
    """
    Handles updating an existing category.
    """

    model = Category
    form_class = CategoryForm
    # We can reuse the same form template from the create view.
    template_name = "resourcehub/categories/update.html"
    success_url = reverse_lazy("resourcehub:categories")

    def get_context_data(self, **kwargs):
        """
        Add extra context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context["section"] = "categories"
        return context


class TechnologyListView(ListView):
    """
    Displays a list of all categories.
    """

    model = Technology
    # We now point to a specific template for categories.
    template_name = "resourcehub/technologies/index.html"

    # Use a more descriptive name for the object list in the template context.
    context_object_name = "technologies"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """
        Add extra context data for the template.
        """
        context = super().get_context_data(**kwargs)
        # This is for the active sidebar link logic.
        context["section"] = "technologies"
        context["form"] = TechnologyForm()
        return context


class TechnologyCreateView(CreateView):

    model = Technology
    form_class = TechnologyForm
    template_name = "resourcehub/technologies/create.html"
    success_url = reverse_lazy("resourcehub:technologies")


class TechnologyDeleteView(DeleteView):
    """
    Handles deleting a category after confirmation from a dedicated page.
    """

    model = Technology
    # The template that will be rendered on a GET request.
    template_name = "resourcehub/technologies/delete.html"
    # The URL to redirect to after the object is successfully deleted.
    success_url = reverse_lazy("resourcehub:technologies")

    def get_context_data(self, **kwargs):
        """
        Add extra context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context["section"] = "technologies"
        return context


class TechnologyUpdateView(UpdateView):
    """
    Handles updating an existing category.
    """

    model = Technology
    form_class = TechnologyForm
    # We can reuse the same form template from the create view.
    template_name = "resourcehub/technologies/update.html"
    success_url = reverse_lazy("resourcehub:technologies")

    def get_context_data(self, **kwargs):
        """
        Add extra context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context["section"] = "technologies"
        return context
