import numpy as np

class NB_Sentiment_Classifier:
    def __init__(self, texts:list, sentiments:list) -> None:
        assert len(texts) == len(sentiments), 'Za svaki tekst postoji tačno jedan sentiment.'
        self.texts = texts
        self.sentiments = sentiments
        self.pos_word_counts = {} 
        self.neg_word_counts = {}
        self.text_counts = {'pos': 0, 'neg': 0} # broj ✅ tekstova i broj ❌ tekstova
        self.n_words = {'pos': 0, 'neg': 0} # ukupan broj ✅ reči i ukupan broj ❌ reči
        self.prior = {'pos': 0, 'neg': 0} # P(✅) i P(❌)

    def _preprocess(self, text:str) -> str:
        '''Preprocess and returns text.'''
        import re
        text = re.sub(r'[^\w\s]', '', text) # uklonimo znakove
        words = text.lower().split() # svedemo na mala slova i podelimo na reči
        return words
    
    def fit(self) -> None:
        '''Train a classifier.'''
        pass


    def predict(self, text:str) -> tuple[float, float]:
        '''Returns a list of: [P(text|✅), P(❌|text)].'''
        pass


if __name__ == '__main__':
    reviews = {
    'The movie was great': 'pos',
    'That was the greatest movie!': 'pos',
    'I really enjoyed that great movie.': 'pos',
    'The acting was terrible': 'neg',
    'The movie was not great at all...': 'neg'}

    reviews_texts = list(reviews.keys())
    reviews_sentiments = list(reviews.values())
    clf = NB_Sentiment_Classifier(reviews_texts, reviews_sentiments)
    clf.fit()
    
    text = 'The movie was terrible, terrible, terrible,...'
    p_text_is_pos, p_text_is_neg = clf.predict(text)
    
    print(f'P(✅|{text}) = {p_text_is_pos:.5f}')
    print(f'P(❌|{text}) = {p_text_is_neg:.5f}')
    if p_text_is_pos > p_text_is_neg: print('Recenzija je pozitivna')
    else: print('Recenzija je negativna')
