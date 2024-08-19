import sys
from collections import Counter


def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r") as fl:
            logs = fl.readlines()
    except FileExistsError:
        print("The file path isn't exists")
    logs = [parse_log_line(log) for log in logs]
    return logs


def parse_log_line(line: str) -> dict:
    parsed_log_line = line.split(" ")
    # assign all needed values
    date, time, log_lvl, *info = parsed_log_line
    # make massage readble
    massage = ' '.join(info)
    log_obj = {
        "Date": date,
        "Time": time,
        "Lvl": log_lvl,
        "Massage": massage.strip(),
    }
    return log_obj


def filter_logs_by_level(logs: list[dict[str]], level: str) -> None:
    # filter needed logs which user want
    logs = list(filter(lambda x: x["Lvl"] == level, logs))
    print(f"Detail of Level '{level}'")
    # Display them
    for log in logs:
        print(f"{log['Date']} {log['Time']} - {log['Massage']}")


def count_logs_by_level(logs: list) -> dict:
    # making dict with information about logs quantity
    log_counter = Counter(log["Lvl"] for log in logs)
    return log_counter


def display_log_counts(counts: dict):
    print(
        f"""
Рівень логування | Кількість
-----------------|----------
INFO             | {counts['INFO']}
DEBUG            | {counts['DEBUG']}
ERROR            | {counts['ERROR']}
WARNING          | {counts['WARNING']}     
          """
    )


def main():
    if len(sys.argv) == 1:
        print("you didn't pass enough arguments")
    else:
        file_path, *log_type = sys.argv[1:]

        if not file_path.endswith('.log'):
            print('Incorrect log file format')
            return
        if log_type[0].upper() not in ['INFO',
                                       'DEBUG',
                                       'ERROR',
                                       'WARNING', ]:
            print('None Log Level type')
            return
        # Open file and pull data from the file
        # Create dict to store logs
        log_list = load_logs(file_path=file_path)
        # we count quantity of each type of log
        counts = count_logs_by_level(log_list)
        # Display
        display_log_counts(counts)
        # if logs_type we use filter logs
        if log_type:
            filter_logs_by_level(log_list, log_type[0].upper())


if __name__ == "__main__":
    main()
