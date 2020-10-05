import sample_platform
import sample_os
import logging

formatter = logging.Formatter(logging.BASIC_FORMAT)


def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def run():
    log = setup_logger('platform', '../log/platform.log')
    sample_platform.platform_info(log)

    log = setup_logger('os', '../log/os.log')
    sample_os.folder_info(log)


if __name__ == '__main__':
    run()
