''' Script is to prep a mgt dataset from a csv and cache it as a differint csv file '''

import pandas as pd



def prepare():

    # original read-in of data
    df = pd.read_csv('cards.csv')

    # list of columns i'm using from the original data

    # list of useful columns

    cols = [
        
            # columns I'm keeping
            'id', 
            'name',
            'manaCost', 
            'manaValue',
            'colors', 
            'colorIdentity',   
            'types', 
            'subtypes',
            'supertypes',
            'text',
            'power',     
            'toughness', 
            'loyalty',
            'defense',
            'leadershipSkills',
            'setCode', 
            'subsets',
        
            # columns for filtering 
            'isFunny', 
            'isOnlineOnly',
            'isOversized'        ]

    # filtering code

    # drop coluns not in list
    df = df[cols]

    # filter out cards that are in unsets, only online, or oversized
    df = df[df.isFunny == False]

    df = df[df.isOnlineOnly == False]

    df = df[df.isOversized == False]

    # drop filter columns
    df = df.drop(columns = ['isFunny', 'isOnlineOnly', 'isOversized'])

    # cache data
    df.to_csv('preped_mtg.csv')

if __name__ == '__main__':

    prepare()