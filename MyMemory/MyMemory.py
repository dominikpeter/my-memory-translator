import requests
import html

class MyMemory:
    def __init__(self):
        self.url = "https://api.mymemory.translated.net/get"
        self.params = {}
        self.json = {}
        self.translations = []
        self.scores = []

    def translate(self, sentence, source_lang, target_lang):
        self.params = {"q": sentence,
                       "langpair": f"{source_lang}|{target_lang}"}
        response = requests.get(self.url, params=self.params)
        self.json = response.json()
        self.translations = [i['translation'] for i in self.json['matches']]
        self.translations = [html.unescape(i) for i in self.translations]
        self.scores = [self._parse_int(i['quality']) for i in self.json['matches']]

    def extract_first(self, score=True):
        translation = self.translations[0]
        if score:
            return translation, self.scores[0]
        return self.translations[0]

    def extract_scores(self):
        if (not self.json):
            print("Init Translation")
            return None
        return self.scores

    def extract_translations(self, score=True):
        if score:
            return [(i, j) for i, j in zip(self.translations, self.scores)]
        else:
            return self.translations

    def _parse_int(self, x):
        try:
            return int(x)
        except TypeError:
            return 0
