import csv

with open("./input/graduacao-unb.csv", encoding="utf-8") as csv_file:
    unb_csv = csv.DictReader(csv_file)

    knowledge_areas = {}

    for row in unb_csv:
        current_area = row["area_conhecimento"]
        current_shift = row["turno"]

        if current_area not in knowledge_areas:
            knowledge_areas[current_area] = {"n": 0, "da": 0, "t": 0}

        if current_shift == "Noturno":
            knowledge_areas[current_area]["n"] += 1

        if current_shift == "Matutino e Vespertino":
            knowledge_areas[current_area]["da"] += 1

        knowledge_areas[current_area]["t"] += 1

with open("./output/report-unb.csv", mode="w", encoding="utf-8") as csv_file:
    headers = ["KNOWLEDGE_AREA", "NIGHT", "DAY_AND_AFTERNOON", "TOTAL"]
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()

    for area, data in knowledge_areas.items():
        row = {"KNOWLEDGE_AREA": area, "NIGHT": data["n"], "DAY_AND_AFTERNOON": data["da"], "TOTAL": data["t"]}
        writer.writerow(row)
