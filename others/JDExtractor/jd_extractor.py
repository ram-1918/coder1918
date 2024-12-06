import pandas as pd
import numpy as np
import json
from collections import defaultdict
import re
import spacy

# multiple_words, languages, frameworks, python_libraries, apitype, webservers, databases, inmemorydb, 
# cicd_tools, containerization_tools, orchestration_tools
# task_queues, cloud, awsservices, os, ides, testing_frameworks, archtectures, design_patterns, 
# system_designs, distributed_systems, keywords, states, exclusion_words, exclusion_syms

# python, frameworks, pyspark, libraries, pandas, data science related, 
# testing both frontend and backend, deployment, hosting, cloud

class JDExtractor():
    def __init__(self):
        self.data = None
        self.jdText = ''
        self.categories = '''webtechnologies, languages, frameworks, python_libraries, apitype, webservers, databases, inmemorydb, cicd_tools, containerization_tools, orchestration_tools, task_queues, cloud, awsservices, os, ides, testing_frameworks, archtectures, design_patterns, system_designs, distributed_systems, keywords, states'''
        self.specifics = set()
        self.result = defaultdict(set)
    
    def __repr__(self):
        return f"I am JDExtractor's object!"
    
    def extractJsonData(self, filename):
        file = open(filename)
        self.data = json.load(file)
        print(f'Json extraction complete!')
    
    def extractJD(self, filename):
        file = open(filename, 'r')
        for line in file.readlines():
            # self.handleYears(line)
            self.handleLocation(line)
            self.jdText += line
        print(f'JD extraction complete!')
    
    def handleYears(self, line):
        if "yrs" in line.lower() or "years" in line.lower() or '+' in line or 'months' in line.lower() or "experience" in line.lower():
            # use regex in this line to get years and also write code to retrieve degree, and location - \s*(?:year|yr|years|yrs|experience|exp)
            year_regexp = re.findall(r'(?:[0-9]-[0-9]+? \w+|[0-9]+?) \w+', line.lower(), re.IGNORECASE)
            print('years', year_regexp)
            if year_regexp:
                for year in year_regexp:
                    self.result['years'].add(year)

    def handleLocation(self, line):
        # if 'location' in line.lower() or 'usa' in line.lower() or 'united states of america' in line.lower() or 'loc' in line.lower():
        for state in self.data['states']:
            if state in line.split():
                self.result['location'].add(state)

    def handleMultipleWords(self):
        multiple_words = self.data['multiple_words']
        for key, values in multiple_words.items():
            for word in values:
                if word in self.jdText.lower():
                    self.result[key].add(word)
                    self.jdText = self.jdText.replace(word, '')
        print(f"\nHandled Multiple words succussfully!")

    def classifyTerms(self, word, categories):
        word = word.lower().strip().strip(',').strip('.').strip('(').strip(')').strip('[').strip(']')
        if not word or word in self.data['exclusion_words'] or word in self.data['exclusion_syms']:
            pass
        else:
            for key in categories:
                key = key.strip()
                if word in self.data[key]:
                    self.result[key].add(word)
                    break
                else:
                    pass
            else:
                if word.isalpha():
                    self.specifics.add(word)
    
    def processJD(self):
        self.handleMultipleWords()
        categories = self.categories.split(',')
        jdWords = self.jdText.split()
        print('Handling words started!')
        for term in jdWords:
            self.classifyTerms(term, categories)
        print('Handling words ended!')

    def display(self):
        result = sorted(self.result.items(), key = lambda x: len(x[1]))
        print()
        for k,v in result:
            print(f'{k.upper()}: {sorted(list(v))}')
        print()

if __name__ == '__main__':
    jdobj = JDExtractor()
    print(jdobj)
    jdobj.extractJsonData('jd_terms.json')
    jdobj.extractJD('jd.txt')
    jdobj.processJD()
    jdobj.display()

