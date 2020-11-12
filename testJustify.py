"""
Given an array of words and a width maxWidth, format the text such that each line has exactly 
maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.
"""
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        i = 0
        current_line = []
        remaining_length = maxWidth
        while i < len(words):
            word = words[i]
            # if more than one word, we need space inbetween
            space = 0 if len(current_line) == 0 else 1
            #we have another word
            if remaining_length - len(word) - space >= 0:
                current_line.append(word)
                remaining_length = remaining_length - len(word) - space
                i += 1                
            else:
                lines.append(current_line.copy())
                current_line = []
                remaining_length = maxWidth
        #we add the last line 
        if len(current_line) > 0:
            lines.append(current_line)


        lines_justified = []
        for index, line in enumerate(lines):
            line_length = 0
            for word in line:
                line_length += len(word)
            #dummy case, line has one word only
            if len(line) == 1:
                lines_justified.append(line[0] + ' ' * (maxWidth - len(line[0])))
            #dummy case 2 - last line 
            elif index == len(lines) - 1:
                line_justified = ''
                extra_spaces = maxWidth - line_length
                for idx, word in enumerate(line):
                    if idx < len(line) - 1:
                        line_justified += word + ' '
                        extra_spaces -= 1
                    else:
                        line_justified += word + (' ' * extra_spaces)
                lines_justified.append(line_justified)
            else:
                #we substract #words - 1    
                extra_spaces = maxWidth - line_length
                extra_space_per_word = extra_spaces // (len(line) - 1)
                remaining_spaces = extra_spaces - (len(line) - 1) * extra_space_per_word
                line_justified = ''
                    
                for index_word, word in enumerate(line):
                    if index_word < len(line) - 1:
                        if remaining_spaces > 0:
                            extra_space = ' '
                            remaining_spaces -= 1
                        else:
                            extra_space = ''
                        line_justified += word + (' ' * extra_space_per_word) + extra_space
                    #last word we just add it
                    else:
                        line_justified += word
                lines_justified.append(line_justified)
        
        return lines_justified


def test():
    sol = Solution()

    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    answer = sol.fullJustify(words, maxWidth)
    print(answer)


    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    answer = sol.fullJustify(words, maxWidth)
    print(answer)

    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    answer = sol.fullJustify(words, maxWidth)
    print(answer)


test()
