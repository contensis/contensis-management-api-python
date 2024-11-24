"""Confirm that the LowerKeyDict class works as expected."""

from contensis_management import lower_key_dict


def test_lower_key_dict():
    """Make sure the LowerKeyDict class works as expected."""
    # Arrange
    original_dict = {
        "Key1": "Value1",
        "KEY2": "Value2",
        "NesTed": {
            "KEy3": "Value3",
            "Key4": "Value4",
        },
    }
    # Act
    new_dict = lower_key_dict.to_lower_key_dict(original_dict)
    # Assert
    assert new_dict["key1"] == "Value1"
    assert new_dict["key2"] == "Value2"
    assert new_dict["nested"]["key3"] == "Value3"
    assert new_dict["nested"]["key4"] == "Value4"
