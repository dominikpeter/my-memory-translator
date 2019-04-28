import requests
import html
import re
import time
from datetime import timedelta

class MyMemory:
    def __init__(self):
        self.url = "https://api.mymemory.translated.net/get"
        self.params = {}
        self.json = {}
        self.translations = []
        self.scores = []
        self.limit_reached = False
        self.seconds_to_wait = 0

    def translate(self, sentence, source_lang, target_lang):
        self.params = {"q": sentence,
                       "langpair": f"{source_lang}|{target_lang}"}
        response = requests.get(self.url, params=self.params)
        self.json = response.json()
        try:
            warning = self.json['responseData']['translatedText']
            self.limit_reached = warning.lower().startswith("mymemory warning")
        except Exception as e:
            self.limit_reached = False
        if self.limit_reached:
            #print("Limit reached")
            self.translations = ['limit reached']
            time_string = re.findall(
                r"\d*\sHOURS\s\d*\sMINUTES\s\d*\sSECONDS", warning)[0]
            ti = time.strptime(
                "09 HOURS 49 MINUTES 28 SECONDS",
                "%H HOURS %M MINUTES %S SECONDS")
            self.seconds_to_wait = timedelta(hours=ti.tm_hour,
                                             minutes=ti.tm_min,
                                             seconds=ti.tm_sec).total_seconds()
        else:
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
