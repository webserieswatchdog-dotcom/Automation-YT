from src.metadata_generator import generate_metadata


def test_generate_metadata():
    result = generate_metadata("AI")

    assert "title" in result
    assert "description" in result
    assert "tags" in result
