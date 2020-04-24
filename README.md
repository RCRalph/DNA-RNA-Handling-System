# DNA / RNA Handling System
This software allows compressing DNA and RNA contenting text files (4 times more effective space usage), creating complementary copies of the DNA / RNA and translating the RNA files into amino acid names, short-names and symbols. The software can only be used on Windows.

# Hardware specifications
This software can run on Windows only. It requires Python 3.5+. You also need the **msvcrt** and **multiprocessing** python package. To install it, run `pip install msvcrt` and `pip install multiprocessing` in your command line.

# Welcome screen
On the start of using the software you will see this screen:\
![Welcome screen](https://i.imgur.com/GSedfqN.png)\
Press any key on the keyboard to progress into the main menu.

# Menu
After the welcome screen the software will show this screen:\
![Main menu](https://i.imgur.com/bEtuDlf.png)\
All the functions listed above are explained below:

## Exit
This function closes the software window.

## Convert DNA or RNA file to and from TXT
This function opens the menu for converting DNA and RNA formatted files into .txt format or into compressed .dna and .rna files. For reference see below.

## Convert between DNA and RNA files
This function allows for creating complementary copies of DNA and RNA. Both .txt and .dna / .rna files are allowed. For reference see below.

## Translate RNA formatted TXT file to polypeptide
This function translates RNA contenting .txt file into a chain of amino acids. For reference see below.

# Convert DNA or RNA file to and from TXT
After pressing the key on the keyboard the software will output this screen:\
![Convert file formats](https://i.imgur.com/MFnyUN5.png)\
All functions are explained below:

## DNA files

### Convert from .dna file to .txt file
This function allows for conversions between compressed .dna file and uncompressed, human-readable .txt file. After choosing this function, you will see this screen:\
![Convert .dna to .txt](https://i.imgur.com/sgj2xBd.png)\
You need to move your file into the software directory (folder) and then enter its name into the console. Make sure not to include its extension. Press enter key to insert the information. After all above you will see the loading screen: When the conversion finishes successfully, you will see the ending screen. The output file name is **DNA.txt** and is located in the software directory. Press any key to return to main menu.

### Convert from .txt file to .dna file
This function allows for conversions between human-readable .txt file and compressed .dna file. After choosing this function, you will see this screen:\
![Convert .txt to .dna](https://i.imgur.com/9V4c9kV.png)\
You need to move your file into the software directory (folder) and then enter its name into the console. Make sure not to include its extension. Press enter key to insert the information. After all above you will see the loading screen. When the conversion finishes successfully, you will see the ending screen. The output file name is **DNA.dna** and is located in the software directory. Press any key to return to main menu.

## RNA files

### Convert from .rna file to .txt file
This function allows for conversions between compressed .rna file and uncompressed, human-readable .txt file. After choosing this function, you will see this screen:\
![Convert .rna to .txt](https://i.imgur.com/Pevxspz.png)\
You need to move your file into the software directory (folder) and then enter its name into the console. Make sure not to include its extension. Press enter key to insert the information. After all above you will see the loading screen. When the conversion finishes successfully, you will see the ending screen. The output file name is **RNA.txt** and is located in the software directory. Press any key to return to main menu.

### Convert from .txt file to .rna file
This function allows for conversions between human-readable .txt file and compressed .rna file. After choosing this function, you will see this screen:\
![Convert .txt to .rna](https://i.imgur.com/vP3TfZy.png)\
You need to move your file into the software directory (folder) and then enter its name into the console. Make sure not to include its extension. Press enter key to insert the information. After all above you will see the loading screen. When the conversion finishes successfully, you will see the ending screen. The output file name is **RNA.rna** and is located in the software directory. Press any key to return to main menu.

# Convert between DNA and RNA files
After pressing the key on the keyboard the software will output this screen:\
![Convert between files](https://i.imgur.com/z2gMaC9.png)\
All functions are explained below:

## Compessed files

### Convert from .dna file to complementary .rna file
This function allows for conversions between compressed .dna file and compressed .rna file while maintaining the rule of complementarity. After choosing this function, you will see this screen:\
![Convert .dna to complementary .rna](https://i.imgur.com/GeVnzPM.png)\
You need to move your file into the software directory (folder) and then enter its name into the console. Make sure not to include its extansion. Press enter key to insert the information. After all above you will see the loading screen. When the conversion finishes successfully, you will see the ending screen. The output file name is **RNA.rna** and is located in the software directory. Press any key to return to main menu.

### Convert from .rna file to complementary .dna file
This function allows for conversions between compressed .dna file and compressed .rna file while maintaining the rule of complementarity. After choosing this function, you will see this screen:\
![Convert .rna to complementary .dna](https://i.imgur.com/IwNd6VC.png)\
You need to move your file into the software directory (folder) and then enter its name into the console. Make sure not to include its extansion. Press enter key to insert the information. After all above you will see the loading screen. When the conversion finishes successfully, you will see the ending screen. The output file name is **DNA.dna** and is located in the software directory. Press any key to return to main menu.

## Text files

### Convert from DNA formatted .txt file to complementary RNA formatted .txt file
This function allows for conversions between compressed .dna file and compressed .rna file while maintaining the rule of complementarity. After choosing this function, you will see this screen:\
![Convert DNA formatted .txt to complementary RNA formatted .txt](https://i.imgur.com/0t9QdQc.png)\
You need to move your file into the software directory (folder) and then enter its name into the console. Make sure not to include its extansion. Press enter key to insert the information. After all above you will see the loading screen. When the conversion finishes successfully, you will see the ending screen. The output file name is **RNA.txt** and is located in the software directory. Press any key to return to main menu.

### Convert from RNA formatted .txt file to complementary DNA formatted .txt file
This function allows for conversions between compressed .dna file and compressed .rna file while maintaining the rule of complementarity. After choosing this function, you will see this screen:\
![Convert RNA formatted .txt to complementary DNA formatted .txt](https://i.imgur.com/r5rKEY5.png)\
You need to move your file into the software directory (folder) and then enter its name into the console. Make sure not to include its extansion. Press enter key to insert the information. After all above you will see the loading screen. When the conversion finishes successfully, you will see the ending screen. The output file name is **DNA.txt** and is located in the software directory. Press any key to return to main menu.

# Translate RNA formatted .txt file into polypeptide
This function allows for translation of RNA formatted .txt file into amino acid names, short names and symbols. After choosing this function, you will see this screen:\
![Translate RNA formatted .txt into polypeptide](https://i.imgur.com/wIKye5T.png)\
You need to move your file into the software directory (folder) and then enter its name into the console. Make sure not to include its extansion. Press enter key to insert the information. After that choose one of the options from the menu. You can make the output one of the following options:

 - full amino acid name (ex. Methionine)
 - short amino acid name (ex. Met)
 - amino acid symbol (ex. M)

Press the key assosiated with your prefered output. After that you will see the loading screen. When the translation finishes successfully, you will see the ending screen. The output file name is **Translation.txt** and is located in the software directory. Press any key to return to main menu.

# Loading screen
The loading screen is shown when an operation of converting or translating is running. The progress of the operation is displayed with accuracy of 2 decimal places. The example look of this screen is displayed below:\
![Loading screen example](https://i.imgur.com/fCB3eXQ.png)

# Ending screen
The ending screen is shown when an operation of converting or translating finishes. The screen includes the name of the output file. The example look of this screen is displayed below:\
![Ending screen template](https://i.imgur.com/M2PbDYA.png)\
Press any key on the keyboard to exit the ending screen.

# Error messages
When the software isn't able to detect your file or the file has invalid length or includes invalid characters. Below you can find the list of errors and their description:

## ERR 00
The software couldn't open the file. This might be caused by the file not being in the software directory.

## ERR 01
The file is too short to be valid. It doesn't include the character, which informs the software about This error only applies to the compressed files such as .dna and .rna. The solution to this error is converting the .txt file one more time. Don't edit the output file!

## ERR 02
First character is invalid. The reason is that the first character in the file is neither 1, 2, 3 nor 4. This error applies only to the compressed files such as .dna and .rna. The solution to this error is converting the .txt file one more time. Don't edit the output file!

## ERR 03
Invalid character that doesn't represent any nitrogenous bases. This means that your DNA or RNA formatted .txt file contents at least one character outside of the set:

| Nucleobase 	| DNA 	| RNA 	|
| :-----------:	| :---:	| :---:	|
| Adenine 		| ✓ 	| ✓ 	|
| Cytosine 		| ✓ 	| ✓ 	|
| Guanine 		| ✓ 	| ✓ 	|
| Thymine 		| ✓ 	| ✗ 	|
| Uracil 		| ✗ 	| ✓ 	|

# Format
The software interprets the binary data and converts .txt files this way:

| Nucleobase 	| DNA 	| RNA 	|
| :-----------:	| :---:	| :---:	|
| Adenine 		| 00 	| 00 	|
| Cytosine 		| 10 	| 10 	|
| Guanine 		| 11 	| 11 	|
| Thymine 		| 01 	| 01 	|
| Uracil 		| 01 	| 01 	|

# Additional information

## Randomly generated file
The repository includes a randomly-generated 1024 character long DNA formatted .txt file.

## Live file size monitor
The repository includes the <b>Life file size.py</b> python script, which allows you to monitor the file size in real time. The only thing you have to do is enter the file name with its extension.

## Random DNA generator
The repository includes the <b>Random DNA.py</b> python script, which allows you to generate a DNA file of entered length. The only thing you have to do is enter the wanted length of the file.