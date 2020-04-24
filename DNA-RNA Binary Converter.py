#global variables
directory = []
globalInfoArray = [False, False] #0 - operation progress, 1 - operation failed

def dotPrinting():
	#function for waiting until exactly half or the whole second is reached
	def waitUntil500():
		#setup
		import time, msvcrt

		#check if it's the first or second half of the second now
		half = False
		if ((time.time() * 1000) % 1000 > 500):
			half = True

		#repeat until a key is pressed or half or the whole second is reached
		while (True):
			#get current miliseconds
			miliseconds = int(time.time() * 1000)

			#check if half or the whole second is reached
			if (half == False and miliseconds % 1000 > 500 or half == True and miliseconds % 1000 <= 500):
				return False

			#check for keyboard hit
			if (msvcrt.kbhit()):
				#wait until the key is released
				while (msvcrt.kbhit()):
					msvcrt.getch()
				return True

			#slow down the script
			time.sleep(0.005)


	#print dots until keyboard hit
	while (True):
		#setup
		retVal = False

		#print 3 dots and check for keyboard hit while waiting 0.5 second
		for _ in range(3):
			print(".", end="", flush=True)
			retVal = waitUntil500()

			#check for keyboard hit
			if (retVal):
				clearConsole()
				break
		if (retVal):
			return

		#delete 3 last characters
		print ("\b\b\b   \b\b\b", end="", flush=True)

		#check for keyboard hit
		retVal = waitUntil500()
		if (retVal):
			clearConsole()
			return

def clearConsole():
	from os import system
	system("cls")
	return

def printDirectory():
	global directory

	for i in range( len(directory) ):
		print(" >> {}".format(directory[i]), end="")
	print ("\n")
	return

def printSimpleMenu(actions):
	#setup
	from msvcrt import getch

	#repeat until a correct key is pressed
	while (True):
		#setup
		clearConsole()
		printDirectory()
		print ("Press one of the following buttons to begin an action:")

		#print the menu
		for i in range(len(actions)):
			print ("[{}] - {}".format(i, actions[i]))

		#get the input from the user
		pressed = getch()

		#handle invalid button
		if (ord(pressed) < 48 or ord(pressed) > 47 + len(actions)):
			print ("\nIncorrect button pressed, try again by pressing a button", end = "")
			dotPrinting()
		else:
			return int(pressed)

def printAdvancedMenu(actionObject):
	#setup
	from msvcrt import getch

	#repeat until a correct key is pressed
	while (True):
		#setup
		clearConsole()
		printDirectory()
		print ("Press one of the following buttons to begin an action:")

		#print the menu
		currentNumber = 0
		for prop in actionObject:
			#print section header
			print ("\n" + prop, end="\n\n")

			#print section content
			for j in range(len(actionObject[prop])):
				print ("[{}] - {}".format(currentNumber, actionObject[prop][j]))
				currentNumber += 1

		#get the input from the user
		pressed = getch()

		#handle invalid button
		if (ord(pressed) < 48 or ord(pressed) > 47 + currentNumber):
			print ("\nIncorrect button pressed, try again by pressing a button", end = "")
			dotPrinting()
		else:
			return int(pressed)

def addDirectory(toAdd):
	directory.append(toAdd)
	clearConsole()
	printDirectory()
	return

def operationDone(message):
	print("{}\n\nPress any key to continue".format(message), end="")
	dotPrinting()

def bitStringToInt(bitString, DNAorRNA):
	#divide the input string into 2-bit segments
	bitString = [(bitString[i:i+2]) for i in range(0, len(bitString), 2)]

	#define values for the corresponding characters
	possibleChars = {
		".dna": {
			"00": "A",
			"01": "T",
			"10": "C",
			"11": "G"
		},
		".rna": {
			"00": "A",
			"01": "U",
			"10": "C",
			"11": "G"
		}
	}

	#set the values to corresponding 2-bit strings
	for i in range(len(bitString)):
		bitString[i] = possibleChars[DNAorRNA][bitString[i]]

	#return values as string
	return "".join(bitString)

def DNAorRNACharsToOneBinChar(fourChars):
	#setup
	result, parameter = 0, 64
	fourChars = fourChars.upper()

	#define the values to the corresponding bit numbers
	possibleCharsWithParameters = {
		"A": 0,
		"T": 1,
		"U": 1,
		"C": 2,
		"G": 3
	}

	#make an 8-bit number out of 4 characters
	for i in fourChars:
		result += int(parameter * possibleCharsWithParameters[i])
		parameter = parameter >> 2

	return result

def getFileNameAndSize(sourceExtension, minSize):
	clearConsole()
	printDirectory()
	import os
	fileData = ["", -1]

	while (fileData[1] < minSize):
		clearConsole()
		printDirectory()
		fileData[0] = input("Move the " + sourceExtension + " file into the software directory and enter its name without its extension.\n\nName of the file: ")
		
		try:
			open(fileData[0] + sourceExtension)
			fileData[1] = os.path.getsize(fileData[0] + sourceExtension)
			if (fileData[1] < minSize):
				print("\nERR 01: The selected file is too sort to be a valid " + sourceExtension + " file.\nPress any key to try again", end="")
				dotPrinting()
		except IOError:
			print("\nERR 00: Couldn't open the file.\n\nPress any key to try again", end="")
			dotPrinting()
		except os.error:
			print("\nERR 00: Couldn't open the file.\n\nPress any key to try again", end="")
			dotPrinting()
	
	return fileData

def pleaseWait(fileSize):
	#setup
	from time import sleep
	import sys
	clearConsole()
	printDirectory()
	print("Please wait until the operation finishes...")

	#print the progress until an error or completion
	global globalInfoArray
	while (globalInfoArray[0] != fileSize and globalInfoArray[1] == False):
		print("Progress: {:5.2f}%".format((100 * globalInfoArray[0]) / fileSize), end="\r")
		sleep(0.01)

	#reset the operation progress
	globalInfoArray[0] = False

	clearConsole()
	printDirectory()
	return

def convertDNAorRNAFile():
	def convertToTXT(sourceExtension, targetName):
		def convertBinFile(sourceFile, targetFile, fileExtension, fileSize):
			#read the number of characters in the last byte
			lastCharBitNumber = sourceFile.read(1)

			#check if the first character is valid and throw an error if isn't
			global globalInfoArray
			if (ord(lastCharBitNumber) < ord("1") or ord(lastCharBitNumber) > ord("4")):
				globalInfoArray[1] = True
				return False
			lastCharBitNumber = int(lastCharBitNumber)

			#read the file and convert it into txt
			for globalInfoArray[0] in range(1, fileSize - 1):
				targetFile.write(bitStringToInt(format(ord(sourceFile.read(1)), "08b"), fileExtension))
			targetFile.write(bitStringToInt(format((ord(sourceFile.read(1))), "08b"), fileExtension)[:lastCharBitNumber])
			globalInfoArray[0] = fileSize
			return True

		#setup
		addDirectory("Convert " + sourceExtension + " To .txt")
		fileData = getFileNameAndSize(sourceExtension, 1)

		#open source and target files
		sourceFile = open(fileData[0] + sourceExtension, "rb")
		targetFile = open(targetName + ".txt", "w")

		#multithreading setup
		from multiprocessing.pool import ThreadPool
		pool = ThreadPool(processes = 1)

		#start converting
		asyncResult = pool.apply_async(convertBinFile, (sourceFile, targetFile, sourceExtension, fileData[1]))
		pleaseWait(fileData[1])

		#get the result and close multithreading
		retVal = asyncResult.get()
		targetFile.close()

		#check for invalid file
		if (retVal == False):
			print ("The selected file is invalid.\n\nERR 02: Invalid first character in the file.\n\nPress any key to continue", end="")
			dotPrinting()
			return

		operationDone("The conversion between formats is done.\nThe converted file is called \"" + targetName + ".txt\"")
		return

	def convertToBINARY(targetExtension, targetFileName):
		def convertTXTFile(sourceFile, targetFile, possibleChars, fileSize):
			#setup
			readFour, readChar = "", ""
			global globalInfoArray

			#write into the target file
			for globalInfoArray[0] in range(fileSize):
				#write into the file if full byte in data
				if (globalInfoArray[0] % 4 == 0 and globalInfoArray[0] != 0):
					targetFile.write(bytes([DNAorRNACharsToOneBinChar(readFour)]))
					readFour = ""

				readChar = sourceFile.read(1).upper()

				#handle invalid character
				if (readChar not in possibleChars):
					globalInfoArray[1] = True
					return False

				readFour += readChar
			targetFile.write(bytes([DNAorRNACharsToOneBinChar(readFour)]))
			globalInfoArray[0] = fileSize
			return True

		#setup
		addDirectory("Convert .txt To " + targetExtension)
		fileData = getFileNameAndSize(".txt", 0)
		sourceFile = open(fileData[0] + ".txt", "r")
		targetFile = open(targetFileName + targetExtension, "wb")

		#write the number of characters in the last byte
		if (fileData[1] % 4 == 0):
			targetFile.write(bytes([ord("4")]))
		else:
			targetFile.write(bytes([ord(str(fileData[1] % 4))]))

		#set the characters
		possibleChars = ["A", "C", "G"]
		if (targetExtension == ".dna"):
			possibleChars.extend(["T"])
		else:
			possibleChars.extend(["U"])

		#multithreading setup
		from multiprocessing.pool import ThreadPool
		pool = ThreadPool(processes = 1)

		#start converting
		asyncResult = pool.apply_async(convertTXTFile, (sourceFile, targetFile, possibleChars, fileData[1]))
		pleaseWait(fileData[1])

		#get the result and close multithreading
		retVal = asyncResult.get()
		targetFile.close()

		#check for invalid file
		if (not retVal):
			print ("The selected file is invalid.\n\nERR 03: Invalid character that doesn't represent any nitrogenous bases.\n\nPress any key to continue", end="")
			dotPrinting()
			return

		operationDone("The conversion between formats is done.\nThe converted file is called \"" + targetFileName + targetExtension + "\"")
		return

	#setup
	addDirectory("Convert DNA Or RNA File To And From TXT")

	#iterate until correct value gets entered
	while (True):
		#setup
		operation = printAdvancedMenu({
			"DNA Files: ": ["Convert from .dna file to .txt file", "Convert from .txt file to .dna file"],
			"RNA Files: ": ["Convert from .rna file to .txt file", "Convert from .txt file to .rna file"]})

		#select funtion and pass arguments
		if (operation == 0):
			convertToTXT(".dna", "DNA")
			break
		elif (operation == 1):
			convertToBINARY(".dna", "DNA")
			break
		elif (operation == 2):
			convertToTXT(".rna", "RNA")
			break
		elif (operation == 3):
			convertToBINARY(".rna", "RNA")
			break

def convertBetweenFiles():
	def conversionBetweenBinaryFiles(sourceExtension, targetExtension):
		def convertBinaryFiles(sourceFile, targetFile, fileSize):
			def convertBetweenDNAandRNA(bitString):
				#divide the input string into 2-bit segments
				bitString = [(bitString[i:i+2]) for i in range(0, len(bitString), 2)]

				#set the values for corresponding 2-bit segments
				possibleChars = {
					"00": 1,
					"01": 0,
					"10": 3,
					"11": 2
				}
				#make an 8-bit number out of 4 characters
				result, parameter = 0, 64
				for i in bitString:
					result += possibleChars[i] * parameter
					parameter = parameter >> 2
				return result

			#setup
			global globalInfoArray

			#read the file and convert it into different type
			for globalInfoArray[0] in range(fileSize):
				targetFile.write(bytes([convertBetweenDNAandRNA(format(ord(sourceFile.read(1)), "08b"))]))
			globalInfoArray[0] = fileSize

			return True

		#setup
		addDirectory("Convert " + sourceExtension + " To " + targetExtension)
		fileData = getFileNameAndSize(sourceExtension, 1)

		#open file streams
		targetFileName = "DNA"
		if (targetExtension == ".rna"):
			targetFileName = "RNA"
		sourceFile = open(fileData[0] + sourceExtension, "rb")
		targetFile = open(targetFileName + targetExtension, "wb")

		#copy the first character from the source file to the target file
		targetFile.write(sourceFile.read(1))

		#multithreading setup
		from multiprocessing.pool import ThreadPool
		pool = ThreadPool(processes = 1)

		#start converting
		asyncResult = pool.apply_async(convertBinaryFiles, (sourceFile, targetFile, fileData[1] - 1))
		pleaseWait(fileData[1] - 1)

		#get the result and close multithreading
		retVal = asyncResult.get()
		targetFile.close()

		#check for invalid file
		if (not retVal):
			print ("The selected file is invalid.\n\nERR 03: Invalid character that doesn't represent any nitrogenous bases.\n\nPress any key to continue", end="")
			dotPrinting()
			return

		operationDone("The conversion between formats is done.\nThe converted file is called \"" + targetFileName + targetExtension + "\"")
		return

	def convertBetweenTextFiles(sourceFormat, targetFormat):
		def convertTextFiles(sourceFile, targetFile, fileSize, sourceFileFormat):
			#setup
			global globalInfoArray
			possibleChars = {
				"C": "G",
				"G": "C",
			}

			#set correct values regarding DNA or RNA
			if (sourceFileFormat == "DNA"):
				possibleChars["T"] = "A"
				possibleChars["A"] = "U"
			elif (sourceFileFormat == "RNA"):
				possibleChars["U"] = "A"
				possibleChars["A"] = "T"

			#read the file and convert it into DNA or RNA
			for globalInfoArray[0] in range(fileSize):
				importedChar = sourceFile.read(1)

				#check for invalid character and write into the file
				if importedChar in possibleChars:
					targetFile.write(possibleChars[importedChar.upper()])
				else:
					globalInfoArray[1] = True
					return False

			globalInfoArray[0] = fileSize
			return True

		#setup
		addDirectory("Convert " + sourceFormat + " To " + targetFormat)
		fileName = input("Move the " + sourceFormat + " formatted .txt file into the software directory and enter its name without its extension.\n\nName of the file: ")
		fileSize = getFileNameAndSize(".txt", 1)

		#open file streams
		sourceFile = open(fileName + ".txt", "r")
		targetFile = open(targetFormat + ".txt", "w")

		#multithreading setup
		from multiprocessing.pool import ThreadPool
		pool = ThreadPool(processes = 1)

		#start converting
		asyncResult = pool.apply_async(convertTextFiles, (sourceFile, targetFile, fileSize, sourceFormat))
		pleaseWait(fileSize)

		#get the result and close multithreading
		retVal = asyncResult.get()
		targetFile.close()

		#check for invalid file
		if (not retVal):
			print ("The selected file is invalid.\n\nERR 03: Invalid character that doesn't represent any nitrogenous bases.\n\nPress any key to continue", end="")
			dotPrinting()
			return

		operationDone("The conversion between formats is done.\nThe converted file is called \"" + targetFormat + ".txt\"")
		return

	#actual function:
	addDirectory("Convert Between DNA And RNA Files")
	while (True):
		operation = printAdvancedMenu({
			"Binary Files: ": ["Convert from .dna file to complementary .rna file", "Convert from complementary .rna file to .dna file"],
			"Text Files: ": ["Convert from DNA file to complementary RNA file", "Convert from complementary RNA file to DNA file"]})
		if (operation == 0):
			conversionBetweenBinaryFiles(".dna", ".rna")
			break
		elif (operation == 1):
			conversionBetweenBinaryFiles(".rna", ".dna")
			break
		elif (operation == 2):
			convertBetweenTextFiles("DNA", "RNA")
			break
		elif (operation == 3):
			convertBetweenTextFiles("RNA", "DNA")
			break

def translateRNAtoProtein():
	def getCodoneObject(dataType): #1 - full name, 2 - short name, 3 - symbol
		#setup
		aminoacidArray = [
			[["CAU", "CAC"], "Histidine", "His", "H"],
			[["AUU", "AUC", "AUA"], "Isoleucine", "Ile", "I"],
			[["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"], "Leucine", "Leu", "L"],
			[["AAA", "AAG"], "Lysine", "Lys", "K"],
			[["AUG"], "Methionine", "Met", "M"],
			[["UUU", "UUC"], "Phenylalanine", "Phe", "F"],
			[["ACU", "ACC", "ACA", "ACG"], "Threonine", "Thr", "T"],
			[["UGG"], "Tryptophan", "Trp", "W"],
			[["GUU", "GUC", "GUA", "GUG"], "Valine", "Val", "V"],
			[["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"], "Arginine", "Arg", "R"],
			[["UGU", "UGC"], "Cysteine", "Cys", "C"],
			[["CAA", "CAG"], "Glutamine", "Gln", "Q"],
			[["GGU", "GGC", "GGA", "GGG"], "Glycine", "Gly", "G"],
			[["CCU", "CCC", "CCA", "CCG"], "Proline", "Pro", "P"],
			[["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"], "Serine", "Ser", "S"],
			[["UAU", "UAC"], "Tyrosine", "Tyr", "Y"],
			[["GCU", "GCC", "GCA", "GCG"], "Alanine", "Ala", "A"],
			[["AAU", "AAC"], "Asparagine", "Asn", "N"],
			[["GAU", "GAC"], "Aspartic acid", "Asp", "D"],
			[["GAA", "GAG"], "Glutamic acid", "Glu", "E"],
			[["UAA", "UAG", "UGA"], "STOP", "STOP", "STOP"]]
		
		#convert the array into object with wanted values
		retArr = []
		for i in range(len(aminoacidArray)):
			for j in range(len(aminoacidArray[i][0])):
				retArr.append([aminoacidArray[i][0][j], aminoacidArray[i][dataType]])
		return dict(retArr)

	def translateFile(sourceFile, targetFile, fileSize, codones):
		#setup
		global globalInfoArray

		#get every 3 characters and translate them by codones
		for globalInfoArray[0] in range(0, fileSize, 3):
			targetFile.write(codones[sourceFile.read(3)])
			targetFile.write("\n")
		globalInfoArray[0] = fileSize

	#setup
	addDirectory("Translate RNA TXT File To Polypeptide")
	fileData = getFileNameAndSize(".txt", 0)
	fileData[1] -= fileData[1] % 3

	#get the wanted length of codone names and get the codones
	dataType = printSimpleMenu(["Use full names of amino acids", "Use short names of amino acids", "Use symbols of amino acids"])
	codones = getCodoneObject(dataType + 1)

	#open file streams
	sourceFile = open(fileData[0] + ".txt", "r")
	targetFile = open("Translation.txt", "w")

	#multithreading setup
	from multiprocessing.pool import ThreadPool
	pool = ThreadPool(processes = 1)

	#start converting
	asyncResult = pool.apply_async(translateFile, (sourceFile, targetFile, fileData[1], codones))
	pleaseWait(fileData[1])

	#get the result and close multithreading
	retVal = asyncResult.get()
	targetFile.close()	
	
	operationDone("The translation is done. The translated file is called \"Translation.txt\".")
	return

def main():
	#start screen
	print("Welcome to DNA / RNA Handling System.\n\nPress any key", end="")
	dotPrinting()

	#main menu and way to exit the programme
	global directory
	while (True):
		directory = ["Menu"]
		operation = printSimpleMenu(["Exit", "Convert DNA or RNA file to and from TXT", "Convert between DNA and RNA files", "Translate RNA formatted TXT file to polypeptide"])
		if (operation == 0):
			break
		elif (operation == 1):
			convertDNAorRNAFile()
		elif (operation == 2):
			convertBetweenFiles()
		elif (operation == 3):
			translateRNAtoProtein()
	return

main()