**Boolean Retrieval Model in Information Retrieval**

**Overview**
This repository contains the implementation of a Boolean Retrieval Model for Information Retrieval (IR). The project was completed as part of Programming Assignment No. 1 for the Information Retrieval (CS4051) course in Spring 2024.

**Objective**
The primary objective of this assignment was to understand and implement different indexing techniques for efficient query retrieval from a document collection. Specifically, we focused on creating an inverted index and a positional index to support Boolean Model operations in IR.

**Key Features**
1. Preprocessing Pipeline: Implemented a pipeline for tokenization, case folding, stop-words removal, and stemming (using the Porter Stemmer) to extract meaningful features from the provided research papers dataset.

2. Index Creation: Built both inverted and positional indexes to facilitate efficient determination of document-term relationships and term proximities.

3. Query Processing: Implemented a simplified Boolean IR model capable of handling queries composed of three terms and supported Boolean operators (AND, OR, NOT). Also supported positional queries.

4. Assumptions: Adhered to basic assumptions of the Boolean Retrieval Model, including term presence/absence in documents, equal evidential value of terms, and Boolean query operations.

5. Implementation Details: Provided a command-line interface for query execution and evaluation. Supported processing of 10 example queries provided in the assignment.

**Files**
1. Dataset: ResearchPapers.zip containing 20 research papers.
2. Stop-words List: File for stop-words removal during preprocessing.
3. Query Result-set: Gold standard for evaluating the implementation.

**Technologies Used**
Programming Language: Python
Libraries: nltk, numpy, and Tkinter

**Future Improvements**
1. Intuitive GUI: Plan to implement a graphical user interface for easier demonstration and interaction with the Boolean Retrieval Model.
2. Additional Features: Consider adding support for more complex query operations and incorporating frequency counts in the indexing process.

**How to run files?**

1) Copy code files into a directory that has a folder named "ResearchPapers" including all corpus documents
    and the same directory should contain a file named "Stopword-List.txt" enlisting all stopwords

2) Do "pip install customtkinter", it is necessary to run gui_interface.py
    2a) do "pip install -r requirements.txt" in the terminal to install the required packages

3) open gui_interface.py, and run it using the code runner extension if using VSCode 
4) It will take some seconds to load the GUI

5) The GUI has a search, use it to search any Boolean queries, proximity too.

Note: the value k differs in some cases due to different processing techniques, be a little flexible by testing a few values of k

Note: If you can not install customtkinter, you can use main.py or main.ipynb to test queries individually.

The files uploaded:

1) main.ipyn -> Jupyter file that consists code 
                snippets of code steps one by one 
                for experimentation/checking purposes
2) main.py -> The combined one-file of the Boolean Retrieval,
                 all functions under the class called "main".
3) gui_interface.py -> Implementation of GUI of the Boolean Retrieval System.


