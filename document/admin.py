from django.contrib import admin
from document.models import Document
# Register your models here.


admin.site.register(Document)

class DocumentAdmin(admin.ModelAdmin):
    change_list_template = 'admin/document_summary_change_list.html'
    date_hierachy = 'created'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except(AttributeError, KeyError):
            return response

        metrics = {
            'total' : Count('id'),
            'total_documents': Sum('documents'),
        }

        response.context_data['summary'] = list(
            qs
            .values('document__category__name')
            .annotate(**metrics)
            .order_by('-total_documents')
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )

        list_filter = (
            'documents',
        )

        summary_over_time = qs.annotate(
            period=Trunc(
                'created',
                'day',
                output_field=DateTimeField(),
            ),
        ).values('period')
        #.annotate(total=Sum('document'))
        #.order_by('period')

        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)

        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total' : x['total'] or 0,
            #'pct': \ 
            #   ((x['total'] or 0) - low) / (high- low) * 100
            #   if high > low else 0,

        } for x in summary_over_time]

        return response



