import os
import emoji 
import numpy as np
from pandas import DataFrame
#my
from Process import loading
from Terminal import terminal_write

class questions:
    def questions_box():
        return [ 'import follow methods ? ->',
                 '---nickname full url to get his followers ? ->',
                 '---how much do you want to go down the scrolls? ->',
                 '---how many successful attempts do you want to make ? ->',
                 '---breaks between sessions ? ->',
                   
                 'import unfollow methods ? ->',
                 '---automatically unfollow bad candidates ?-->',
                 '---how much do you want to go down the scrolls? ->',
                 '---how many successful attempts do you want to make ? ->',
                 '---breaks between sessions ?->',
               
                 'import like by tags methods ? ->',
                 '---what is the hashtag ? ->',
                 '---how much do you want to go down the scrolls? ->',
                 '---how many successful attempts do you want to make ? ->',
                 '---breaks between sessions ? ->',
                 
                 'import like by following methods? -> ',
                 '---like specifically subscriptions okey ?->',
                 '---how many nicknames do we take ? ->',
                 '---how many successful attempts do you want to make ? ->',
                 '---breaks between sessions ?->',
               
                 'import story methods ? ->',
                 '---What percentage of stories do we like ? -> ',
                 '---how many recursions do you need ? ->',
                 '---how many successful attempts do you want to make ? ->',
                 '---breaks between sessions ? ->',
                
                'import comments methods ? ->',
                '---we will write positive comments to our subscribers okey? ->',
                '---how many nicknames do we take ? ->',
                '---how many successful attempts do you want to make ? ->',
                '---breaks between sessions ?->']
                 
                 
    def zeros(rangers):
        return [0 for ranger in range(rangers)]
    
    def question_method(questions_data):
        values=list()
        moment=0
        
        def ask(questions_data, moment):
            if moment>29:
                return values
            if moment%5==1:
                loading()
            terminal_write(questions_data[moment],
                           time_sleep=0.02,
                           endl=False)
            value=input()
            
            if value=='cd ..':
                if moment ==0:
                    return '------> out_of_value<------ !!! '
                else:
                    moment-=1
                    values.pop(-1)
                    print('<-- <--')
                    return ask(questions_data,moment)
            else:
                
                if value=='no' and moment%5==0:
                    values[moment:moment+5]=questions.zeros(5)
                    moment=len(values)
                    return ask(questions_data, moment)
                
                else:
                    try:
                        value=int(value)
                        values.append(value)
                        moment+=1
                    except:
                        values.append(value)
                        moment+=1
                    return ask(questions_data,  moment)
                
                    
        return ask(questions_data,moment)
    
    def preprocessor(vector):
        vector=np.array(vector)
        vector.shape=(6,5)
        matrix=DataFrame(vector).T
        matrix.columns=['    follow', '    unfollow', '    like by tags', '    like by following', '    story', '    comments']
        print('\n')
        
        loading(0.02)
        print('Please do not touch the computer because we are starting now !!! ')
        emoji_name=':raised_back_of_hand:'
        print(emoji.emojize(emoji_name)*20)
        loading(0.09)

        return matrix
        
        
 
    def main_stream():
        questions_box=questions.questions_box()
        questions_vector=questions.question_method(questions_data=questions_box)
        questions_matrix=questions.preprocessor(vector=questions_vector)
        
        indicators=[True if value=='yes' or value==1 or value=='True' else False for value in questions_matrix[:1].values[0]]
        
        return questions_matrix[1:], indicators

