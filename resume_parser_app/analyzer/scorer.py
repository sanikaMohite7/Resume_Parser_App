from typing import Dict
from config.settings import WEIGHTS

def overall_score(scores: Dict[str, float]) -> float:
    s = 0.0
    for k, v in scores.items():
        s += WEIGHTS.get(k, 0.0) * v
    # clamp 0..1
    s = max(0.0, min(1.0, s))
    return s