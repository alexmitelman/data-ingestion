from db_writer import insert_records_to_db
from file_reader import read_csv_in_chunks
from processor import transform_and_validate_record


def process_csv():
    """Processes the entire CSV file in chunks."""
    for chunk in read_csv_in_chunks():
        records = [transform_and_validate_record(row) for row in chunk]
        insert_records_to_db(records)

if __name__ == "__main__":
    process_csv()
