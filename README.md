# L3T11 Compulsory Task.

## Description:

This repository contains the files for Level 3 Task 11, as requested 
in the same's compulsory task. The purpose of this task is to 
demonstrate capability with the Spacy NLP module. 

As context, the following text relates to the task i was asked to
perform:

● Read the introduction about garden path sentences and explore a few of
the examples on Wikipedia.
● Create a new Python file called garden.py.
● Find at least 5 garden path sentences from the web or think up your own.
● Store the sentences you have identified or created in a list called
gardenpathSentences
● Tokenise each sentence in the list and perform entity recognition.
● Examine how spaCy has categorised each sentence. Then, use
spacy.explain to look up and print the meaning of entities that you don’t
understand. For example: print(spacy.explain("FAC"))
● At the bottom of your file, write a comment about two entities that you
looked up. For each entity answer the following questions:
  ○ What was the entity and its explanation that you looked up?
  ○ Did the entity make sense in terms of the word associated with it?
● Host your solution on a remote Git repo host such as GitHub or GitLab.

## Table of Contents:

### 1 - Installation
### 2 - Usage
### 3 - Credits

## 1 - Installation:

This requires docker desktop be installed if not already.

In an appropriate location/folder create a clone of this repository by 
running the following command in VSC or command line (remember to open 
the folder in VSC, or open terminal within the folder):

"git clone https://github.com/chatsim79/L3T11CT.git"

once the repository is cloned, cd into the App Files folder and run the
following command, providing an approriate app name:

docker build -t [app-name] ./ 

The Build process will occur automatically.

## 2 - Usage:

Run the following command to execute the code remembering to use the
app name you assigned in the build step.

docker run [app-name]

## 3 - Credits: 

Me :) Also thanks to John an Njabulo, who always provide excellent
assistance.


