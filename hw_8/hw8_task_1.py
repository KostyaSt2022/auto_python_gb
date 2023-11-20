"""
Задача по обходу и анализу файловой системы.
Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию и все
вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.
Каждый результат должен содержать следующую информацию:
Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория.
Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах.
Важные детали:
Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
Для файлов сохраните их размер в байтах.
Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся
внутри данной директории, ивложенных директорий.

Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.

Для обхода файловой системы вы можете использовать модуль os.

Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и
возвращать результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных файлах
(JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
"""


# import json
# import csv
# import pickle
# import os
#
#
# def get_directory_size(path):
#     """
#     Функция для получения размера директории или файла в байтах.
#     """
#     if os.path.isfile(path):
#         return os.path.getsize(path)
#
#     elif os.path.isdir(path):
#         total_size = 0
#         for dirpath, dirnames, filenames in os.walk(path):
#             for filename in filenames:
#                 filepath = os.path.join(dirpath, filename)
#                 total_size += os.path.getsize(filepath)
#         return total_size
#
#
# def get_directory_info(path):
#     """
#     Функция для получения информации о директории и всех ее файлов и директориях.
#     """
#     results = []
#     for root, dirs, files in os.walk(path):
#         dirname = os.path.basename(root)
#         dirsize = get_directory_size(root)
#         results.append({
#             'name': dirname,
#             'type': 'directory',
#             'size': dirsize,
#             'parent_directory': os.path.dirname(root),
#         })
#
#         for file in files:
#             filepath = os.path.join(root, file)
#             filesize = get_directory_size(filepath)
#             results.append({
#                 'name': file,
#                 'type': 'file',
#                 'size': filesize,
#                 'parent_directory': os.path.dirname(filepath),
#             })
#
#     return results
#
#
# def save_results_to_json(results, output_file):
#     """
#     Функция для сохранения результатов в формате JSON.
#     """
#     with open(output_file, 'w') as f:
#         json.dump(results, f, indent=4)
#
#
# def save_results_to_csv(results, output_file):
#     """
#     Функция для сохранения результатов в формате CSV.
#     """
#     fieldnames = ['name', 'type', 'size', 'parent_directory']
#     with open(output_file, 'w', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(results)
#
#
# def save_results_to_pickle(results, output_file):
#     """
#     Функция для сохранения результатов в формате Pickle.
#     """
#     with open(output_file, 'wb') as f:
#         pickle.dump(results, f)
#
#
# def traverse_directory(path):
#     """
#     Функция для обхода заданной директории и сохранения результатов.
#     """
#     results = get_directory_info(path)
#
#     json_output_file = 'output.json'
#     save_results_to_json(results, json_output_file)
#     print(f'Результат сохранен в {json_output_file}')
#
#     csv_output_file = 'output.csv'
#     save_results_to_csv(results, csv_output_file)
#     print(f'Результат сохранен в {csv_output_file}')
#
#     pickle_output_file = 'output.pickle'
#     save_results_to_pickle(results, pickle_output_file)
#     print(f'Результат сохранен в {pickle_output_file}')
#
#
# traverse_directory('D:/deep_python/auto_python_gb')
# # get_directory_info('D:/deep_python/auto_python_gb')





"""
Решение от ГБ:
"""
import os
import json
import csv
import pickle


def get_dir_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_dir_size(dp)
    return total_size


def save_results_to_json(results, file_name):
    with open(file_name, 'w') as f:
        json.dump(results, f)


def save_results_to_csv(results, file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path', 'Type', 'Size'])
        for result in results:
            writer.writerow([result['Path'], result['Type'], result['Size']])


def save_results_to_pickle(results, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(results, f)


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results


print(traverse_directory('D:/deep_python/auto_python_gb'))