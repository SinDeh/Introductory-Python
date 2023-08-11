from collections import OrderedDict

# Get the number of vocabularies with their translations
niter = int(input())

# Initialize an empty string to store the vocabulary entries
string_vocab = ''

# Loop to collect vocabulary entries
for _ in range(niter):
    vocab = input()  # Get input for each vocabulary entry
    string_vocab += vocab + ' '  # Append the vocabulary entry to the string

# Split the string_vocab into a list of vocabulary entries
list_vocab = string_vocab.split()

# Create an ordered dictionary from the list of vocabulary entries
name = OrderedDict()
for i in range(0, len(list_vocab), 2):
    name[list_vocab[i]] = list_vocab[i + 1]

# Get the sentence to be translated
sentence = input()

# Translate the sentence using the dictionary
translated = ''
for i in sentence.split():
    if i in name:
        translated += name.get(i) + ' '  # Translate the word if it's in the dictionary
    else:
        translated += i + ' '  # Keep the word as is if not in the dictionary

print(translated)  # Print the translated sentence
