from .table import LATIN_ALPHABET, \
                   ARABIC_NUMERALS, \
                   ASCII_SYMBOL, \
                   SPACE


class ZenHan:
    """
    半角と全角を正規化する
    """
    def __init__(self,
                 alphabet_zen_to_han=False,
                 alphabet_han_to_zen=False,
                 number_zen_to_han=False,
                 number_han_to_zen=False,
                 ascii_symbol_zen_to_han=False,
                 ascii_symbol_han_to_zen=False,
                 space_zen_to_han=False,
                 space_han_to_zen=False):
        self.validate_init_params(alphabet_zen_to_han,
                                  alphabet_han_to_zen,
                                  number_zen_to_han,
                                  number_han_to_zen,
                                  ascii_symbol_zen_to_han,
                                  ascii_symbol_han_to_zen,
                                  space_zen_to_han,
                                  space_han_to_zen)
        self.char_to_char_table = {}

        if alphabet_zen_to_han:
            _t = self.read_table(LATIN_ALPHABET, reverse=True)
            self.char_to_char_table.update(_t)
        elif alphabet_han_to_zen:
            _t = self.read_table(LATIN_ALPHABET, reverse=False)
            self.char_to_char_table.update(_t)

        if number_zen_to_han:
            _t = self.read_table(ARABIC_NUMERALS, reverse=True)
            self.char_to_char_table.update(_t)
        elif number_han_to_zen:
            _t = self.read_table(ARABIC_NUMERALS, reverse=False)
            self.char_to_char_table.update(_t)

        if ascii_symbol_zen_to_han:
            _t = self.read_table(ASCII_SYMBOL, reverse=True)
            self.char_to_char_table.update(_t)
        elif ascii_symbol_han_to_zen:
            _t = self.read_table(ASCII_SYMBOL, reverse=False)
            self.char_to_char_table.update(_t)

        if space_zen_to_han:
            _t = self.read_table(SPACE, reverse=True)
            self.char_to_char_table.update(_t)
        elif space_han_to_zen:
            _t = self.read_table(SPACE, reverse=False)
            self.char_to_char_table.update(_t)

    def validate_init_params(self,
                             alphabet_zen_to_han: bool,
                             alphabet_han_to_zen: bool,
                             number_zen_to_han: bool,
                             number_han_to_zen: bool,
                             ascii_symbol_zen_to_han: bool,
                             ascii_symbol_han_to_zen: bool,
                             space_zen_to_han: bool,
                             space_han_to_zen: bool):
        """
        初期化パラメーターを検証する
        """
        assert not (alphabet_zen_to_han is True and alphabet_han_to_zen is True)
        assert not (number_zen_to_han is True and number_han_to_zen is True)
        assert not (ascii_symbol_zen_to_han is True and ascii_symbol_han_to_zen is True)
        assert not (space_zen_to_han is True and space_han_to_zen is True)

        assert not (alphabet_zen_to_han is True \
           and alphabet_han_to_zen is True \
           and number_zen_to_han is True \
           and number_han_to_zen is True \
           and ascii_symbol_zen_to_han is True \
           and ascii_symbol_han_to_zen is True \
           and space_zen_to_han is True \
           and space_han_to_zen is True)

    def read_table(self, table, reverse=True):
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
