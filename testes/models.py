from django.db import models


class Teste(models.Model):
    TIPOS_TESTE = [
        ('mensagem_universo', 'Descubra a Mensagem Oculta do Universo Para Você'),
        ('dom_espiritual', 'Qual é o Seu Dom Espiritual Escondido?'),
        ('milagre', 'Que Milagre Está Prestes a Acontecer na Sua Vida?'),
        ('guia_espiritual', 'Qual é o Seu Guia Espiritual e o Que Ele Quer Te Dizer?'),
        ('energia_mistica', 'Que Energia Mística Você Atrai?'),
    ]
    
    tipo = models.CharField(max_length=50, choices=TIPOS_TESTE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    icone = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Testes"
    
    def __str__(self):
        return self.titulo


class Resposta(models.Model):
    teste = models.ForeignKey(Teste, on_delete=models.CASCADE)
    email = models.EmailField()
    respostas = models.JSONField()
    resultado_preview = models.TextField()
    resultado_completo = models.TextField()
    pago = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Respostas"
    
    def __str__(self):
        return f"{self.email} - {self.teste.titulo}"
