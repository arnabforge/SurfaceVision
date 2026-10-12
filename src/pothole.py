def create_pothole_record(
    pothole_id,
    confidence,
    severity,
    bounding_box
):
    """Create a structured pothole detection record."""

    pothole = {
        "id": pothole_id,
        "confidence": confidence,
        "severity": severity,
        "bounding_box": bounding_box,
    }

    return pothole