from django_distill import distill_path
from blog import views

urlpatterns = [
    distill_path('', views.index, name='index'),  # Replace views.index with your home view
    # Add distill_path for any other static views
]