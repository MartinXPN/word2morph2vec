from typing import Optional, List

from sentence2tags.parser import Parser
from word2morph import Word2Morph


class Word2Morph2Vec(object):
    def __init__(self,
                 sentence2tags: Optional[Parser] = None,
                 word2morph: Optional[Word2Morph] = None,
                 morph2vec=None):
        self.sentence2tags = sentence2tags
        self.word2morph = word2morph
        self.morph2vec = morph2vec

    def get_sentence_vector(self, sentence: List[str]):
        lemmas, morph_tags, pos_tags = self.sentence2tags.predict(sentence)
        vectors = [self.get_word_vector(word=word, lemma=lemma, morph_tags=mt, pos_tag=pos)
                   for word, lemma, mt, pos in zip(sentence, lemmas, morph_tags, pos_tags)]
        return vectors

    def get_word_vector(self,
                        word: str,
                        lemma: str,
                        morph_tags: Optional[List[str]] = None,
                        pos_tag: Optional[str] = None):
        morphemes = self.word2morph[lemma]
        vector = self.morph2vec.get(wordform=word, lemma=lemma,
                                    morph_tags=morph_tags, morphemes=morphemes, pos_tag=pos_tag)
        return vector


def load_model(sentence2tags_path: str, word2morph_path: str, morph2vec_path: str):
    # TODO load all 3 models and pass to word2morph2vec
    return Word2Morph2Vec()
