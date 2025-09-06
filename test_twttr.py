from twttr import shorten

def test_shorten():
    
    assert shorten("word") == "wrd"
    assert shorten("WORD") == "WRD"
    assert shorten("word1") == "wrd1"
    assert shorten("word,") == "wrd,"
