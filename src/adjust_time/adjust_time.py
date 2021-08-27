from datetime import datetime
from datetime import timedelta

def adjust_date(time_str: str, delta: int) -> str:
    """deltaを計算した日付を返す
    """
    if delta >= 0:
        calculated_time = datetime.strptime(time_str, "%Y-%m-%d") + timedelta(days=delta)
        return datetime.strftime(calculated_time, "%Y-%m-%d")
    elif delta < 0:
        calculated_time = datetime.strptime(time_str, "%Y-%m-%d") + timedelta(days=delta)
        return datetime.strftime(calculated_time, "%Y-%m-%d")

if __name__ == "__main__":
    print(adjust_time("2018-10-01", 1))