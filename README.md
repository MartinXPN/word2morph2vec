# word2morph2vec
End to end pipeline for extracting morphological vectors from a given word

### Prerequisites
* Python 3.6
* Clone the repository and install the dependencies
```bash
git clone https://github.com/MartinXPN/word2morph2vec.git
cd word2morph2vec
pip install .
```



### Example usage
```python
from word2morph2vec import Word2Morph2Vec

m = Word2Morph2Vec.load_model(locale='ru')
print(m.get_word_vector(word='привет', lemma='привет'))
print(m.get_sentence_vectors(sentence=['привет', 'привет', 'привет']))
```