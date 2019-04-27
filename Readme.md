

```python
from MyMemory import MyMemory
```


```python
mm = MyMemory()
```


```python
sentences = ["Das ist ein Test",
             "Hallo mein Name ist Hans",
             "MyMemory ist super",
             "Übersetzer ist kein Job mit Zukunft",
             "Künstliche Intelligenz wird die Welt übernehmen"]
```


```python
for sentence in sentences:
    mm.translate(sentence, "DE", "EN")
    print(mm.extract_first(score=False))
```

    This is a test.
    Hello my name is
    MyMemory is great
    Translator is not a job with a future
    Artificial intelligence will take over the world
    


```python
for sentence in sentences:
    mm.translate(sentence, "DE", "EN")
    transl, score = mm.extract_first(score=True)
    print(transl)
    print(f'Score = {score}')
    print("===============================")
```

    This is a test.
    Score = 74
    ===============================
    Hello my name is
    Score = 74
    ===============================
    MyMemory is great
    Score = 70
    ===============================
    Translator is not a job with a future
    Score = 70
    ===============================
    Artificial intelligence will take over the world
    Score = 70
    ===============================
    
