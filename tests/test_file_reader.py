from src.file_reader import read_csv_in_chunks


def test_first_chunk_content():
    """Test that the first chunk contains the correct records."""
    chunk_generator = read_csv_in_chunks()
    first_chunk = next(chunk_generator)

    # Validate the first record in the chunk
    assert len(first_chunk) == 10_000
    assert "COLLISION_ID" in first_chunk[0]
    assert first_chunk[0]["COLLISION_ID"].isdigit()

def test_second_chunk_content():
    """Test that the second chunk contains the correct records."""
    chunk_generator = read_csv_in_chunks()
    next(chunk_generator)
    second_chunk = next(chunk_generator)

    assert len(second_chunk) == 10_000
    assert "COLLISION_ID" in second_chunk[0]
    