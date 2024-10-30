from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from loriz.models import PaginaInicialTexto, PaginaInicialImagem, PaginaInicialBg, SobreTexto, SobreImagem, SobreBg, ServicosTexto, ServicosImagem, ServicosBg, ProjetosTexto, ProjetosImagem, ProjetosBg, ClientesTexto, ClientesBg, ContatoTexto, ContatoBg, ProjetoEspecifico

from loriz.serializers import PaginaInicialTextoSerializer, PaginaInicialImagemSerializer, PaginaInicialBgSerializer, SobreTextoSerializer, SobreImagemSerializer, SobreBgSerializer, ServicosTextoSerializer, ServicosImagemSerializer, ServicosBgSerializer, ProjetosTextoSerializer, ProjetosImagemSerializer, ProjetosBgSerializer, ClientesTextoSerializer, ClientesBgSerializer, ContatoTextoSerializer, ContatoBgSerializer, ProjetoEspecificoSerializer

class PermissaoLoriz(permissions.BasePermission):
    """
    Permissão personalizada para verificar se o usuário faz parte do grupo de editores.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Verifica se o usuário está no grupo 'Editores Loriz'
        return request.user.groups.filter(name='Editores Loriz').exists()

class PaginaInicialTextoViewSet(viewsets.ModelViewSet):
    queryset = PaginaInicialTexto.objects.all()
    serializer_class = PaginaInicialTextoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class PaginaInicialImagemViewSet(viewsets.ModelViewSet):
    queryset = PaginaInicialImagem.objects.all()
    serializer_class = PaginaInicialImagemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class PaginaInicialBgViewSet(viewsets.ModelViewSet):
    queryset = PaginaInicialBg.objects.all()
    serializer_class = PaginaInicialBgSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class SobreTextoViewSet(viewsets.ModelViewSet):
    queryset = SobreTexto.objects.all()
    serializer_class = SobreTextoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class SobreImagemViewSet(viewsets.ModelViewSet):
    queryset = SobreImagem.objects.all()
    serializer_class = SobreImagemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class SobreBgViewSet(viewsets.ModelViewSet):
    queryset = SobreBg.objects.all()
    serializer_class = SobreBgSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class ServicosTextoViewSet(viewsets.ModelViewSet):
    queryset = ServicosTexto.objects.all()
    serializer_class = ServicosTextoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class ServicosImagemViewSet(viewsets.ModelViewSet):
    queryset = ServicosImagem.objects.all()
    serializer_class = ServicosImagemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class ServicosBgViewSet(viewsets.ModelViewSet):
    queryset = ServicosBg.objects.all()
    serializer_class = ServicosBgSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class ProjetosTextoViewSet(viewsets.ModelViewSet):
    queryset = ProjetosTexto.objects.all()
    serializer_class = ProjetosTextoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class ProjetosImagemViewSet(viewsets.ModelViewSet):
    queryset = ProjetosImagem.objects.all()
    serializer_class = ProjetosImagemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class ProjetosBgViewSet(viewsets.ModelViewSet):
    queryset = ProjetosBg.objects.all()
    serializer_class = ProjetosBgSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class ClientesTextoViewSet(viewsets.ModelViewSet):
    queryset = ClientesTexto.objects.all()
    serializer_class = ClientesTextoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class ClientesBgViewSet(viewsets.ModelViewSet):
    queryset = ClientesBg.objects.all()
    serializer_class = ClientesBgSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class ContatoTextoViewSet(viewsets.ModelViewSet):
    queryset = ContatoTexto.objects.all()
    serializer_class = ContatoTextoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class ContatoBgViewSet(viewsets.ModelViewSet):
    queryset = ContatoBg.objects.all()
    serializer_class = ContatoBgSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]

class ProjetoEspecificoViewSet(viewsets.ModelViewSet):
    queryset = ProjetoEspecifico.objects.all()
    serializer_class = ProjetoEspecificoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoLoriz]
