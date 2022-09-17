from events.models import Event
from rest_framework.serializers import ModelSerializer
from users.serializers import CreateUserProfileSerializer



class CreateUpdateEventSerializer(ModelSerializer):
    user = CreateUserProfileSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'notes', 'start', 'end', 'user')
