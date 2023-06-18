from han_to_zen_table import LATIN_ALPHABET as HAN2ZEN_LATIN_ALPHABET
from zen_to_han_table import LATIN_ALPHABET as ZEN2HAN_LATIN_ALPHABET


class BaseConverter:
    """
    コンバーターの基底クラス
    """
    def __init__(self, latain_alphabet_table):
        self.latain_alphabet_table = str.maketrans(latain_alphabet_table)

    def convert(self, text):
        """
        変換する
        """
        return text.translate(self.latain_alphabet_table)


class ZenToHan(BaseConverter):
    """
    全角を半角に変換するクラス
    """
    def __init__(self):
        super().__init__(ZEN2HAN_LATIN_ALPHABET)


class HanToZen(BaseConverter):
    """
    半角を全角に変換するクラス
    """
    def __init__(self):
        super().__init__(HAN2ZEN_LATIN_ALPHABET)
