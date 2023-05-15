import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    if path_file not in instance.queue:
        instance.enqueue(path_file)

        file = txt_importer(path_file)
        file_info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }

        sys.stdout.write(str(file_info))


def remove(instance: Queue):
    if instance.__len__() == 0:
        sys.stdout.write("Não há elementos\n")

    removed = instance.dequeue()
    if removed is not None:
        sys.stdout.write(f'Arquivo {removed} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
