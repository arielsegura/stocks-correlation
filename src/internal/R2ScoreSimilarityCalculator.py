from sklearn.metrics import r2_score

from src.internal.SimilarityArrayUtils import fix_shape


class R2ScoreSimilarityCalculator:

    def calculate_similarity(self, x, y):
        x, y = fix_shape(x, y)

        return r2_score(x.reshape(-1, 1), y.reshape(-1, 1))
