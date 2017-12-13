import os

from Utils.utils import log


def to_file(titles, file_path):
    with open(file_path, 'a') as f:
        for text in titles:
            try:
                f.write(text)
                f.flush()
            except Exception as ex:
                log(str(ex))
                continue


def remove_duplicates(file_path):
    uniq_lines = set(open(file_path).readlines())
    open(file_path, 'w').writelines(set(uniq_lines))


def create_file_if_not_exist(path):
    if not os.path.isfile(path):
        open(path, 'w').close()


def write_to_file_no_duplicates(path, elements):
    with (open(path, 'a')) as f1, (open(path, 'r')) as f2:
        for ele in elements:
            in_file = [line.strip() for line in f2.readlines()]
            # print("if %s not in %s " %(ele,list))
            if ele not in in_file:
                f1.write(ele + '\n')
            f2.seek(0)
