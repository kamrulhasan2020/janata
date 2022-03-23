import csv
import os
from .models import Trade

module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, "stock_market_data.csv")


def load():
    Trade.objects.all().delete()
    with open(file_path) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                _, created = Trade.objects.get_or_create(
                    date=row[0],
                    trade_code=row[1],
                    high=float(row[2].replace(",", "")),
                    low=float(row[3].replace(",", "")),
                    open=float(row[4].replace(",", "")),
                    close=float(row[5].replace(",", "")),
                    volume=float(row[6].replace(",", "")),
                )
            except ValueError:
                continue

    return "ok"

