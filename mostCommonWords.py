from collections import Counter

def getTopSixWords(text):
    wordsAsList = Counter(text.split())
    topSix = wordsAsList.most_common(6)
    return topSix

text = "I hear the drums echoing tonight But she hears only whispers of some quiet conversation She's coming in, 12:30 flight \
The moonlit wings reflect the stars that guide me towards salvation I stopped an old man along the way \
Hoping to find some long forgotten words or ancient melodies He turned to me as if to say, Hurry boy, it's waiting there for you \
It's gonna take a lot to take me away from you There's nothing that a hundred men or more could ever do \
I bless the rains down in Africa Gonna take some time to do the things we never had The wild dogs cry out in the night\
As they grow restless, longing for some solitary company I know that I must do what's right As sure as Kilimanjaro rises like Olympus above the Serengeti \
I seek to cure what's deep inside, frightened of this thing that I've become It's gonna take a lot to drag me away from you \
There's nothing that a hundred men or more could ever do I bless the rains down in Africa Gonna take some time to do the things we never had \
Hurry boy, she's waiting there for you It's gonna take a lot to drag me away from you There's nothing that a hundred men or more could ever do \
I bless the rains down in Africa I bless the rains down in Africa (I bless the rain) I bless the rains down in Africa \
(I bless the rain) I bless the rains down in Africa I bless the rains down in Africa (Ah, gonna take the time) Gonna take some time to do the things we never had"


file = open("README.md", "r")

print("AFRICA BY TOTO: ", getTopSixWords(text))
print("READ ME FILE: ", getTopSixWords(file.read()))