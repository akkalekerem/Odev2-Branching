import pandas as pd

# CSV'den veri oku
df = pd.read_csv("data.csv")

# Ortalamayı hesapla
average_value = df["value"].mean()

print(f"Veri ortalaması: {average_value}")
