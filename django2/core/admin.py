from django.contrib import admin

# Register your models here.
from .models import Produto


# vai aparecer no /admin
# DECORATOR QUE REGISTRA 'PRODUTO' NO /ADMIN
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # nome das variaveis criadas no MODELS
    list_display = ('nome',
                    'preco',
                    'estoque',
                    'slug',
                    'criado',
                    'modificado',
                    'ativo')
