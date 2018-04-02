import os

from os.path import isfile, join


def to_file(titles, file_path):
    with open(file_path, 'a') as f:
        for text in titles:
            try:
                f.write(text)
                f.flush()
            except Exception as ex:
                print(ex)
                continue


def remove_duplicates(file_path):
    unique_lines = set(open(file_path).readlines())
    open(file_path, 'w').writelines(set(unique_lines))


def create_file_if_not_exist(path):
    if not os.path.isfile(path):
        open(path, 'w').close()


def write_to_file_no_duplicates(path, elements):
    with open(path, 'a') as f1, open(path, 'r') as f2:
        for ele in elements:
            in_file = [line.strip() for line in f2.readlines()]
            if ele not in in_file:
                f1.write(ele + '\n')
            f2.seek(0)


def combine_files(count, file_path, folder_path, prefix):
    file_names = [folder_path + "%s%s.txt" % (prefix, str(i)) for i in range(1, count + 1)]
    with open(file_path, 'w') as outfile:
        for fname in file_names:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)


def combine_all_files(folder_path, output_file):
    files = [f for f in os.listdir(folder_path) if isfile(join(folder_path, f))]
    with open(output_file, 'w') as outfile:
        for fname in files:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)


def remove_files(files):
    for file in files:
        os.remove(file)
