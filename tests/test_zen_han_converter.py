from zen_han_converter.zen_han_convter import ZenToHan, HanToZen


def test_ZenToHan():
    zen_to_han = ZenToHan()
    assert zen_to_han.convert('ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ') == 'abcdefghijklmnopqrstuvwxyz'
    assert zen_to_han.convert('abcdefghijklmnopqrstuvwxyz') == 'abcdefghijklmnopqrstuvwxyz'


def test_HanToZen():
    han_to_zen = HanToZen()
    assert han_to_zen.convert("abcdefghijklmnopqrstuvwxyz") == "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    assert han_to_zen.convert("ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ") == "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
