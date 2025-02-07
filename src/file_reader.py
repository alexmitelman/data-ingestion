import csv

from config import settings


def read_csv_in_chunks():
    """Generator function that reads the latest CSV file in chunks."""
    csv_path = settings.CSV_FILE_PATH
    
    with csv_path.open(mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        batch = []

        for row in reader:
            batch.append(row)

            if len(batch) >= settings.CHUNK_SIZE:
                yield batch
                batch = []

        if batch:
            yield batch
