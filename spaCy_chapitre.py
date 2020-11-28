import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("fr_core_news_sm")

# Process whole documents
text = ("Par comparaison avec les autres asiles de Suisse, le taux des incurables à Préfargier est notablement élevé pour un asile qui prétend ne pas les accueillir. Dans la suite de son ouvrage, Ladame présente une statistique comparée des populations d’aliénés dans quatre asiles de Suisse. À la lecture de ces chiffes, il apparaît que les aliénés atteints de maladies incurables représentent 24 % de la population de Préfargier. ")
doc = nlp(text)

# Analyze syntax
print("Phrases nominales:", [chunk.text for chunk in doc.noun_chunks])
print("Verbes:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
