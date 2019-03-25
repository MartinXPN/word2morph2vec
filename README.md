# word2morph2vec
End to end pipeline for extracting morphological vectors from a given word


### Example usage
```python
from word2morph2vec import Word2Morph2Vec
m = Word2Morph2Vec.load_model(locale='ru')
print(m.get_word_vector(word='привет', lemma='привет'))
print(m.get_sentence_vectors(sentence=['привет', 'привет', 'привет']))
```