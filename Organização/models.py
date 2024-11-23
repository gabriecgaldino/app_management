from django.db import models

class Empresa(models.Model):
    razao_social = models.CharField("Razão Social", max_length=100)
    nome_fantasia = models.CharField("Nome Fantasia", max_length=100)
    cnpj = models.CharField("CNPJ", max_length=14, unique=True)
    ie = models.CharField("Inscrição Estadual", max_length=9, blank=True, null=True)
    im = models.CharField("Inscrição Municipal", max_length=11, blank=True, null=True)
    endereco = models.CharField("Endereço", max_length=100)
    telefone = models.CharField("Telefone", max_length=11, blank=True, null=True)
    email = models.EmailField("E-mail", max_length=50)
    type_organizacao = models.CharField(
        "Tipo de Organização",
        max_length=50,
        choices=[
            ("Matriz", "Matriz"),
            ("Filial", "Filial"),
        ],
    )

    def __str__(self):
        return self.nome_fantasia
