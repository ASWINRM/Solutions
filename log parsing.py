def compare_two_date_times(dt1, dt2):
    """
    Arguments: 
        dt1 - A list of the following form:- [date, time]
        dt2 - A list of the following form:- [date, time]
    
    Returns:
        True/False. If dt1 occurs before dt2, returns True, else returns False 
    """

    dd1 = int(dt1[0][:2])
    monn1 = int(dt1[0][3:5])
    yy1 = int(dt1[0][6:])
    hh1 = int(dt1[1][:2])
    mm1 = int(dt1[1][3:5])
    ss1 = int(dt1[1][6:])

    dd2 = int(dt2[0][:2])
    monn2 = int(dt2[0][3:5])
    yy2 = int(dt2[0][6:])
    hh2 = int(dt2[1][:2])
    mm2 = int(dt2[1][3:5])
    ss2 = int(dt2[1][6:])

    if yy1 < yy2:
        return True
    elif yy2 < yy1:
        return False

    if monn1 < monn2:
        return True
    elif monn1 > monn2:
        return False

    if dd1 < dd2:
        return True
    if dd1 > dd2:
        return False

    if hh1 < hh2:
        return True
    if hh1 > hh2:
        return False

    if mm1 < mm2:
        return True
    if mm1 > mm2:
        return False

    if ss1 < ss2:
        return True
    if ss1 > ss2:
        return False

    return True


def is_valid_return_code(log):
    cnt_double_inverted_commas = 0
    pos = -1
    for i in range(len(log)):
        if log[i] == '"':
            cnt_double_inverted_commas += 1
        if cnt_double_inverted_commas == 2:
            pos = i
            break

    pos += 2
    return_code = 0
    while log[pos] >= "0" and log[pos] <= "9":
        return_code = 10 * return_code + int(log[pos])
        pos += 1

    if (return_code >= 400) and (return_code <= 599):
        return False
    return True


def is_inside_interval(log, time_interval):
    i = 0
    while log[i] != "[":
        i += 1
    i += 1

    log_date = ""
    log_time = ""

    while log[i] != ":":
        log_date += log[i]
        i += 1

    i += 1
    while log[i] != "]":
        log_time += log[i]
        i += 1

    if compare_two_date_times(
        time_interval[:2], [log_date, log_time]
    ) and compare_two_date_times([log_date, log_time], time_interval[2:]):
        return True
    return False


def solve(logs_list, time_interval):
    ans = 0
    for i in range(len(logs_list)):
        if is_valid_return_code(logs_list[i]) and is_inside_interval(
            logs_list[i], time_interval
        ):
            ans += 1

    return ans


def solver():
    n = int(input())
    ans = 0
    logs_list = []
    while n > 0:
        s = input()
        logs_list.append(s)
        n -= 1

    t = input()
    time_interval = t.split(" ")
    print(solve(logs_list=logs_list, time_interval=time_interval))


solver()
