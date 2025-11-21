from rest_framework.seriliazers import Modelserializer
from core.backend.models import CategoriaAcervo

class CategoriaAcervoSerializer(Modelserializer):
    class Meta:
        model = CategoriaAcervo
        fields = '__all__'
        