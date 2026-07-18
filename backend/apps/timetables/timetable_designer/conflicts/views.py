from rest_framework.views import APIView

from rest_framework.response import Response



class ConflictCheckView(
    APIView
):

    def get(
        self,
        request
    ):

        conflicts = []

        return Response(
            conflicts
        )
