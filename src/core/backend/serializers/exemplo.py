from core.backend.models import ModelExemplo
from rest_framework.serializers import ModelSerializer
from .state import StateSerializer

class AddressSerializer(ModelSerializer):
    state = StateSerializer()
    class Meta:
        model = Address
        fields = '__all__'