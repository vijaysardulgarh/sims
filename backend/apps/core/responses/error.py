from rest_framework.response import (
    Response
)


def error_response(

    errors=None,

    message="Error",

    status_code=400
):

    return Response({

        "success": False,

        "message": message,

        "errors": errors
    },
    status=status_code)