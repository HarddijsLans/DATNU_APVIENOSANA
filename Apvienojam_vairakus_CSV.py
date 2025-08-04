import pandas as pd
import glob
import os
import shutil
from datetime import datetime

# Ceļš uz CSV failiem
csv_path = "C:\\Users\\hardijslans\\Desktop\\VISUAL STUDIO CODE\\LADP\\*.csv"
csv_files = glob.glob(csv_path)

# Mape, kur saglabāt apvienoto failu
apvienotais_cels = "C:\\Users\\hardijslans\\Desktop\\VISUAL STUDIO CODE\\LADP\\Apvienoti"
os.makedirs(apvienotais_cels, exist_ok=True)

# Mape, uz kuru pārvietot apstrādātos failus
arhiva_mape = "C:\\Users\\hardijslans\\Desktop\\VISUAL STUDIO CODE\\LADP\\apstrādāti"
os.makedirs(arhiva_mape, exist_ok=True)

# Iegūst šodienas datumu formātā YYYY-MM-DD
sodienas_datums = datetime.today().strftime('%Y-%m-%d')

dfs = []

for f in csv_files:
    try:
        df = pd.read_csv(f, encoding='utf-8')
        dfs.append(df)
        print(f"[✓] Nolasīts: {os.path.basename(f)}")
    except Exception as e:
        print(f"[!] Kļūda nolasot failu {os.path.basename(f)}: {e}")

if dfs:
    df_apvienots = pd.concat(dfs, ignore_index=True)
    
    # Izveido pilnu ceļu uz izvadfailu ar datumu nosaukumā
    faila_nosaukums = f"VZD_atvērtie_dati_MSTR_{sodienas_datums}.csv"
    izvada_fails = os.path.join(apvienotais_cels, faila_nosaukums)
    df_apvienots.to_csv(izvada_fails, index=False)

    print(f"\n✅ Dati veiksmīgi apvienoti un saglabāti kā: {faila_nosaukums}")
    print(f"📁 Saglabāšanas vieta: {izvada_fails}")

    # Pārvieto oriģinālos CSV failus uz arhīva mapi
    for f in csv_files:
        try:
            shutil.move(f, arhiva_mape)
            print(f"[📂] Pārvietots uz 'apstrādāti': {os.path.basename(f)}")
        except Exception as e:
            print(f"[!] Neizdevās pārvietot {os.path.basename(f)}: {e}")

    print("\n📦 Visi CSV faili pārvietoti uz 'apstrādāti' mapi.")
else:
    print("\n⚠️ Neizdevās apvienot datus – netika nolasīts neviens derīgs CSV fails.")

    print("\n⚠️ Neizdevās apvienot datus – netika nolasīts neviens derīgs CSV fails.")