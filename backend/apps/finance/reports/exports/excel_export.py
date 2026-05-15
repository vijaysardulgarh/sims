import pandas as pd



def export_to_excel(queryset):

    data = list(queryset.values())

    dataframe = pd.DataFrame(data)

    return dataframe