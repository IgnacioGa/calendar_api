from events.models import Event
from events.serializers import CreateUpdateEventSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Event.objects.all()
    serializer_class = CreateUpdateEventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, pk=None):
        if self.request.user.pk != self.get_object().user.pk:
            return Response({'Method not Allowed because you are not the owner'}, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request)

    def destroy(self, request, *args, **kwargs):
        if request.user.pk != self.get_object().user.pk:
            return Response({'Method not Allowed because you are not the owner'}, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request)