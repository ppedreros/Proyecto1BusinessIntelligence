from sklearn.base import BaseEstimator, TransformerMixin
import re
import ftfy

class Preprocessing (BaseEstimator, TransformerMixin):
  def fit(self, X, y=None):
      return self

  def remove_punctuation(self, text):
      cleaned_text = ftfy.fix_text(text)
      cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)
      return cleaned_text

  def transform (self, X):
      X['Review'] = X['Review'].apply(ftfy.fix_text)
      X['Review'] = X['Review'].apply(lambda x: x.lower())
      X['Review'] = X['Review'].apply(self.remove_punctuation)
      X["Review"] = X["Review"].astype(str)

      return X["Review"]

