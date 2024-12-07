# type: ignore

from rest_framework.viewsets import ModelViewSet
from .models import Team
from .serializers import TeamSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def create(self, request, *args, **kwargs):
        titles = request.data.get("titles", None)
        first_cup = request.data.get("first_cup", None)

        if titles is not None and int(titles) < 0:
            return Response(
                {"error": "titles cannot be negative"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if first_cup is not None:
            try:
                first_cup_date = datetime.strptime(first_cup, "%Y-%m-%d")
            except ValueError:
                return Response(
                    {"error": "first_cup must be in the format YYYY-MM-DD"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if first_cup_date.year < 1930:
                return Response(
                    {"error": "there was no world cup this year"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if (first_cup_date.year - 1930) % 4 != 0:
                return Response(
                    {"error": "there was no world cup this year"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if first_cup_date.year < datetime.now().year:
                played_cups = (datetime.now().year - first_cup_date.year) // 4

                if datetime.now().year % 4 == 2:
                    played_cups += 1

                titles = request.data.get("titles", None)

                if not titles <= played_cups:
                    return Response(
                        {"error": "impossible to have more titles than disputed cups"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def destroy(self, request, *args, **kwargs):
        try:
            team = self.get_object()
        except Exception:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        try:
            team = self.get_object()
        except Exception:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(team)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            team = self.get_object()
        except Exception:
            return Response(
                {"message": "Team not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().update(request, *args, **kwargs)
