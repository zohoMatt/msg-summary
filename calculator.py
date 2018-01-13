def time_minus(bigger, smaller):
    return 0


def check_waiting_time(user, data):
    return 0


def normalize_records(lines):
    return 0


def begin_calculation(file_path):
    rfile = open(file_path, 'r', encoding='utf-8')
    lines = rfile.readlines()
    normalized = normalize_records(lines)
    my_waiting = check_waiting_time('我', normalized)
    pp_waiting = check_waiting_time('pp', normalized)
    print('我的等待时间：{0}小时\nPP等待时间：{1}小时'.format(my_waiting, pp_waiting))

begin_calculation('msg_records.txt')
