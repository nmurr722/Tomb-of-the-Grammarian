import Levenshtein
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os

spell_list_arr = []
dictionary_arr = []

##create the root window
#root = tk.Tk()
#root.title('Tkinter Open File Dialog')
#root.resizable(False, False)
#root.geometry('550x250')

#def select_dictionary():
#    filetypes = (
#        ('text files', '*.txt'),
#        ('All files', '*.*')
#    )
#
#    dictionary = fd.askopenfilename(
#        title='Choose a Dictionary',
#        initialdir='/',
#        filetypes=filetypes)
#    
#    with open(dictionary) as my_file:
#        dictionary_arr = my_file.readlines()
#    
#
#    
#def select_spells():
#    print(dictionary_arr)
#
#    filetypes = (
#        ('text files', '*.txt'),
#        ('All files', '*.*')
#    )
#        
#    spell_list = fd.askopenfilename(
#        title='Choose a spell list',
#        initialdir='/',
#        filetypes=filetypes)
#
#    #showinfo(
#    #    title='Selected File',
#    #    message=spell_list
#    #)
#
#
## open button
#open_dict = ttk.Button(
#    root,
#    text='Open a Dictionary File',
#    command=select_dictionary
#)
#
#open_spells = ttk.Button(
#    root,
#    text='Open a Spell List File',
#    command=select_spells
#)
#
#open_dict.pack(expand=True)
#open_spells.pack(expand=True)


##run the application
#root.mainloop()

with open("D:\GIT\Projects\Tomb_of_the_Grammarian\kpop_spellbook.txt") as my_spells:
        spell_list_arr = my_spells.read().splitlines()
#print(len(spell_list_arr))
#print(spell_list_arr)

with open("D:\GIT\Projects\Tomb_of_the_Grammarian\words.txt") as my_words:
        dictionary_arr = my_words.read().splitlines()
#print(len(dictionary_arr))

output = open(os.path.splitext(my_spells.name)[0] + '_' + "output.txt",'w')

for spell in spell_list_arr:
    spell_words = spell.split(' ')
    output.write("******************************* " + spell + "************************************************\n")
    for word in dictionary_arr:
        for spell_word in spell_words:
            if spell_word.casefold() != word.casefold():
                distance = Levenshtein.distance(spell_word.casefold(),word.casefold(), score_cutoff=1)
                if(distance < 2):
                    output.write(word + " -> " + spell.replace(spell_word,word)+ "\n")

print("Done!")

my_spells.close() 
my_words.close()
output.close()