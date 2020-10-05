import platform


def platform_info(log):
    log.info(f'Version           : #{platform.python_version()}')
    log.info(f'Version tuple     : #{platform.python_version_tuple()}')
    log.info(f'Compiler          : #{platform.python_compiler()}')
    log.info(f'Build             : #{platform.python_build()}')

    log.info(f'System            : #{platform.system()}')
    log.info(f'Node              : #{platform.node()}')
    log.info(f'Release           : #{platform.release()}')
    log.info(f'Version           : #{platform.version()}')
    log.info(f'Machine           : #{platform.machine()}')
    log.info(f'Processor         : #{platform.processor()}')

    log.info(f'Interpreter       : #{platform.architecture()}')

    return None
