"""Madlibs take random inputs and output show a funny story """
import random
import json

with open('stories.json', 'r', encoding='utf-8') as file:
    stories = json.load(file)

n = random.randint(0,7)
story = stories[n]
inputlist = story["inputs"]
inputnumber = story["inputsnumber"]

inputs = {}

for i in range(inputnumber):
    temp = input(f"Enter {inputlist[i]} : ")
    inputs[inputlist[i]] = temp
 
text = story["story"]

text = text.format(**inputs)

# old implmentation
# for i in range(inputnumber):
#     start = text.index(inputlist[i]) - 1
#     end = start + len(inputlist[i]) + 1 
#     text = text[:start ] + inputs[i] + text[end+1:]

print()
print("=========================MADLIB=========================")
print()
print(text)

