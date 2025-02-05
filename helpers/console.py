class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def write_to_console(message, color):
    print(color + message + BColors.ENDC)

def print_deeplinks(deeplinks, only_applinks):
    for activity, handlers in deeplinks.items():
        write_to_console(f'\n{activity}\n', BColors.BOLD)
        for deeplink in sorted(handlers.keys()):
            is_applink = deeplink.startswith('http')
            if not only_applinks or is_applink:
                write_to_console(deeplink, BColors.OKGREEN)
