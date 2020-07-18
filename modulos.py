from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
from relatorios import Relatorios

import sqlite3

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
from PIL import ImageTk , Image
import base64