with open('./input.txt', 'r') as file:
    reports = file.readlines()

reports = [report.strip() for report in reports]
total_safe_reports = 0


def isValidPair(num1, num2):
    diff = abs(num1-num2)
    return 1 <= diff <= 3


def isValidReport(report_list):
    ascending = all(report_list[x+1] > report_list[x] and isValidPair(report_list[x+1], report_list[x])
                    for x in range(len(report_list) - 1))
    descending = all(report_list[x] > report_list[x+1] and isValidPair(report_list[x+1], report_list[x])
                     for x in range(len(report_list) - 1))
    if (ascending or descending):
        return True
    else:
        return False


all_mod_lists = []


for report in reports:
    valid = False
    levels_list = [int(level) for level in report.split(" ")]
    is_valid = isValidReport(levels_list)

    if (not is_valid):
        for x in range(len(levels_list)):
            mod_list = levels_list[:x] + levels_list[x+1:]
            if mod_list in all_mod_lists:
                continue

            new_report_valid = isValidReport(mod_list)
            if new_report_valid:
                total_safe_reports += 1
                all_mod_lists.append(mod_list)
                break

    if is_valid:
        total_safe_reports += 1
        continue

print(total_safe_reports)
