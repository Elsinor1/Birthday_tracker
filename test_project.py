import pytest
from project import days_to_birthday, nearest_birthday, validate_contact
from datetime import date


def test_days_to_birthday():
    test_date = str(date.today().month) + "/" + str((date.today().day + 5))
    assert days_to_birthday(test_date) == 5
    test_date = str(date.today().month) + "/" + str((date.today().day - 1))
    assert days_to_birthday(test_date) == 365
    with pytest.raises(ValueError):
        days_to_birthday("13/32")
        days_to_birthday(15)


def test_nearest_birthday():
    assert nearest_birthday(
        {"Martin": "1/17", "Lenka": "4/14", "Tim": "08/02"}) == "Martin"
    with pytest.raises(ValueError):
        nearest_birthday({"Martin": "13/32", "Lenka": "4/14"})
        nearest_birthday({"Martin": "13/32", "+": "4/14"})
        nearest_birthday({"Martin": 15, "Lenka": "4/14"})


def test_validate_contact():
    assert validate_contact("Martin", "Luther", "08/18",
                            "martin.luther@gmail.com") == True
    assert validate_contact("Martin", "", "8/1", "martin@gmail.com") == True

    assert validate_contact("Martin-Gus", "", "8/1",
                            "martin@gmail.com") == False
    assert validate_contact("", "Martin", "8/1", "martin@gmail.com") == False
    assert validate_contact("Martin", "", "18/1", "martin@gmail.com") == False
    assert validate_contact("Martin", "", "8/32", "martin@gmail.com") == False
    assert validate_contact("Martin", "", "8/1", "martin.gmail.com") == False
    assert validate_contact("Martin", "+-", "8/1", "martin@gmail.com") == False
    assert validate_contact("Martin", "", 1, "martin@gmail.com") == False
    assert validate_contact(0, "", "8/1", "martin@gmail.com") == False
    assert validate_contact("Martin", 0, "8/1", "martin@gmail.com") == False
    assert validate_contact("Martin", "", "8/1", 0) == False
