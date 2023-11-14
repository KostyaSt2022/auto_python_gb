"""
Информация о файле.
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
Пример использования.

На входе:
file_path = "C:/Users/User/Documents/example.txt"

На выходе:
('C:/Users/User/Documents/', 'example', '.txt')
"""

file_path = "D:/deep_python/auto_python_gb/hw_5/hw5_task_1.py"


# def get_file_info(full_path: str):
#     def divine(abs_path: str, div: str) -> tuple:
#         abs_path = abs_path.split(div)
#         file_name, extension = abs_path[-1].split('.')
#         path = div.join(abs_path[:-1])
#         return path, file_name, extension
#
#     return divine(full_path, '/') if '/' in full_path else divine(full_path, '\\')
#
#
# print(get_file_info(file_path))



# Идеал от GB:
def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)

print(get_file_info(file_path))