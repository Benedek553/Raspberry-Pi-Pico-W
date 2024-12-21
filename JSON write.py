import ujson

# A JSON fájl neve
json_file_name = "data.json"

# Adatok, amelyeket el akarunk menteni
data_to_save = {
    "name": "89",
    "age": 30,
    "city": "Budapest"
}

try:
    # JSON fájl megnyitása írásra
    with open(json_file_name, "w") as file:
        # Adatok mentése JSON formátumban
        ujson.dump(data_to_save, file)

    print(f"Az adatok sikeresen mentve a {json_file_name} fájlba.")

except OSError:
    print(f"Hiba: Nem sikerült megnyitni a {json_file_name} fájlt írásra.")
