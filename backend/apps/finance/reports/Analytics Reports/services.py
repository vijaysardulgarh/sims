from .charts import monthly_collection_chart



def monthly_collection_chart_service():

    chart = monthly_collection_chart()

    return {
        "results": chart
    }