import yadisk
import config


y = yadisk.YaDisk(token=config.DISK_TOKEN)

def get_all_dirs() -> list:
    """
    :return: list of all dirs
    """
    y.mkdir("simple_data_collector")
    return list(i.name for i in y.listdir(""))

def send_csv_to_yandex(name_file: str):
    dirs = get_all_dirs()
    if "simple_data_collector" not in dirs:
        y.mkdir("simple_data_collector")
    y.upload(f"{str(name_file)}", f"simple_data_collector/{str(name_file)}", timeout=500)

