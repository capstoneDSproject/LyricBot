from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtMultimedia, uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QPushButton, QVBoxLayout
import tkinter as tk
from tkinter import messagebox
import sys

import numpy as np
import cv2
import time
import os
import random
import re
from collections import defaultdict

import openpyxl 
import sys
import pymsgbox
import random
#from openpyxl import *
from tkinter import *
from tkinter import ttk
import nltk
import warnings
import string

import threading
import imp

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\s+', gaps=True)

class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


class UI(QWidget):
        
    def __init__(self):
        super(UI,self).__init__()

        
        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        self.button1= QPushButton("Romance")
        self.button1.clicked.connect(self.rom)

        self.button2= QPushButton("Rock")
        self.button2.clicked.connect(self.rock)

        self.button3= QPushButton("Hip Hop")
        self.button3.clicked.connect(self.hhp)

        self.button4= QPushButton("Pop")
        self.button4.clicked.connect(self.pop)

                #self.exit_button.clicked.connect(self.closeEvent)
        vbox = QVBoxLayout()
        vbox.addWidget(self.tb, 0)
        vbox.addWidget(self.button1, 1)
        vbox.addWidget(self.button2, 2)
        vbox.addWidget(self.button3, 3)
        vbox.addWidget(self.button4, 4)
        self.setLayout(vbox)

        self.setWindowTitle('LyricBot')
        self.setGeometry(500, 500, 500, 500)
        self.show()
        self.show()
        self.tb.append('Welcome to LyricBot!')
        self.tb.append('Press the button below to generate song lyrics based on the Genre provided')
      

    def rom(self):
        path = r"D:\LyricBot_Main\Romance.txt"
        with open(path) as f:
          text = f.read()
        tokenized_text = [
            word
            for word in tokenizer.tokenize(text)
            if word != ''
        ]

        # Create graph.
        markov_graph = defaultdict(lambda: defaultdict(int))

        last_word = tokenized_text[0].lower()
        for word in tokenized_text[1:]:
          word = word.lower()
          markov_graph[last_word][word] += 1
          last_word = word

        def walk_graph(graph, distance=5, start_node=None):
          """Returns a list of words from a randomly weighted walk."""
          if distance <= 0:
            return []

          # If not given, pick a start node at random.
          if not start_node:
            start_node = random.choice(list(graph.keys()))


          weights = np.array(
              list(markov_graph[start_node].values()),
              dtype=np.float64)
          # Normalize word counts to sum to 1.
          weights /= weights.sum()

          # Pick a destination using weighted distribution.
          choices = list(markov_graph[start_node].keys())
          chosen_word = np.random.choice(choices, None, p=weights)

          return [chosen_word] + walk_graph(
              graph, distance=distance-1,
              start_node=chosen_word)


        print("#--------------------------------Romance Song Start-------------------------------#") 
        print("\nVerse 1\n")
        
        for i in range(6):
          print(' '.join(walk_graph(
              markov_graph, distance=8)), '\n')

        print("\nChorus x2\n")
        for i in range(4):
          print(' '.join(walk_graph(
              markov_graph, distance=5)), '\n')

        print("\nVerse 2\n")
        for i in range(6):
          print(' '.join(walk_graph(
              markov_graph, distance=8)), '\n')

        print("\nRepeat Chorus x2\n")

        print("\nFinal Verse\n")
        for i in range(3):
          print(' '.join(walk_graph(
              markov_graph, distance=7)), '\n')
        print("#--------------------------------Romance Song End-------------------------------#") 


    def rock(self):
        # Read text from file and tokenize.
        path = r"D:\LyricBot_Main\Rock.txt"
        with open(path) as f:
          text = f.read()
        tokenized_text = [
            word
            for word in tokenizer.tokenize(text)
            if word != ''
        ]

        # Create graph.
        markov_graph = defaultdict(lambda: defaultdict(int))

        last_word = tokenized_text[0].lower()
        for word in tokenized_text[1:]:
          word = word.lower()
          markov_graph[last_word][word] += 1
          last_word = word

        def walk_graph(graph, distance=5, start_node=None):
          """Returns a list of words from a randomly weighted walk."""
          if distance <= 0:
            return []

          # If not given, pick a start node at random.
          if not start_node:
            start_node = random.choice(list(graph.keys()))


          weights = np.array(
              list(markov_graph[start_node].values()),
              dtype=np.float64)
          # Normalize word counts to sum to 1.
          weights /= weights.sum()

          # Pick a destination using weighted distribution.
          choices = list(markov_graph[start_node].keys())
          chosen_word = np.random.choice(choices, None, p=weights)

          return [chosen_word] + walk_graph(
              graph, distance=distance-1,
              start_node=chosen_word)

        print("\n\n\n\n")
        print("#--------------------------------Rock Song Start-------------------------------#") 
        print("\nVerse 1\n")
        for i in range(6):
          print(' '.join(walk_graph(
              markov_graph, distance=8)), '\n')

        print("\nChorus\n")
        for i in range(4):
          print(' '.join(walk_graph(
              markov_graph, distance=5)), '\n')

        print("\nVerse 2\n")
        for i in range(6):
          print(' '.join(walk_graph(
              markov_graph, distance=8)), '\n')

        print("\nRepeat Chorus x1\n") 

        print("\nBridge\n")
        for i in range(5):
          print(' '.join(walk_graph(
              markov_graph, distance=8)), '\n')

        print("\nRepeat Chorus x1\n")  
        print("#--------------------------------Rock Song End-------------------------------#")

    def hhp(self):
        # Read text from file and tokenize.
        path = r"D:\LyricBot_Main\HipHop.txt"
        with open(path) as f:
          text = f.read()
        tokenized_text = [
            word
            for word in tokenizer.tokenize(text)
            if word != ''
        ]

        # Create graph.
        markov_graph = defaultdict(lambda: defaultdict(int))

        last_word = tokenized_text[0].lower()
        for word in tokenized_text[1:]:
          word = word.lower()
          markov_graph[last_word][word] += 1
          last_word = word

        def walk_graph(graph, distance=5, start_node=None):
          """Returns a list of words from a randomly weighted walk."""
          if distance <= 0:
            return []

          # If not given, pick a start node at random.
          if not start_node:
            start_node = random.choice(list(graph.keys()))


          weights = np.array(
              list(markov_graph[start_node].values()),
              dtype=np.float64)
          # Normalize word counts to sum to 1.
          weights /= weights.sum()

          # Pick a destination using weighted distribution.
          choices = list(markov_graph[start_node].keys())
          chosen_word = np.random.choice(choices, None, p=weights)

          return [chosen_word] + walk_graph(
              graph, distance=distance-1,
              start_node=chosen_word)

        print("\n\n\n\n")
        print("#--------------------------------Hip Hop Song Start-------------------------------#") 
        print("\nIntro\n")
        for i in range(4):
          print(' '.join(walk_graph(
              markov_graph, distance=5)), '\n')

        print("\nHook\n")
        for i in range(4):
          print(' '.join(walk_graph(
              markov_graph, distance=10)), '\n')

        print("\nVerse 1 (Rap)\n")
        for i in range(12):
          print(' '.join(walk_graph(
              markov_graph, distance=5)), '\n')

        print("\nRepeat Hook x1\n")

        print("\nVerse 2 (Rap)\n")
        for i in range(12):
          print(' '.join(walk_graph(
              markov_graph, distance=5)), '\n')

        print("\nRepeat Hook x1\n")

        print("\nOutro\n")
        for i in range(5):
          print(' '.join(walk_graph(
              markov_graph, distance=5)), '\n')
        print("#--------------------------------Hip Hop Song End-------------------------------#")

    def pop(self):
        # Read text from file and tokenize.
        path = r"D:\LyricBot_Main\Pop.txt"
        with open(path) as f:
          text = f.read()
        tokenized_text = [
            word
            for word in tokenizer.tokenize(text)
            if word != ''
        ]

        # Create graph.
        markov_graph = defaultdict(lambda: defaultdict(int))

        last_word = tokenized_text[0].lower()
        for word in tokenized_text[1:]:
          word = word.lower()
          markov_graph[last_word][word] += 1
          last_word = word

        def walk_graph(graph, distance=5, start_node=None):
          """Returns a list of words from a randomly weighted walk."""
          if distance <= 0:
            return []

          # If not given, pick a start node at random.
          if not start_node:
            start_node = random.choice(list(graph.keys()))


          weights = np.array(
              list(markov_graph[start_node].values()),
              dtype=np.float64)
          # Normalize word counts to sum to 1.
          weights /= weights.sum()

          # Pick a destination using weighted distribution.
          choices = list(markov_graph[start_node].keys())
          chosen_word = np.random.choice(choices, None, p=weights)

          return [chosen_word] + walk_graph(
              graph, distance=distance-1,
              start_node=chosen_word)

        print("\n\n\n\n")
        print("#--------------------------------Pop Song Start-------------------------------#") 
        print("\nVerse 1\n")
        for i in range(7):
          print(' '.join(walk_graph(
              markov_graph, distance=8)), '\n')

        print("\nChorus\n")
        for i in range(6):
          print(' '.join(walk_graph(
              markov_graph, distance=7)), '\n')

        print("\nVerse 2\n")
        for i in range(7):
          print(' '.join(walk_graph(
              markov_graph, distance=8)), '\n')

        print("\nRepeat Chorus x1\n")

        print("\nBridge\n")
        for i in range(6):
          print(' '.join(walk_graph(
              markov_graph, distance=7)), '\n')

        print("\nRepeat Chorus x1\n")
        print("#--------------------------------Pop Song End-------------------------------#")



if __name__ == '__main__':

    app=QApplication(sys.argv)
    UIWindow=UI()
    sys.exit(app.exec_())

