from django.urls import path
from . import views


app_name = "resourcehub"

urlpatterns = [
    path("", views.HomeView.as_view(), name="dashboard"),
    path("resources/", views.ResourceListView.as_view(), name="resources"),
    path(
        "resources/create/", views.ResourceCreateView.as_view(), name="create_resource"
    ),
    path(
        "resources/<int:pk>/update/",
        views.ResourceUpdateView.as_view(),
        name="update_resource",
    ),
    path(
        "resources/<int:pk>/delete/",
        views.ResourceDeleteView.as_view(),
        name="delete_resource",
    ),
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path(
        "categories/create/", views.CategoryCreateView.as_view(), name="create_category"
    ),
    path(
        "categories/<int:pk>/delete/",
        views.CategoryDeleteView.as_view(),
        name="delete_category",
    ),
    path(
        "categories/<int:pk>/update/",
        views.CategoryUpdateView.as_view(),
        name="update_category",
    ),
    path("technologies/", views.TechnologyListView.as_view(), name="technologies"),
    path(
        "technologies/create/",
        views.TechnologyCreateView.as_view(),
        name="create_technology",
    ),
    path(
        "technologies/<int:pk>/delete/",
        views.TechnologyDeleteView.as_view(),
        name="delete_technology",
    ),
    path(
        "technologies/<int:pk>/update/",
        views.TechnologyUpdateView.as_view(),
        name="update_technology",
    ),
]
