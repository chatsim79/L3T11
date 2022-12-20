import spacy
nlp = spacy.load('en_core_web_sm')

# Create lsit of Garden Path sentences.
# Included one non GP sentence as entity recognition on them was unspectacular
gard_path = ['The horse raced past the barn fell,',
             'The old man the boat.',
             'The cotton clothing is made of grows in Mississippi.',
             'The sour drink from the ocean.',
             'We painted the wall with cracks.',
             '''The Next Generation Space Telescope, 
             which will be located much further away 
             from the Earth than the Hubble Space 
             Telescope presently is, will also explore 
             the infrared part of the spectrum.''']

# For in loop applying tokenisation to each successive string in list
for string in gard_path:
    # nlp calls spacy built in method on string
    doc = nlp(string)
    print("\n")
    print([(token, token.orth_, token.orth) for token in doc])
    print("\n")
    print([(i, i.label_, i.label) for i in doc.ents])

#Declare variables as entities to be explained.
entity_gpe = spacy.explain("GPE")
entity_org = spacy.explain("ORG")
print(f"\nGPE relates to: {entity_gpe}")
print(f"\nORG relates to: {entity_org}\n")

"""
Above print commands return:
1) 'GPE relates to: Countries, cities, states.'
2) 'ORG relates to: Companies, agencies, institutions, etc.'

1 makes sense as it is a state in the USA (Mississippi).

2 is a good attempt for 'The Next Generation Space Telescope" as it could sound like the name of an organisation or entity, but it is ultimately not correct as the entity is a Telescope.
"""
