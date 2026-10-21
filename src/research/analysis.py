from __future__ import annotations
import numpy as np
import pandas as pd

def make_demo_data(n: int = 120, seed: int = 20261021) -> pd.DataFrame:
    # Deterministic synthetic data, only to verify the pipeline.
    rng = np.random.default_rng(seed)
    x = rng.normal(size=n)
    treatment = rng.binomial(1, 0.5, size=n)
    noise = rng.normal(scale=0.8, size=n)
    y = 1.2 + 0.7 * x + 0.9 * treatment + noise
    return pd.DataFrame({"outcome": y, "predictor": x, "treatment": treatment})

def simple_ols_coefficients(data: pd.DataFrame) -> tuple[float, float]:
    # OLS: outcome ~ intercept + treatment.
    x = np.column_stack([np.ones(len(data)), data["treatment"].to_numpy()])
    y = data["outcome"].to_numpy()
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    return float(beta[0]), float(beta[1])
