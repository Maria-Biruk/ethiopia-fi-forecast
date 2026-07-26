from dataclasses import dataclass

@dataclass
class ForecastConfig:
    forecast_years: int = 3
    confidence_level: float = 0.95
    random_state: int = 42