"""
Функция группового переименования файлов.
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории
Пример использования.

На входе:
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

На выходе:
new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc,
new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc
"""


import os


def rename_files(dir_path: str,
                 new_name: str = '',
                 count: int = 3,
                 in_extension: str = 'txt',
                 out_extension: str = 'txt',
                 slice_name: tuple = (0, 0)):
    if not os.path.isdir(dir_path):
        return False
    file_list = os.listdir(dir_path)
    files_count = 1
    for cur_file in file_list:
        cur_name, cur_ext = cur_file.split('.')
        if cur_ext == in_extension:
            new_file = ''
            if slice_name:
                new_file += f'{cur_name[slice_name[0]:slice_name[1]]}'
            if new_name:
                new_file += f'{new_name}'
            new_file += f'_{files_count:0>{count}}.{out_extension}'
            os.rename(os.path.join(dir_path, cur_file),
                      os.path.join(dir_path, new_file))
            files_count += 1
    return f'{files_count} файл(а/ов) переименован(ы) по шаблону ' \
           f'"old_name[{slice_name[0]}:{slice_name[1]}]{new_name}_{"X" * int(f"{count}")}.{out_extension}"'


print(rename_files('test_folder', new_name='NewSuper', count=3, in_extension='txt',
                   out_extension='doc', slice_name=(5, 30)))