import spacy

# nlp = spacy.load('en_core_web_sm')
nlp = spacy.load('ru_core_news_sm')
doc = nlp(u'севодня меня кто-то в метро лизнул жею')
for token in doc:
    print(token.head.text, token.pos_, token.dep_)
