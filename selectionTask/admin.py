from django.contrib import admin
from django.utils.encoding import smart_str
from models import AbstractTask, ConcreteTask, Subject, Result
from django.http import HttpResponse
import csv

admin.site.register(AbstractTask)
admin.site.register(ConcreteTask)


def export_csv_results(result, request, queryset):

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
        temp1 = convert(obj.card_one_isflipped)
        temp2 = convert(obj.card_two_isflipped)
        temp3 = convert(obj.card_three_isflipped)
        temp4 = convert(obj.card_four_isflipped)
        writer.writerow([
            smart_str(obj.subject),
            smart_str(obj.task),
            smart_str(temp1),
            smart_str(temp2),
            smart_str(temp3),
            smart_str(temp4),
        ])
    return response
export_csv_results.short_description = u"Export CSV"


def export_csv_subjects(result, request, queryset):

    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=subjects.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"Subject ID"),
        smart_str(u"Group"),
    ])
    for obj in queryset:
        temp = convertGroup(obj.group)
        writer.writerow([
            smart_str(obj.subject_id),
            smart_str(temp),
        ])
    return response
export_csv_results.short_description = u"Export CSV"


def convert(boolean):
    if boolean == True:
        return "1"
    else:
        return "0"


def convertGroup(boolean):
    if boolean == True:
        return "Abstract"
    else:
        return "Concrete"


class MyResultAdmin(admin.ModelAdmin):
    actions = [export_csv_results]


class MySubjectAdmin(admin.ModelAdmin):
    actions = [export_csv_subjects]


admin.site.register(Result, MyResultAdmin)
admin.site.register(Subject, MySubjectAdmin)