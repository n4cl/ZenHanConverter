from zen_han_converter.zen_han_converter import ZenHan


def test_ZenHan():
    zen_to_han = ZenHan(alphabet_zen_to_han=True,
                        number_zen_to_han=True,
                        ascii_symbol_zen_to_han=True,
                        space_zen_to_han=True)
    assert zen_to_han.convert('ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ') == 'abcdefghijklmnopqrstuvwxyz'
    assert zen_to_han.convert('abcdefghijklmnopqrstuvwxyz') == 'abcdefghijklmnopqrstuvwxyz'
    assert zen_to_han.convert('０１２３４５６７８９') == '0123456789'
    assert zen_to_han.convert('0123456789') == '0123456789'
    assert zen_to_han.convert("！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～") == "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    assert zen_to_han.convert("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~") == "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    assert zen_to_han.convert("　") == " "
    assert zen_to_han.convert(" ") == " "

    han_to_zen = ZenHan(alphabet_han_to_zen=True,
                        number_han_to_zen=True,
                        ascii_symbol_han_to_zen=True,
                        space_han_to_zen=True)
    assert han_to_zen.convert("abcdefghijklmnopqrstuvwxyz") == "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    assert han_to_zen.convert("ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ") == "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    assert han_to_zen.convert("0123456789") == "０１２３４５６７８９"
    assert han_to_zen.convert("０１２３４５６７８９") == "０１２３４５６７８９"
    assert han_to_zen.convert("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~") == "！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～"
    assert han_to_zen.convert("！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～") == "！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～"
    assert han_to_zen.convert(" ") == "　"
    assert han_to_zen.convert("　") == "　"
