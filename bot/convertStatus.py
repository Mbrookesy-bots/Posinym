import re
import urllib.request, json

def convertToAntonym(current_status):

    with open("../config.json", "r") as file:
        config = json.load(file)

        sentence = []

        for word in current_status.split():
            with urllib.request.urlopen(config["url"] + word) as url:
                load = url.read()
                data = json.loads(load)
            sentence.append(data["antonym"])

    seperator = " "
    made_sentence = seperator.join(sentence)

    converted_text = re.sub('@{1}[^\s]*', '', made_sentence)

    return converted_text
