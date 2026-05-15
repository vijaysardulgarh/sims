import csv



def export_to_csv(response, queryset):

    writer = csv.writer(response)

    writer.writerow(["Student", "Total", "Paid", "Due"])

    for item in queryset:

        writer.writerow([
            item.student,
            item.total_amount,
            item.paid_amount,
            item.due_amount,
        ])

    return response