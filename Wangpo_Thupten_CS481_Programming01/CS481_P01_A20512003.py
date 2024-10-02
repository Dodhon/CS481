import sys
import pandas as pd
import time

def min_edit_distance(source, target, weights, substitution_weights=None):
    n = len(source)
    m = len(target)
    
    D = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        D[i][0] = D[i-1][0] + 1 
        
    for j in range(1, m+1):
        D[0][j] = D[0][j-1] + 1  
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            del_cost = D[i-1][j] + 1 
            ins_cost = D[i][j-1] + 1 
            
            if weights == 1 and substitution_weights is not None:
                sub_cost = D[i-1][j-1] + substitution_weights.get((source[i-1], target[j-1]), 2)
            else:
                sub_cost = D[i-1][j-1] + (0 if source[i-1] == target[j-1] else 2)
            
            D[i][j] = min(del_cost, ins_cost, sub_cost)
    
    return D[n][m]

def load_data(weights):
    words_df = pd.read_csv('words.csv', header=None) # I get an error if I do index_col=0
    words = words_df[0].str.lower().tolist() 

    substitution_weights = None
    
    if weights == 1:
        ed_weights = pd.read_csv('EDweights.csv', index_col=0) 
        substitution_weights = {}
        for source_letter in ed_weights.index:
            for target_letter in ed_weights.columns:
                substitution_weights[(source_letter, target_letter)] = ed_weights.loc[source_letter, target_letter]

    return words, substitution_weights


def process_misspelled_word(misspelled_word, words, weights, substitution_weights):
    
    min_dist = 571903650136451976395623048569134756203654987160582436598734
    suggestions = []
    
    for word in words:
        
        if isinstance(word, str):
            distance = min_edit_distance(misspelled_word.lower(), word, weights, substitution_weights)
            if distance < min_dist:
                min_dist = distance
                suggestions = [word]
            elif distance == min_dist:
                suggestions.append(word)
    
    suggestions.sort()
    
    return suggestions, min_dist


def display_results(name, weights, misspelled_word, processing_time, suggestions):
    
    print(f"{name} solution:")
    print(f"Weights: {weights}")
    print(f"Misspelled word: {misspelled_word}")
    print("")
    print(f"Processing time: {processing_time:.4f} seconds")
    print("")
    print("Minimum edit distance suggested word(s):")
    
    
    for i, suggestion in enumerate(suggestions):
        print(f"{i+1}. <{suggestion}>")

def main():
    if len(sys.argv) != 3:
        print("Error: Incorrect number of arguments.")
        return
    
    
    weights = int(sys.argv[1]) if sys.argv[1] in ['0', '1'] else 0 # If the WEIGHTS argument is out of the specified range, assume that the value for WEIGHTS is 0. The assignment doc doesn't say to check if it is a int at all.
    misspelled_word = sys.argv[2]
    
    words, substitution_weights = load_data(weights)
    
    start_time = time.time()
    
    suggestions, _ = process_misspelled_word(misspelled_word, words, weights, substitution_weights)
    
    processing_time = time.time() - start_time
    
    name = "Wangpo, Thupten, A20512003"
    display_results(name, weights, misspelled_word, processing_time, suggestions)

if __name__ == "__main__":
    main()