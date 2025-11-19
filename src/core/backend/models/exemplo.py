from django.db import models

class ModelExemplo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.nome} - {"Ativo" if self.ativo else "Inativo"}'
    
    class Meta:
        verbose_name = "Modelo Exemplo"
        verbose_name_plural = "Modelos Exemplo"
        ordering = ['-criado_em']