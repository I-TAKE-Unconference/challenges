from decimal import *
import math

def computeFraction(inputValue):
	global numerator
	global denominator
	getcontext().prec = 6
	numerator = pow(Decimal(1968002560) * Decimal(2.71828) / Decimal(2370), 2370)
	textNumerator = "Numarator = " + str(numerator) + "\n"
	textToFile += textNumerator

	denominator = Decimal(2) * Decimal(math.pi) * Decimal(2370) * inputValue
	global textToFile
	textDenominator = "Numitor = " + str(denominator) + "\n"
	textToFile += textDenominator

	fraction = numerator / denominator
	return fraction

def computeResult():
	global textToFile
	inputValue = computeInputValue()

	fraction = computeFraction(inputValue)
	textFraction = "Fractia = " + str(fraction) + "\n"
	textToFile += textFraction

	printToFileAtTimestamp(textToFile)
	print textToFile
