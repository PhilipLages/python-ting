from ting_file_management.queue import Queue
from ting_file_management.file_process import create_file_info


def find_word_occurrences(lines, word):
    occurrences = []
    for line_number, line in enumerate(lines, start=1):
        if word.lower() in line.lower():
            occurrences.append({"linha": line_number})
    return occurrences


def exists_word(word, instance: Queue):
    all_occurrences = []
    for file_path in instance.queue:
        file_info = create_file_info(file_path)
        occurrences = find_word_occurrences(
            file_info["linhas_do_arquivo"], word
            )
        if occurrences:
            all_occurrences.append({
                "palavra": word,
                "arquivo": file_info["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return all_occurrences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
