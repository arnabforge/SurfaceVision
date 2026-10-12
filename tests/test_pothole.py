from src.pothole import create_pothole_record


def test_create_pothole_record():
    pothole = create_pothole_record(
        pothole_id=1,
        confidence=0.94,
        severity="High",
        bounding_box=[120, 80, 250, 190],
    )

    assert pothole["id"] == 1
    assert pothole["confidence"] == 0.94
    assert pothole["severity"] == "High"
    assert pothole["bounding_box"] == [120, 80, 250, 190]


if __name__ == "__main__":
    test_create_pothole_record()
    print("All pothole record checks passed!")