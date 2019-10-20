from parser import WiktionaryParser
import json
parser = WiktionaryParser()

# SETTINGS
showEtymology = False
currentLanguage = 'en'

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class language:
  DUTCH = 'nl'
  ENGLISH = 'en'

languageDefinitions_nl = {
  "participle": "participium",
  "singular": "enkelvoud",
  "nominative": "nominativus",
  "ablative": "ablativus"
}

def translateWord(word):
  languageDefinitions = {}
  if (currentLanguage == language.ENGLISH):
    return word
  if (currentLanguage == language.DUTCH):
    languageDefinitions = languageDefinitions_nl

  
  for key,val in languageDefinitions.items():
    if (key in word):
      return word.replace(key, val)
  
  return word

def translate(sentence):
  words = sentence.split(" ")
  newSentence = ""
  for i in range(0, len(words)):
    newSentence += translateWord(words[i] + " ")
  
  return newSentence

while True:
	print("\n")
	i = input("   " + color.UNDERLINE + "Word:" + color.END + " ")
	jsonData = parser.fetch(i, 'latin')
	#print(jsonData)
	if (len(jsonData) == 0 or len(jsonData[0]['definitions']) == 0):
		print(color.END + " x No results were found.")
	else:
		for x in range(0, len(jsonData[0]['definitions'])):
			print(color.END + color.BOLD + color.RED + " • Conjugation " + str(x+1) + ": " + color.END  + translate(jsonData[0]['definitions'][x]['text'][0]) + " (" +translate(jsonData[0]['definitions'][x]['partOfSpeech'] + ")"))

			for y in range(1, len(jsonData[0]['definitions'][x]['text'])):
				print(" • Definition  " + str(y) + ": " + translate(jsonData[0]['definitions'][x]['text'][y]))
			if (len(jsonData[0]['etymology']) > 0 and showEtymology): print(" • Etymology:    " + jsonData[x]['etymology'])
