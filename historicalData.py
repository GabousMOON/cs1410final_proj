"""
    Where I handle all of my historical data
"""
from typing import List, Dict, Union, Protocol
import pandas as pd


class HistoricalData(Protocol):
    def __init__(self) -> None:
        ...

    def __str__(self) -> str:
        ...

    def show(self) -> pd.DataFrame:
        ...


class PopulationData:
    def __init__(self) -> None:
        self.data: Dict[str, List[int]] = {
            "Healthy": [],
            "Asymptomatic": [],
            "Symptomatic": [],
        }

    def __str__(self) -> str:
        data = pd.DataFrame(self.data)
        return f"{data.to_string}"

    def show(self):
        return pd.DataFrame(self.data)


class PathogenData:
    def __init__(self) -> None:
        self.data: Dict[str, List[int]] = {
            "Damage Factor": [],
            "Cure Defense": [],
            "Longevity Factor": [],
            "Incubation Length": [],
            "Symp. Infectability": [],
            "Asymp. Infectability": [],
            "Surf. Infect. Factor": [],
        }

    def __str__(self) -> str:
        data = pd.DataFrame(self.data)
        return f"{data.to_string}"

    def show(self) -> pd.DataFrame:
        return pd.DataFrame(self.data)
