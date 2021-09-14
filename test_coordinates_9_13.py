# test_coordinates_9_13.py
def test_coordinateline():
    from coordinates_9_13 import coordinateline
    result = coordinateline(0,0,2,2,1)
    expected = 1
    assert result == expected