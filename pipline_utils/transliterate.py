from typing import Dict


class Transliterator:
    def __init__(self, config: str):
        self._config = self._process_config(config)

    @staticmethod
    def _process_config(config_root: str) -> Dict:
        with open(config_root, 'r', encoding='utf8') as fd:
            letters = fd.read()
            fd.close()
        letters = letters.split('\n')
        return {letter.split(",")[0]: letter.split(",")[1] for letter in letters if letter.split(",")[0]}

    def _transliterate_word(self, word):
        out_word = word.lower()
        for letter in self._config:
            if letter:
                out_word = out_word.replace(letter, self._config[letter])
                out_word = out_word.replace(letter.capitalize(), self._config[letter])
        return out_word

    @staticmethod
    def transliterate(word_list):
        for word in word_list.split("\n"):
            trans._transliterate_word(word)


if '__name__' == '__main__':
    trans = Transliterator("/home/valeria/Загрузки/translit_dict_mehweb.csv")

