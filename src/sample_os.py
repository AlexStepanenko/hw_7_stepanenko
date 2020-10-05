import os


def folder_info(log):
    file_list = os.listdir('.')
    file_list.sort()
    log.info(file_list)

    return None
