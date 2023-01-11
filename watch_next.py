# Hello
# This code will suggest a film to the user based on word vector similarity of the description

# Import spacy and the language
import spacy
nlp = spacy.load('en_core_web_md')

# Provide description of film
hulk_title = "Planet Hulk"
hulk_description = ''' Will he save their world or destroy it? When the hulk becomes too
                        dangerous for the earth, the illuminati trick Hulk into a shuttle and launch him
                        into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on
                        the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# Cast the title and description to nlp
hulk_title_nlp = nlp(hulk_title)
hulk_description_nlp = nlp(hulk_description)


# Define the function that unpacks the list of movies stored in txt, cycles through each one comparing it to the
# description of the film already watched and prints the closest match.
def movie_match(description):
    open_moves = open('movies.txt', 'r')
    lines = open_moves.readlines()
    max_match = 0
    max_name = None
    for line in lines:
        similarity = nlp(line).similarity(description)
        if similarity > max_match:
            max_match = similarity
            max_name = line[:7]
    print(f"The best matched film is {max_name} with a match of {max_match}")


# Run the function giving it the hulk description 
movie_match(hulk_description_nlp)
