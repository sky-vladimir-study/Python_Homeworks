from StringUtils import StringUtils
import pytest


strig_utils = StringUtils()


def test_capitalize():
    assert strig_utils.capitilize("skypro") == "Skypro"
    assert strig_utils.capitilize("vladimir") == "Vladimir"


def test_capitalize_negative():
    assert strig_utils.capitilize("123") == "123"
    assert strig_utils.capitilize("") == ""
    assert strig_utils.capitilize(" ") == " "


def test_trim():
    assert strig_utils.trim("   skypro") == "skypro"
    assert strig_utils.trim("   Vladimir") == "Vladimir"
    assert strig_utils.trim("Vladimir") == "Vladimir"
    assert strig_utils.trim("Vladimir ") == "Vladimir "
    assert strig_utils.trim("   123") == "123"
    assert strig_utils.trim("    ") == ""
    assert strig_utils.trim("   ") == ""
    assert strig_utils.trim(" sky pro ") == "sky pro "


def test_trim_negative():
    assert strig_utils.trim("") == ""
    assert strig_utils.trim("!@#$%^&*") == "!@#$%^&*"


def test_to_list():
     assert strig_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
     assert strig_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
     assert strig_utils.to_list("!:0:.", ":") == ["!", "0", "."]
     assert strig_utils.to_list("1$2$3", "$") == ["1", "2", "3"]
     assert strig_utils.to_list("v$l$a$d", "$") == ["v", "l", "a", "d"]
     assert strig_utils.to_list("v l a d", " ") == ["v", "l", "a", "d"]
     assert strig_utils.to_list("H,e,l,l,o,!", ",") == ["H", "e", "l", "l", "o", "!"]
     assert strig_utils.to_list("H.e.l.l.o.!", ".") == ["H", "e", "l", "l", "o", "!"]


def test_to_list_negative():
    assert strig_utils.to_list(" ::-", ":") == [" ", "", "-"]


def test_contains():
     assert strig_utils.contains("SkyPro", "S") == True
     assert strig_utils.contains("SkyPro", "U") == False
     assert strig_utils.contains("SkyPro", "k") == True
     assert strig_utils.contains("SkyPro", "P") == True
     assert strig_utils.contains("SkyPro!", "!") == True


def test_contains_negative():
    assert strig_utils.contains(" ", " ") == True
    assert strig_utils.contains("", "") == True
    assert strig_utils.contains("", "!") == False


def test_delete_symbol():
    assert strig_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert strig_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert strig_utils.delete_symbol("skypro", "kypr") == "so"
    assert strig_utils.delete_symbol(" SkyPro", " Sky") == "Pro"
    assert strig_utils.delete_symbol("123SkyPro", "23Sky") == "1Pro"
    assert strig_utils.delete_symbol("!SkyPro$$", "!Sky") == "Pro$$"


def test_delete_symbol_negative():
    assert strig_utils.delete_symbol(" ", " ") == ""
    assert strig_utils.delete_symbol(". ", " ") == "."
    assert strig_utils.delete_symbol("123456", "123") == "456"
    assert strig_utils.delete_symbol("1234567890", "2345") == "167890"


@pytest.mark.parametrize("input_string, input_symbol, result",
[
("SkyPro", "S", True),
("SkyPro", "M", False),
(" SkyPro", " ", True),
]
)
def test_starts_with(input_string, input_symbol, result):
    assert strig_utils.starts_with(input_string, input_symbol) == result


@pytest.mark.parametrize(
"input_string, input_symbol, result",
[
("", "", True),
(".", " ", False),
("!", "!", True),
(" ", " ", True),
]
)
def test_starts_with_negative(input_string, input_symbol, result):
    assert strig_utils.starts_with(input_string, input_symbol) == result


def test_end_with():
    assert strig_utils.end_with("SkyPro", "o") == True
    assert strig_utils.end_with("SkyPro", "y") == False
    assert strig_utils.end_with("Vladimir", "r") == True
    assert strig_utils.end_with("Vladimir123", "3") == True
    assert strig_utils.end_with("Vladimir ", " ") == True


def test_end_with_negative():
    assert strig_utils.end_with("!@#$%^&*(", "(") == True
    assert strig_utils.end_with("", "") == True
    assert strig_utils.end_with("@#$%^", "#") == False
    assert strig_utils.end_with("12345", "1") == False


def test_is_empty():
    assert strig_utils.is_empty("") == True


def test_is_empty_negative():
    assert strig_utils.is_empty(" ") == True
    assert strig_utils.is_empty("      ") == True
    assert strig_utils.is_empty("123456") == False
    assert strig_utils.is_empty("!@#$%^&") == False
    assert strig_utils.is_empty(" V ") == False
    assert strig_utils.is_empty(" . ") == False
    assert strig_utils.is_empty("Vladimir") == False
    assert strig_utils.is_empty(" Vladimir") == False


def test_list_to_string():
    assert strig_utils.list_to_string([0,1,2,3,4]) == "0, 1, 2, 3, 4"
    assert strig_utils.list_to_string([-1,-2,-3,-4]) == "-1, -2, -3, -4"
    assert strig_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert strig_utils.list_to_string([0,1,2,3,4], ".") == "0.1.2.3.4"
    assert strig_utils.list_to_string(["Hello", "World!"]) == "Hello, World!"
    assert strig_utils.list_to_string(["12345", "67890"]) == "12345, 67890"
    assert strig_utils.list_to_string(["когда", "нибудь"], "-") == "когда-нибудь"
    assert strig_utils.list_to_string(["world", "earth"], "/") == "world/earth"


def test_list_to_string_negative():
    assert strig_utils.list_to_string(["", ""], "-") == "-"
    assert strig_utils.list_to_string([".", "."], "_") == "._."
