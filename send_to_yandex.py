import yadisk
from dotenv import dotenv_values
env_dict = dotenv_values('.env')

DISK_TOKEN: str = str(env_dict["DISK_TOKEN"])
y = yadisk.YaDisk(token=DISK_TOKEN)
def send_csv_to_yandex(name_file: str):
    y.upload(f"{str(name_file)}", f"monitoring_csv/{str(name_file)}", timeout=500)
