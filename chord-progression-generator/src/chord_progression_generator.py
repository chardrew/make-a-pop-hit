import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # (FATAL) Suppress verbose tensorflow warning and info messages
import logging
import numpy as np
import pandas as pd
import random
import tensorflow as tf
from tensorflow.keras.models import load_model
import tensorflow.keras.backend as K
from tensorflow.keras.layers import RepeatVector

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

def one_hot(x, depth):
    x = K.argmax(x)
    x = tf.one_hot(indices=x, depth=depth) 
    x = RepeatVector(1)(x)
    return x
    
    
def degrees_to_chords(degrees, key='random'):
    '''
    maps scale degrees to chords in in key provided
    '''
    
    if key == 'random':  # select random key as none was provided
        key = random.choice(key_chord_mapping.columns)
    
    chords_in_key = key_chord_mapping[key]
    chords = [chords_in_key[d] for d in degrees]
    
    return chords


def generate_chord_sequence(inference_model, x_init, a_init, c_init):
    '''
    generate a chord sequence of length Ty, according to inference_model,
    where Ty is output sequence length
    '''
    
    # generate array of decimals (activations)
    # shape (Ty, 7)
    prediction = inference_model.predict([x_init, a_init, c_init])
    
    # transform array by replacing them with the index (chord number - 1) of the corresponding maximum entry
    # shape (Ty, 1)
    indices = np.array(prediction).argmax(axis=-1)

    # convert array to corresponding chord outputs and flatten into list
    # shape (Ty, 1)
    sequence = map_to_chord_numbers(indices)
    
    return sequence


def map_to_chord_numbers(a):
    '''
    convert array of indices to their corresponding chord number
    '''
    return (a + 1).flatten().tolist()
    
    
# Load model
filename_inference_model = 'model'
MODEL_PATH = os.path.join('..', filename_inference_model)
model = load_model(MODEL_PATH)

# Load sequence -> chord mapper
try:
    DATA_DIR = os.path.join(os.getcwd(), '..', 'data')
    DATA_LOOKUPS_DIR = os.path.join(DATA_DIR, 'lookups')
    key_chord_mapping = pd.read_csv(os.path.join(DATA_LOOKUPS_DIR, 'musical_key-triad_chord_mapping.csv'), index_col='Degree')
except FileNotFoundError:
    DATA_DIR = os.path.join(os.getcwd(), '..', '..', 'data')
    DATA_LOOKUPS_DIR = os.path.join(DATA_DIR, 'lookups')
    key_chord_mapping = pd.read_csv(os.path.join(DATA_LOOKUPS_DIR, 'musical_key-triad_chord_mapping.csv'), index_col='Degree')

# Initialise variables
n = 7
n_a = 4*n
a_init = np.zeros((1, n_a))
c_init = np.zeros((1, n_a))
keys = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
exit_commands = ['exit', 'Exit', 'quit', 'Quit', 'q']

print('\n\n')
while True:
    # get user input for key
    key = input('Enter key of music (leave blank for random choice): ')
    
    # check if user wants to exit
    if key in exit_commands:
        exit('Program terminated by user')
    elif key == '':  # if nothing entered, then select random key
            key = random.choice(keys)
    try:
        assert key in keys
    except AssertionError:  # if key not valid, print help message and start again
        print('Please enter a valid key, or type exit')
        print(f'Accepted keys: {keys}')
        print()
        continue
    
    # generate a chord progression and display to user
    x_init = np.random.rand(1, 1, n)
    sequence = generate_chord_sequence(model, x_init, a_init, c_init)
    chords = degrees_to_chords(sequence, key)
    print(f'key: {key}  ---  {chords}')
    print()
    