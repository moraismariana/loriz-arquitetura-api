from django.contrib import admin
from django.urls import path, include

# pillow imagens
from django.conf import settings
from django.conf.urls.static import static

# viewsets, router e jwt authentication
from loriz.views import PaginaInicialTextoViewSet, PaginaInicialImagemViewSet, PaginaInicialBgViewSet, SobreTextoViewSet, SobreImagemViewSet, SobreBgViewSet, ServicosTextoViewSet, ServicosImagemViewSet, ServicosBgViewSet, ProjetosTextoViewSet, ProjetosImagemViewSet, ProjetosBgViewSet, ClientesTextoViewSet, ClientesBgViewSet, ContatoTextoViewSet, ContatoBgViewSet, ProjetoEspecificoViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router_loriz = routers.DefaultRouter()
router_loriz.register('paginainicialtexto', PaginaInicialTextoViewSet, basename='paginainicialtexto')
router_loriz.register('paginainicialimagem', PaginaInicialImagemViewSet, basename='paginainicialimagem')
router_loriz.register('paginainicialbg', PaginaInicialBgViewSet, basename='paginainicialbg')
router_loriz.register('sobretexto', SobreTextoViewSet, basename='sobretexto')
router_loriz.register('sobreimagem', SobreImagemViewSet, basename='sobreimagem')
router_loriz.register('sobrebg', SobreBgViewSet, basename='sobrebg')
router_loriz.register('servicostexto', ServicosTextoViewSet, basename='servicostexto')
router_loriz.register('servicosimagem', ServicosImagemViewSet, basename='servicosimagem')
router_loriz.register('servicosbg', ServicosBgViewSet, basename='servicosbg')
router_loriz.register('projetostexto', ProjetosTextoViewSet, basename='projetostexto')
router_loriz.register('projetosimagem', ProjetosImagemViewSet, basename='projetosimagem')
router_loriz.register('projetosbg', ProjetosBgViewSet, basename='projetosbg')
router_loriz.register('clientestexto', ClientesTextoViewSet, basename='clientestexto')
router_loriz.register('clientesbg', ClientesBgViewSet, basename='clientesbg')
router_loriz.register('contatotexto', ContatoTextoViewSet, basename='contatotexto')
router_loriz.register('contatobg', ContatoBgViewSet, basename='contatobg')
router_loriz.register('projetoespecifico', ProjetoEspecificoViewSet, basename='projetoespecifico')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router_loriz.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
