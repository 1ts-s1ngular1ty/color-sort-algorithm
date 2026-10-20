--[[
	*| COLOR SORT ALGORITHM (PROTOTYPE) |*
	AUTHOR: 1TS_S1NGULAR1TY (roblox.com/users/699608387/profile)
	DATE: 7/29/2026
	LICENSE: BSD-3 Clause
	LANGUAGE: Luau (Roblox Native)
	DESCRIPTION: A creative and dominantly competitive prototyped unstable sorting algorithm which efficiently sorts data according to a predefined color gradient spectrum
	ORDER:
		- Ascending (isAscending = true)
		- Descending (isAscending = false)
	MODES:
		- Numerical (isNumerical = true)
		- Alphabetical (isNumerical = false)
	NOTES:
		- 11 colors by default
    	- 1st & 2nd letter sorting for alphabetical mode
]]

------------------------------
-- MODULE --
------------------------------
const ColorSort = {}

------------------------------
-- TYPES --
------------------------------
type Gradient = { Threshold: number, Color: Color3 }

------------------------------
-- INTERNAL VARIABLES --
------------------------------
local DataToFilter = {}
------------------------------
local AlphabetMap = {
	["A"] = 1,
	["B"] = 2,
	["C"] = 3,
	["D"] = 4,
	["E"] = 5,
	["F"] = 6,
	["G"] = 7,
	["H"] = 8,
	["I"] = 9,
	["J"] = 10,
	["K"] = 11,
	["L"] = 12,
	["M"] = 13,
	["N"] = 14,
	["O"] = 15,
	["P"] = 16,
	["Q"] = 17,
	["R"] = 18,
	["S"] = 19,
	["T"] = 20,
	["U"] = 21,
	["V"] = 22,
	["W"] = 23,
	["X"] = 24,
	["Y"] = 25,
	["Z"] = 26
}
------------------------------
local GradientMap: {[number]: Gradient} = {
	{ Threshold = 0, Color = Color3.fromRGB(255, 23, 68) }, -- Red [1]
	{ Threshold = 10, Color = Color3.fromRGB(255, 143, 0) }, -- Orange [2]
	{ Threshold = 20, Color = Color3.fromRGB(255, 235, 59) }, -- Yellow [3]
	{ Threshold = 30, Color = Color3.fromRGB(198, 255, 0) }, -- Lime [4]
	{ Threshold = 40, Color = Color3.fromRGB(0, 230, 118) }, -- Green [5]
	{ Threshold = 50, Color = Color3.fromRGB(0, 229, 255) }, -- Teal [6]
	{ Threshold = 60, Color = Color3.fromRGB(0, 176, 255) }, -- Cyan [7]
	{ Threshold = 70, Color = Color3.fromRGB(41, 98, 255) }, -- Blue [8]
	{ Threshold = 80, Color = Color3.fromRGB(61, 90, 254) }, -- Indigo [9]
	{ Threshold = 90, Color = Color3.fromRGB(124, 77, 255) }, -- Purple [10]
	{ Threshold = 100, Color = Color3.fromRGB(213, 0, 249) } -- Magenta [11]
}

------------------------------
-- INTERNAL FUNCTIONS --
------------------------------
local function MapValueToColorGradient(value: number, gradient: typeof(GradientMap))
	local minimumThreshold: number = gradient[1].Threshold
	local maximumThreshold: number = gradient[#gradient].Threshold
	local clampedValue: number = math.clamp(value, minimumThreshold, maximumThreshold)
	
	local lowerBound, upperBound
	for i = 1, #gradient - 1 do
		if clampedValue >= gradient[i].Threshold and clampedValue <= gradient[i + 1].Threshold then
			lowerBound = gradient[i]
			upperBound = gradient[i + 1]
			break
		end
	end
	if not lowerBound then return gradient[#gradient].Color end
	
	local range = upperBound.Threshold - lowerBound.Threshold
	local fraction = 0
	if range > 0 then
		fraction = (clampedValue - lowerBound.Threshold) / range
	end
	
	return lowerBound.Color:Lerp(upperBound.Color, fraction)
end

local function SortData(dataToUnpack: {}, isAscending: boolean, isNumerical: boolean)
	if not isNumerical then
		--|| Alphabetical Sorting ||--
		for dataIndex, dataValue in dataToUnpack do
			DataToFilter[dataIndex] = dataValue
		end
		
		for _, value in DataToFilter do
			if typeof(value) ~= "string" then return end
			
			local firstLetter = string.sub(value, 1, 1):upper()
			local secondLetter = string.sub(value, 2, 2):upper()
			
			local firstIndex = AlphabetMap[firstLetter]
			local secondIndex = AlphabetMap[secondLetter]
			
			if secondLetter ~= "" and firstIndex and secondIndex then
				if secondIndex >= firstIndex then
					MapValueToColorGradient(secondIndex, GradientMap)
				end
			end
			
			MapValueToColorGradient(firstIndex, GradientMap)
		end
		
		table.sort(DataToFilter, function(a, b)
			if isAscending then
				return a < b
			else
				return a > b
			end
		end)
	else
		--|| Numerical Sorting ||--
		for dataIndex, dataValue in dataToUnpack do
			DataToFilter[dataIndex] = dataValue
		end
		
		for _, value in DataToFilter do
			MapValueToColorGradient(value, GradientMap)
		end

		table.sort(DataToFilter, function(a, b)
			if isAscending then
				return a < b
			else
				return a > b
			end
		end)
	end
end

------------------------------
-- EXPORT --
------------------------------
return setmetatable(ColorSort, {
	__call = function(_, ...)
		SortData(...)
	end
})
