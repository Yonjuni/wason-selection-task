from django.contrib import admin
from django.utils.encoding import smart_str
from models import AbstractTask, ConcreteTask, Subject, Result
from django.http import HttpResponse
import csv


def export_csv_results(result, request, queryset):

    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=results.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"Subject ID"),
        smart_str(u"Task ID"),
        smart_str(u"1st Card Flipped"),
        smart_str(u"2nd Card Flipped"),
        smart_str(u"3rd Card Flipped"),
        smart_str(u"4th Card Flipped"),
        smart_str(u"Time (Millisec)"),

    ])
    for obj in queryset:
        temp1 = convert(obj.first_card_flipped)
        temp2 = convert(obj.second_card_flipped)
        temp3 = convert(obj.third_card_flipped)
        temp4 = convert(obj.fourth_card_flipped)
        writer.writerow([
            smart_str(obj.subject),
            smart_str(obj.task),
            smart_str(temp1),
            smart_str(temp2),
            smart_str(temp3),
            smart_str(temp4),
            smart_str(obj.time),
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
    list_display = ('subject', 'task', 'first_card_flipped', 'second_card_flipped', 'third_card_flipped', 'fourth_card_flipped', 'time')


class MySubjectAdmin(admin.ModelAdmin):
    actions = [export_csv_subjects]
    list_display = ('subject_id', 'group')


class MyTaskAdmin(admin.ModelAdmin):
    fields = ('description', ('first_card', 'first_card_should_flip'), ('second_card', 'second_card_should_flip'),
              ('third_card', 'third_card_should_flip'), ('fourth_card', 'fourth_card_should_flip'), 'story'
    )


admin.site.register(Result, MyResultAdmin)
admin.site.register(Subject, MySubjectAdmin)
admin.site.register(AbstractTask, MyTaskAdmin)
admin.site.register(ConcreteTask, MyTaskAdmin)