with open('./input.txt', 'r') as file:
    reports = file.readlines()

reports = [report.strip() for report in reports]
total_safe_reports = 0

print("total reports: ", len(reports))


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
    print("-----------------------\ncurrent report is: ", levels_list)
    is_valid = isValidReport(levels_list)

    if (not is_valid):
        print("not valid as it is. Lets try breaking it down.")
        for x in range(len(levels_list)):
            print("removing ", levels_list[x], " now.")
            mod_list = levels_list[:x] + levels_list[x+1:]
            print("modlist: ", mod_list)
            if mod_list in all_mod_lists:
                print("same hi aagya macho")
                continue

            new_report_valid = isValidReport(mod_list)
            if new_report_valid:
                print("removing ", levels_list[x], " from ", levels_list,
                      " makes it ", mod_list, " which is valid.\nAdding +1")
                total_safe_reports += 1
                print("safe reports until now: ", total_safe_reports)
                all_mod_lists.append(mod_list)
                break
            else:
                print("still not valid.")
                print("Count: ", total_safe_reports)

    if is_valid:
        print("its valid as it is.")
        total_safe_reports += 1
        print("count: ", total_safe_reports)
        continue

print(total_safe_reports)
