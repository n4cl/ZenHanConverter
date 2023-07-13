from .table import LATIN_ALPHABET, \
                   ARABIC_NUMERALS, \
                   ASCII_SYMBOL, \
                   SPACE

class BaseConverter:
    """
    コンバーターの基底クラス
    """
    def __init__(self, alphabet_table, number_table, ascii_symbol_table, space_table, reverse):
        self.char_to_char_table = {}

        if alphabet_table:
            _t = self.read_table(LATIN_ALPHABET, reverse)
            self.char_to_char_table.update(_t)
        if number_table:
            _t = self.read_table(ARABIC_NUMERALS, reverse)
            self.char_to_char_table.update(_t)
        if ascii_symbol_table:
            _t = self.read_table(ASCII_SYMBOL, reverse)
            self.char_to_char_table.update(_t)
        if space_table:
            _t = self.read_table(SPACE, reverse)
            self.char_to_char_table.update(_t)


    def read_table(self, table, reverse=False):
        """
        変換テーブルを読み込む
        """
        if reverse:
            return {v: k for k, v in table.items()}
        else:
            return table

    def convert(self, text):
        """
        変換する
        """
        result = []
        for _t in text:
            if _t in self.char_to_char_table:
                result.append(self.char_to_char_table[_t])
            else:
                result.append(_t)
        return "".join(result)


class ZenToHan(BaseConverter):
    """
    全角を半角に変換するクラス
    """
    def __init__(self,
                 alphabet_table=True,
                 number_table=True,
                 ascii_symbol_table=True,
                 space_table=True):
        reverse = True
        super().__init__(alphabet_table, number_table, ascii_symbol_table, space_table, reverse)


class HanToZen(BaseConverter):
    """
    半角を全角に変換するクラス
    """
    def __init__(self,
                 alphabet_table=True,
                 number_table=True,
                 ascii_symbol_table=True,
                 space_table=True):
        reverse = False
        super().__init__(alphabet_table, number_table, ascii_symbol_table, space_table, reverse)
