from rest_framworks.serializers import ModelSerializer
from core.backend.models import Colecao

class ColecaoSerializer(ModelSerializer):
    class Meta:
        model = Colecao
        fields = '__all__'