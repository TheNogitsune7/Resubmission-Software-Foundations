
from statistics import mean, median, stdev
from typing import List

def calculate_mean(scores: List[float]) -> float:
    return round(mean(scores), 2) if scores else 0.0

def calculate_median(scores: List[float]) -> float:
    return round(median(scores), 2) if scores else 0.0

def calculate_std_dev(scores: List[float]) -> float:
    return round(stdev(scores), 2) if len(scores) > 1 else 0.0

def calculate_pass_rate(scores: List[float], pass_mark: float) -> float:
    if not scores:
        return 0.0
    passed = sum(1 for score in scores if score >= pass_mark)
    return round((passed / len(scores)) * 100, 2)

def calculate_z_scores(scores: List[float]) -> List[float]:
    if not scores:
        return []
    mu = mean(scores)
    sigma = stdev(scores) if len(scores) > 1 else 1
    return [round((x - mu) / sigma, 2) for x in scores]

def assign_grade(score: float, pass_mark: float) -> str:
    if score >= 85:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= pass_mark:
        return 'D'
    else:
        return 'F'
