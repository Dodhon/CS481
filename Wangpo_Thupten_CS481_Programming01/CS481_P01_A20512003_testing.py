import pandas as pd
import time
import matplotlib.pyplot as plt
import random

def min_edit_distance(source, target):
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
            sub_cost = D[i-1][j-1] + (0 if source[i-1] == target[j-1] else 2)
            D[i][j] = min(del_cost, ins_cost, sub_cost)
    
    return D[n][m]

def generate_random_words(word_length, n=1, file_path='words.csv'):
    df = pd.read_csv(file_path, header=None)
    words = df[0].str.lower().tolist()  
    
    filtered_words = [word for word in words if len(str(word)) == word_length]
    
    if len(filtered_words) < n:
        raise ValueError(f"Not enough words of length {word_length} in the file.")
    
    return random.sample(filtered_words, n)

def measure_runtime_for_word(source, target):
    start_time = time.time()
    min_edit_distance(source, target)
    return time.time() - start_time

def main():
    trials = 100 
    
    lengths = range(1, 11)  
    average_times = []
    
    for length in lengths:
        total_time = 0
        for _ in range(trials):
            # random
            source = generate_random_words(word_length=length, n=1)[0]
            target = generate_random_words(word_length=length, n=1)[0]
            
            
            total_time += measure_runtime_for_word(source, target)
        
        
        avg_time = total_time / trials
        average_times.append(avg_time)
        print(f"Average processing time for word length {length}: {avg_time:.4f} seconds")
    
    return lengths, average_times

def plot_results(lengths, times):
    plt.figure(figsize=(8, 5))
    plt.plot(lengths, times, marker='o', linestyle='-', color='b')
    plt.title('Processing Time vs. Word Length')
    plt.xlabel('Word Length')
    plt.ylabel('Average Processing Time (seconds)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    lengths, average_times = main()
    plot_results(lengths, average_times)
