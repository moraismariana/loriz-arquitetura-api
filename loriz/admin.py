from django.contrib import admin
from loriz.models import PaginaInicialTexto, PaginaInicialImagem, PaginaInicialBg, SobreTexto, SobreImagem, SobreBg, ServicosTexto, ServicosImagem, ServicosBg, ProjetosTexto, ProjetosImagem, ProjetosBg, ClientesTexto, ClientesBg, ContatoTexto, ContatoBg, ProjetoEspecifico

class PaginaInicialTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class PaginaInicialImagemAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class PaginaInicialBgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class SobreTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class SobreImagemAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class SobreBgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class ServicosTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class ServicosImagemAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class ServicosBgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class ProjetosTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class ProjetosImagemAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class ProjetosBgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class ClientesTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class ClientesBgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class ContatoTextoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class ContatoBgAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    
class ProjetoEspecificoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

admin.site.register(PaginaInicialTexto, PaginaInicialTextoAdmin)

admin.site.register(PaginaInicialImagem, PaginaInicialImagemAdmin)

admin.site.register(PaginaInicialBg, PaginaInicialBgAdmin)

admin.site.register(SobreTexto, SobreTextoAdmin)

admin.site.register(SobreImagem, SobreImagemAdmin)

admin.site.register(SobreBg, SobreBgAdmin)

admin.site.register(ServicosTexto, ServicosTextoAdmin)

admin.site.register(ServicosImagem, ServicosImagemAdmin)

admin.site.register(ServicosBg, ServicosBgAdmin)

admin.site.register(ProjetosTexto, ProjetosTextoAdmin)

admin.site.register(ProjetosImagem, ProjetosImagemAdmin)

admin.site.register(ProjetosBg, ProjetosBgAdmin)

admin.site.register(ClientesTexto, ClientesTextoAdmin)

admin.site.register(ClientesBg, ClientesBgAdmin)

admin.site.register(ContatoTexto, ContatoTextoAdmin)

admin.site.register(ContatoBg, ContatoBgAdmin)

admin.site.register(ProjetoEspecifico, ProjetoEspecificoAdmin)
