# models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Technology(models.Model):
    """
    Represents a specific technology, e.g., 'Python', 'React', 'Docker'.
    This model stores the names of technologies that resources can be associated with.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Name of the technology (e.g., Python, React)",
    )

    def __str__(self):
        """String representation of the Technology object."""
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"


class Category(models.Model):
    """
    Represents a category to classify a resource, e.g., 'UI Component', 'Tutorial', 'Tool'.
    Resources can belong to multiple categories.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Name of the category (e.g., Tutorial, Library)",
    )

    def __str__(self):
        """String representation of the Category object."""
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Resource(models.Model):
    """
    Represents a saved resource, like a web link, an article, or a tool.
    This is the main model of the application.
    """

    """ user = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text="The user who saved this resource"
    ) """

    title = models.CharField(
        max_length=200, help_text="Descriptive title for the resource"
    )
    url = models.URLField(
        max_length=2000, help_text="The URL link to the resource", blank=True, null=True
    )
    description = models.TextField(
        help_text="Personal notes about why this resource was saved"
    )

    # Foreign Key to Technology: A resource is associated with one primary technology.
    # on_delete=models.SET_NULL means if a technology is deleted, the resource's technology field will be set to NULL,
    # instead of deleting the resource itself. `null=True` is required for this.
    technology = models.ForeignKey(
        Technology, on_delete=models.SET_NULL, null=True, blank=True
    )

    # ManyToManyField to Category: A resource can be assigned multiple categories.
    categories = models.ManyToManyField(Category)

    # DateTimeField to store the creation timestamp.
    # `default=timezone.now` automatically sets the current date and time when a new resource is created.
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """String representation of the Resource object."""
        return self.title

    class Meta:
        # Orders resources by creation date, with the newest appearing first.
        ordering = ["-created_at"]
