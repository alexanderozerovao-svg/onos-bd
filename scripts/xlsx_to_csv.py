print("SCRIPT PATH:", __file__)
from pathlib import Path
import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Usage: python3 xlsx_to_csv.py <filename.xlsx>")
    sys.exit(1)

filename = sys.argv[1]

SRC = Path("data/raw") / filename
OUT = Path("data/out") / filename.replace(".xlsx", ".csv")
OUT.parent.mkdir(parents=True, exist_ok=True)

if not SRC.exists():
    print(f"File not found: {SRC}")
    sys.exit(1)

df = pd.read_excel(SRC, sheet_name=0)
df.columns = [str(c).strip().lower() for c in df.columns]

for c in ["datgr", "makedate", "data_ogo"]:
    if c in df.columns:
        df[c] = pd.to_datetime(df[c], errors="coerce").dt.date

df.to_csv(OUT, index=False, encoding="utf-8", sep=",")

print(f"OK: {OUT}")
print(f"Rows: {len(df)}  Columns: {len(df.columns)}")
