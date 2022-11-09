from django.db import models
# biblioteca para salvar imagens
from stdimage.models import StdImageField

# Create your models here.
# SIGNALS
# tarefa realizada ANTES ou DEPOIS de armazenar/deletar/atualizar no banco
from django.db.models import signals
# SLUGI pega o nome e coloca traço = pega-o-nome-e-faz-isso
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateTimeField('Data de Crianção', auto_now_add=True)
    modificado = models.DateTimeField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo ?', default=True)

    class Meta:
        abstract: True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    #IMPORTADO
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


# funçao que sera relaizada no SIGNAL
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


# o SIGNAL, Executa no PRE-SAVE quando Produto for salvo.
# antes de salvarm o signal é chamado executando a funlçao.
signals.pre_save.connect(produto_pre_save, sender=Produto)

