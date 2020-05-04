import django_filters
from .models import Trail

class TrailFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Crescator'),
        ('descending', 'Descrescator')
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')
    
    class Meta:
        model = Trail
        fields = ('region', 'difficulty')

    def filter_by_order(self, queryset, name, value):
        expression = 'date' if value == 'ascending' else '-date'
        return queryset.order_by(expression)
