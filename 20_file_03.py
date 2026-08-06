# ========================================
print(f"\n{"=" * 40}\n")

import os
import sys
import csv

csv_path = os.path.join("data", "08_press.csv")

with open(csv_path, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["90:00", "PUMP-01"])
