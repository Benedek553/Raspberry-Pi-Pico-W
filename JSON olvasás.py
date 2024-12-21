import ujson

# A JSON fájl neve
json_file_name = "wifi.json"

try:
    # JSON fájl megnyitása olvasásra
    with open(json_file_name, "r") as file:
        # JSON tartalom betöltése
        data = ujson.load(file)

    # Tartalom kiírása
    print("A JSON fájl tartalma:")
    for key, value in data.items():
        print(f"{key}: {value}")

except OSError:
    print(f"Hiba: Nem sikerült megnyitni a {json_file_name} fájlt.")
except ValueError:
    print("Hiba: A JSON fájl formátuma hibás.")
