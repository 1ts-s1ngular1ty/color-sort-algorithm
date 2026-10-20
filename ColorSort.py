"""
*| COLOR SORT ALGORITHM (PROTOTYPE) |*
AUTHOR: S1NGULAR1TY (@github/1ts-s1ngular1ty)
DATE: 7/29/2026
LICENSE: BSD 3-Clause
LANGUAGE: Python (v3.14.4)
DESCRIPTION: A creative and dominantly competitive efficient prototyped unstable sorting algorithm which sorts data according to a predefined color gradient spectrum
ORDER:
    - Ascending (isAscending = True)
    - Descending (isAscending = False)
MODES:
    - Numerical (isNumerical = True)
    - Alphabetical (isNumerical = False)
NOTES:
    - No external package dependencies
    - 11 colors by default
    - 1st & 2nd letter sorting for alphabetical mode
"""

# ------------------------------
# -- DEPENDENCIES --
# ------------------------------
from typing import List, Dict, Union, Any
import time

# ------------------------------
# -- CLASSES --
# ------------------------------
class Color3: # Abstract Color3 class for representing specific RGB colors with an included lerp class method
    def __init__(self, r: float, g: float, b: float):
        self.r = r
        self.g = g
        self.b = b

    @classmethod
    def fromRGB(cls, r: float, g: float, b: float) -> 'Color3':
        return cls(r / 255.0, g / 255.0, b / 255.0)

    def lerp(self, other: 'Color3', fraction: float) -> 'Color3':
        return Color3(
            self.r + (other.r - self.r) * fraction,
            self.g + (other.g - self.g) * fraction,
            self.b + (other.b - self.b) * fraction
        )
        
    def __repr__(self) -> str:
        return f"Color3({self.r:.3f}, {self.g:.3f}, {self.b:.3f})"

# ------------------------------
# -- VARIABLES --
# ------------------------------
AlphabetMap: Dict[str, int] = {chr(65 + i): i for i in range(26)} # Iterates alphetical unicode character indexes from A-Z (ex: A = 0, B = 1, etc.) for alphabetical data filtration
# ------------------------------
GradientMap: List[Dict[str, Union[float, Color3]]] = [ # Predefined gradient color spectrum with keypoints that contain percent based thresholds and corresponding RGB values (ex: 0% = Red, 100% = Magenta)
    {"Threshold": 0, "Color": Color3.fromRGB(255, 23, 68)},    # Red [1]
    {"Threshold": 10, "Color": Color3.fromRGB(255, 143, 0)},   # Orange [2]
    {"Threshold": 20, "Color": Color3.fromRGB(255, 235, 59)},  # Yellow [3]
    {"Threshold": 30, "Color": Color3.fromRGB(198, 255, 0)},   # Lime [4]
    {"Threshold": 40, "Color": Color3.fromRGB(0, 230, 118)},   # Green [5]
    {"Threshold": 50, "Color": Color3.fromRGB(0, 229, 255)},   # Teal [6]
    {"Threshold": 60, "Color": Color3.fromRGB(0, 176, 255)},   # Cyan [7]
    {"Threshold": 70, "Color": Color3.fromRGB(41, 98, 255)},   # Blue [8]
    {"Threshold": 80, "Color": Color3.fromRGB(61, 90, 254)},   # Indigo [9]
    {"Threshold": 90, "Color": Color3.fromRGB(124, 77, 255)},  # Purple [10]
    {"Threshold": 100, "Color": Color3.fromRGB(213, 0, 249)}   # Magenta [11]
] # (Theoretically, more colors and/or higher color contrasts would increase the data filtration accuracy)

# ------------------------------
# -- HELPER FUNCTIONS --
# ------------------------------
def _clamp(value: float, minVal: float, maxVal: float) -> float:
    return max(minVal, min(value, maxVal))

# ------------------------------
# -- MAIN FUNCTIONS --
# ------------------------------
def mapValueToColorGradient(value: float, gradient: List[Dict[str, Any]]) -> Color3: # Blends each individual float value onto to the respective (weighted) percentage based threshold keypoints within the predefined color spectrum, using the principle of gradient color lerping (or linear interpolation)
    minimumThreshold = gradient[0]["Threshold"]
    maximumThreshold = gradient[-1]["Threshold"]
    clampedValue = _clamp(value, minimumThreshold, maximumThreshold)

    lowerBound, upperBound = None, None
    for i in range(len(gradient) - 1):
        if gradient[i]["Threshold"] <= clampedValue <= gradient[i + 1]["Threshold"]:
            lowerBound = gradient[i]
            upperBound = gradient[i + 1]
            break
            
    if not lowerBound:
        return gradient[-1]["Color"]
        
    rangeThreshold = upperBound["Threshold"] - lowerBound["Threshold"]
    fraction = 0.0
    if rangeThreshold > 0:
        fraction = (clampedValue - lowerBound["Threshold"]) / rangeThreshold
        
    return lowerBound["Color"].lerp(upperBound["Color"], fraction)

# ------------------------------
# -- PACKAGE CONSTRUCTOR --
# ------------------------------
class ColorSortClass:
    def __init__(self):
        self._dataToFilter = []
        print("Raw Time:", time.time()) # Benchmark timetstamp for raw data before filtration

    def __call__(self, dataToUnpack: List[float], *args) -> List[float]:
        isAscending = args[0] if args else True
        isNumerical = args[1] if len(args) > 1 else True

        # Sort the raw data with the above gradient mapping function (according to sort mode)
        self._dataToFilter = list(dataToUnpack)

        if isNumerical: # Numerical sorting
            for value in self._dataToFilter:
                mapValueToColorGradient(value, GradientMap)
        else: # Alphabetical sorting
            for value in self._dataToFilter:
                firstLetter = value[0].upper()
                secondLetter = value[1].upper()

                firstIndex = AlphabetMap[firstLetter]
                secondIndex = AlphabetMap[secondLetter]

                if secondIndex > firstIndex:
                    mapValueToColorGradient(secondIndex, GradientMap)

                mapValueToColorGradient(firstIndex, GradientMap)
            
        self._dataToFilter.sort(reverse = not isAscending)
        
        print("Sorted Time:", time.time()) # Benchmark timetstamp for sorted data after filtration

        return self._dataToFilter

ColorSort = ColorSortClass()
