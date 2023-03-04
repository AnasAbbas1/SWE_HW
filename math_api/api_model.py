import statistics
import numpy as np

class APIsModel:
    _NUMBERS_PARAM = 'numbers'
    _QUANTIFIER_PARAM = 'quantifier'
    _Q_PARAM = 'q'

    @staticmethod
    def min(data):
        return sorted(data[APIsModel._NUMBERS_PARAM])[:data[APIsModel._QUANTIFIER_PARAM]]

    @staticmethod
    def max(data):
        return sorted(data[APIsModel._NUMBERS_PARAM], reverse=True)[:data[APIsModel._QUANTIFIER_PARAM]]

    @staticmethod
    def avg(data):
        return sum(data[APIsModel._NUMBERS_PARAM]) / len(data[APIsModel._NUMBERS_PARAM])

    @staticmethod
    def median(data):
        return statistics.median(data[APIsModel._NUMBERS_PARAM])

    @staticmethod
    def percentile(data):
        return int(np.quantile(data[APIsModel._NUMBERS_PARAM], data[APIsModel._Q_PARAM] / 100, method='nearest'))