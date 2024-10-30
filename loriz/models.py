from django.db import models
from loriz.mixins import DeleteOldImageMixin

# Página Inicial
class PaginaInicialTexto(models.Model):
    inicio_titulo = models.TextField()
    inicio_descricao = models.TextField()
    inicio_link = models.TextField()
    servicos_titulo = models.TextField()
    servico1_titulo = models.TextField()
    servico1_descricao = models.TextField()
    servico2_titulo = models.TextField()
    servico2_descricao = models.TextField()
    servico3_titulo = models.TextField()
    servico3_descricao = models.TextField()
    depoimento_titulo = models.TextField()
    depoimento_texto = models.TextField()
    depoimento_cliente = models.TextField()
    depoimento_link = models.TextField()
    projetos_titulo = models.TextField()
    projetos_texto = models.TextField()
    projetos_link = models.TextField()
    mapa_endereco1 = models.TextField()
    mapa_endereco2 = models.TextField()

class PaginaInicialImagem(DeleteOldImageMixin, models.Model):
    servicos_imagem1 = models.ImageField(upload_to='loriz', blank=True)
    servicos_imagem2 = models.ImageField(upload_to='loriz', blank=True)
    servicos_imagem3 = models.ImageField(upload_to='loriz', blank=True)

class PaginaInicialBg(DeleteOldImageMixin, models.Model):
    introducao_bg = models.ImageField(upload_to='loriz', blank=True)
    projetos_bg = models.ImageField(upload_to='loriz', blank=True)

# Sobre
class SobreTexto(models.Model):
    titulo = models.TextField()
    texto = models.TextField()
    frase1 = models.TextField()
    frase1_autor = models.TextField()
    frase2 = models.TextField()
    frase2_autor = models.TextField()

class SobreImagem(DeleteOldImageMixin, models.Model):
    imagem1 = models.ImageField(upload_to='loriz', blank=True)
    imagem2 = models.ImageField(upload_to='loriz', blank=True)

class SobreBg(DeleteOldImageMixin, models.Model):
    bg = models.ImageField(upload_to='loriz', blank=True)

# Serviços
class ServicosTexto(models.Model):
    titulo = models.TextField()
    servico1_titulo = models.TextField()
    servico1_texto = models.TextField()
    servico2_titulo = models.TextField()
    servico2_texto = models.TextField()
    servico3_titulo = models.TextField()
    servico3_texto = models.TextField()

class ServicosImagem(DeleteOldImageMixin, models.Model):
    imagem1 = models.ImageField(upload_to='loriz', blank=True)
    imagem2 = models.ImageField(upload_to='loriz', blank=True)
    imagem3 = models.ImageField(upload_to='loriz', blank=True)

class ServicosBg(DeleteOldImageMixin, models.Model):
    bg = models.ImageField(upload_to='loriz', blank=True)

# Projetos
class ProjetosTexto(models.Model):
    titulo = models.TextField()
    projeto1 = models.TextField()
    projeto2 = models.TextField()
    projeto3 = models.TextField()
    projeto4 = models.TextField()
    projeto5 = models.TextField()
    projeto6 = models.TextField()
    projeto7 = models.TextField()
    projeto8 = models.TextField()
    projeto9 = models.TextField()
    projeto10 = models.TextField()
    projeto11 = models.TextField()
    projeto12 = models.TextField()

class ProjetosImagem(DeleteOldImageMixin, models.Model):
    imagem1 = models.ImageField(upload_to='loriz', blank=True)
    imagem2 = models.ImageField(upload_to='loriz', blank=True)
    imagem3 = models.ImageField(upload_to='loriz', blank=True)
    imagem4 = models.ImageField(upload_to='loriz', blank=True)
    imagem5 = models.ImageField(upload_to='loriz', blank=True)
    imagem6 = models.ImageField(upload_to='loriz', blank=True)
    imagem7 = models.ImageField(upload_to='loriz', blank=True)
    imagem8 = models.ImageField(upload_to='loriz', blank=True)
    imagem9 = models.ImageField(upload_to='loriz', blank=True)
    imagem10 = models.ImageField(upload_to='loriz', blank=True)
    imagem11 = models.ImageField(upload_to='loriz', blank=True)
    imagem12 = models.ImageField(upload_to='loriz', blank=True)

class ProjetosBg(DeleteOldImageMixin, models.Model):
    bg = models.ImageField(upload_to='loriz', blank=True)

# Clientes
class ClientesTexto(models.Model):
    titulo = models.TextField()
    cliente1_texto = models.TextField()
    cliente1_nome = models.TextField()
    cliente2_texto = models.TextField()
    cliente2_nome = models.TextField()
    cliente3_texto = models.TextField()
    cliente3_nome = models.TextField()
    cliente4_texto = models.TextField()
    cliente4_nome = models.TextField()
    cliente5_texto = models.TextField()
    cliente5_nome = models.TextField()
    cliente6_texto = models.TextField()
    cliente6_nome = models.TextField()

class ClientesBg(DeleteOldImageMixin, models.Model):
    bg = models.ImageField(upload_to='loriz', blank=True)

# Contato
class ContatoTexto(models.Model):
    titulo = models.TextField()
    whatsapp = models.TextField()
    email = models.TextField()
    telefone = models.TextField()
    mapa_endereco1 = models.TextField()
    mapa_endereco2 = models.TextField()

class ContatoBg(DeleteOldImageMixin, models.Model):
    bg = models.ImageField(upload_to='loriz', blank=True)

# Projeto Específico
class ProjetoEspecifico(DeleteOldImageMixin, models.Model):
    titulo = models.TextField()
    imagem = models.ImageField(upload_to='loriz', blank=True)
    descricao = models.TextField()



