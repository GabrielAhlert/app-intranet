from django.core.management.base import BaseCommand, CommandError
from agenda.models import Unidade, Funcao, Contato
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'r', encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    nome, funcao, unidade, nascimento, ramal, email, telefone = line.split(',')
                    ramal_ativo = True
                    pessoa_ativo = True
                    
                    if ramal == None or ramal == '':
                        ramal_ativo = False

                    if nascimento == None or nascimento == '':
                        pessoa_ativo = False
                    else:
                        nascimento = datetime.strptime(nascimento, '%d/%m/%Y').date()
                    
                    funcao, _ = Funcao.objects.get_or_create(nome=funcao)
                    unidade, _ = Unidade.objects.get_or_create(nome=unidade)
                    Contato.objects.update_or_create(nome=nome.title(), ramal=ramal, telefone=telefone, email=email, funcao=funcao, unidade=unidade, nascimento=nascimento, ramal_ativo=ramal_ativo, pessoa_ativo=pessoa_ativo)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))