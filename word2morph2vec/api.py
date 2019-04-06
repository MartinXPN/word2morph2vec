from typing import List, Tuple

from morph2vec import Morph2Vec
from nltk import everygrams
from sentence2tags import Sentence2Tags, sentence_to_tree
from word2morph import Word2Morph


class Word2Morph2Vec(object):
    def __init__(self,
                 sentence2tags: Sentence2Tags,
                 word2morph: Word2Morph,
                 morph2vec: Morph2Vec):
        self.sentence2tags = sentence2tags
        self.word2morph = word2morph
        self.morph2vec = morph2vec
        self.ngram_min_len = self.morph2vec.model.f.getArgs().minn
        self.ngram_max_len = self.morph2vec.model.f.getArgs().maxn

    def get_sentence_vectors(self, sentence: List[str]):
        tree = sentence_to_tree(sentence=sentence)
        tokens = self.sentence2tags[tree].tokens

        lemmas = [token.fields['lemma'] for token in tokens]
        pos_tags = [token.fields['upostag'] for token in tokens]
        morph_tags = [tuple(token.fields['feats'].split('|')) for token in tokens]

        vectors = [self.get_word_vector(word=word, lemma=lemma, morph_tags=mt, pos_tag=pos)
                   for word, lemma, mt, pos in zip(sentence, lemmas, morph_tags, pos_tags)]
        return vectors

    def get_word_vector(self,
                        word: str,
                        lemma: str,
                        pos_tag: str = '',
                        morph_tags: Tuple[str] = tuple()):
        morphemes = self.word2morph[lemma]
        ngrams = tuple([''.join(g) for g in everygrams(word, min_len=self.ngram_min_len, max_len=self.ngram_max_len)])

        vector = self.morph2vec.get_vector(word=word, lemma=lemma, pos=pos_tag,
                                           morph_tags=morph_tags,
                                           morphemes=morphemes.segments,
                                           ngrams=ngrams)
        return vector

    @staticmethod
    def load_model(locale: str):
        return Word2Morph2Vec(sentence2tags=Sentence2Tags.load_model(locale='hy'),
                              word2morph=Word2Morph.load_model(locale='ru'),
                              morph2vec=Morph2Vec.load_model(path='../morph2vec/logs/ru.bin'))
