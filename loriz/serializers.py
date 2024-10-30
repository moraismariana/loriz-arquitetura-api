from rest_framework import serializers
from loriz.models import PaginaInicialTexto, PaginaInicialImagem, PaginaInicialBg, SobreTexto, SobreImagem, SobreBg, ServicosTexto, ServicosImagem, ServicosBg, ProjetosTexto, ProjetosImagem, ProjetosBg, ClientesTexto, ClientesBg, ContatoTexto, ContatoBg, ProjetoEspecifico
from loriz.mixins import DeleteOldImageSerializerMixin

class PaginaInicialTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaginaInicialTexto
        fields = '__all__'

class PaginaInicialImagemSerializer(DeleteOldImageSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = PaginaInicialImagem
        fields = '__all__'

class PaginaInicialBgSerializer(DeleteOldImageSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = PaginaInicialBg
        fields = '__all__'

class SobreTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SobreTexto
        fields = '__all__'

class SobreImagemSerializer(DeleteOldImageSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = SobreImagem
        fields = '__all__'

class SobreBgSerializer(DeleteOldImageSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = SobreBg
        fields = '__all__'

class ServicosTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicosTexto
        fields = '__all__'

class ServicosImagemSerializer(DeleteOldImageSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ServicosImagem
        fields = '__all__'

class ServicosBgSerializer(DeleteOldImageSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ServicosBg
        fields = '__all__'

class ProjetosTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetosTexto
        fields = '__all__'

class ProjetosImagemSerializer(DeleteOldImageSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ProjetosImagem
        fields = '__all__'

class ProjetosBgSerializer(DeleteOldImageSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ProjetosBg
        fields = '__all__'

class ClientesTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientesTexto
        fields = '__all__'

class ClientesBgSerializer(DeleteOldImageSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ClientesBg
        fields = '__all__'

class ContatoTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoTexto
        fields = '__all__'

class ContatoBgSerializer(DeleteOldImageSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ContatoBg
        fields = '__all__'

class ProjetoEspecificoSerializer(DeleteOldImageSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ProjetoEspecifico
        fields = '__all__'