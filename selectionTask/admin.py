from django.contrib import admin
from django.utils.encoding import smart_str
from models import AbstractTask, ConcreteTask, Subject, Result
from django.http import HttpResponse
import csv

admin.site.register(AbstractTask)
admin.site.register(ConcreteTask)
admin.site.register(Subject)


def export_csv(result, request, queryset):

    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=results.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"Subject ID"),
        smart_str(u"Task ID"),
        smart_str(u"First Card Flipped"),
        smart_str(u"Second Card Flipped"),
        smart_str(u"Third Card Flipped"),
        smart_str(u"Fourth Card Flipped"),

    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.subject),
            smart_str(obj.task),
            smart_str(obj.card_one_isflipped),
            smart_str(obj.card_two_isflipped),
            smart_str(obj.card_three_isflipped),
            smart_str(obj.card_four_isflipped),
        ])
    return response
export_csv.short_description = u"Export CSV"


class MyResultAdmin(admin.ModelAdmin):
    actions = [export_csv]

admin.site.register(Result, MyResultAdmin)