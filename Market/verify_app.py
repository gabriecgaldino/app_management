import os
import zipfile
from django.core.exceptions import ValidationError

def verify_app(app_instance):
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

        zip_path = app_instance.zip_file.path
        
        # Verificação do arquivo zip
        if not os.path.exists(zip_path):
            raise ValidationError("O arquivo zip fornecido não existe ou não pôde ser encontrado.")

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_files = zip_ref.namelist()
            
            # Normalizando os caminhos dos arquivos e verificando se eles existem na lista
            required_files = [
                'models.py',
                'views.py',
                'admin.py',
                '__init__.py',
            ]
            
            # Verificar se os arquivos necessários existem na lista
            missing_files = [file for file in required_files if not any(file in f for f in zip_files)]
            
            if missing_files:
                raise ValidationError(f"Arquitetura do app está incompleta. Arquivos faltando: {', '.join(missing_files)}")

        # Atualizar o status para 'Aprovado' se tudo estiver correto
        app_instance.status = 'Aprovado'
        app_instance.save()  # Salvar a alteração no banco de dados

        return True  # Retorna True se o app for aprovado

    except ValidationError as e:
        # Caso algum requisito não seja atendido, atualiza o status para 'Negado' e retorna a mensagem de erro
        app_instance.status = 'Negado'
        app_instance.save()  # Salvar a alteração no banco de dados
        return str(e)  # Retorna a mensagem de erro para mostrar ao usuário
