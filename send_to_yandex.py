import yadisk
import config


y = yadisk.YaDisk(token=config.DISK_TOKEN)
def send_csv_to_yandex(name_file: str):
    y.upload(f"{str(name_file)}", f"program_testing/{str(name_file)}", timeout=500)
