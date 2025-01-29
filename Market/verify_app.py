import os
import zipfile

from django.core.exceptions import ValidationError

# Função de verificação após o post do app
def verify_app(app_instance):
    """
    Verifica se o app postado atende aos requisitos necessários para ser publicado.
    Se aprovado, altera o status do app.
    """
    try:
        # Requisito 1: Nome deve ter pelo menos 3 caracteres
        if len(app_instance.nome) < 3:
            raise ValidationError("O nome do aplicativo deve ter pelo menos 3 caracteres.")
        
        # Requisito 2: Descrição obrigatória
        if not app_instance.descricao:
            raise ValidationError("A descrição do aplicativo é obrigatória.")
        
        # Requisito 3: Verificar se o arquivo zip foi carregado
        if not app_instance.zip_file:
            raise ValidationError("É necessário enviar um arquivo compactado válido.")


        # Verificação da arquitetura do app Django dentro do arquivo ZIP
        zip_path = app_instance.zip_file.path  # Caminho do arquivo ZIP no servidor
        
        if not os.path.exists(zip_path):
            raise ValidationError("O arquivo zip fornecido não existe ou não pôde ser encontrado.")

        # Verificar se a pasta ZIP contém os arquivos essenciais do Django
        required_files = [
            'urls.py',
            'models.py',
            'views.py',
            'admin.py',
            '__init__.py',
            'migrations'
        ]

        # Abrindo o arquivo zip para verificar seu conteúdo
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_files = zip_ref.namelist()

            # Verificando se todos os arquivos essenciais estão presentes
            missing_files = [file for file in required_files if file not in zip_files]

            if missing_files:
                raise ValidationError(f"Arquitetura do app está incompleta. Arquivos faltando: {', '.join(missing_files)}")

        # Se todos os requisitos forem passados, altera o status para aprovado
        app_instance.status = 'aprovado'
        app_instance.save()

        return True  # Se aprovado
    except ValidationError as e:
        # Caso algum requisito não seja atendido, altera o status para rejeitado e retorna a mensagem
        app_instance.status = 'Negado'
        app_instance.save()
        return str(e)  # Retorna a mensagem de erro para mostrar ao usuário

