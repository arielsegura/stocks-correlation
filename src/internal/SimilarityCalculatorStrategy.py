from src.internal.CosineSimilarityCalculator import CosineSimilarityCalculator
from src.internal.NormalizedR2ScoreSimilarityCalculator import NormalizedR2ScoreSimilarityCalculator
from src.internal.R2ScoreSimilarityCalculator import R2ScoreSimilarityCalculator


class SimilarityCalculatorStrategy:
    def build_similarity_calculator(self, strategy):
        if strategy == 'cosine':
            return CosineSimilarityCalculator()
        elif strategy == 'r2-score':
            return R2ScoreSimilarityCalculator()
        elif strategy == 'normalized-r2-score':
            return NormalizedR2ScoreSimilarityCalculator()
        else:
            # TODO throw error
            print("Unsupported strategy " + strategy)
            return 0
