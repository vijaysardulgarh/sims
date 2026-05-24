from rest_framework.exceptions import (
    APIException
)


class BadRequestException(
    APIException
):

    status_code = 400

    default_detail = "Bad request."

    default_code = "bad_request"


class PermissionDeniedException(
    APIException
):

    status_code = 403

    default_detail = "Permission denied."

    default_code = "permission_denied"