import timeit

def boyer_moore(text, pattern):

    #Алгоритм пошуку підрядка Боєра-Мура.

    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0

    last = {}
    for k in range(m):
        last[pattern[k]] = k

    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1

    return -1

def kmp_table(pattern):

    #Функція для створення таблиці для алгоритму Кнута-Морріса-Пратта.

    m = len(pattern)
    table = [0] * m
    i = 1
    j = 0
    while i < m:
        if pattern[i] == pattern[j]:
            i += 1
            j += 1
            table[i - 1] = j
        elif j > 0:
            j = table[j - 1]
        else:
            i += 1
    return table

def knuth_morris_pratt(text, pattern):

    # Алгоритм пошуку підрядка Кнута-Морріса-Пратта.

    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0

    table = kmp_table(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = table[j - 1]
            else:
                i += 1

    return -1

def rabin_karp(text, pattern, d=256, q=101):

    # Алгоритм пошуку підрядка Рабіна-Карпа.

    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if pattern == text[i:i + m]:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return -1

# Зчитування текстових файлів
def read_text_file(filename):
    # шлях до файлу
    filepath = f"C:/Users/Ahenoed/Documents/GitHub/goit-algo-hw-05/{filename}"  
    with open(filepath, "r", encoding="ansi") as f:
        return f.read()

text1 = read_text_file("стаття1.txt")
text2 = read_text_file("стаття2.txt")

# Підрядки для пошуку
pattern1 = "алгоритмів"  # Існуючий підрядок
pattern2 = "ацйуца"  # Вигаданий підрядок

# Функція для вимірювання часу виконання алгоритму
def measure_time(func, text, pattern, num_runs=100):
    time_taken = timeit.timeit(lambda: func(text, pattern), number=num_runs)
    return time_taken

# Вимірювання часу виконання для кожного алгоритму та підрядка
algorithms = {
    "Боєра-Мура": boyer_moore,
    "Кнута-Морріса-Пратта": knuth_morris_pratt,
    "Рабіна-Карпа": rabin_karp,
}

results = {}
for text_name, text in {"стаття1.txt": text1, "стаття2.txt": text2}.items():
    results[text_name] = {}
    for pattern_name, pattern in {"існуючий": pattern1, "вигаданий": pattern2}.items():
        results[text_name][pattern_name] = {}
        for algo_name, algo_func in algorithms.items():
            time_taken = measure_time(algo_func, text, pattern)
            results[text_name][pattern_name][algo_name] = time_taken

# Виведення результатів
for text_name, text_results in results.items():
    print(f"Результати для тексту: {text_name}")
    for pattern_name, pattern_results in text_results.items():
        print(f"  Підрядок: {pattern_name}")
        for algo_name, time_taken in pattern_results.items():
            print(f"    {algo_name}: {time_taken:.6f} секунд")

# Аналіз результатів та висновки (приклад)
fastest_overall = None
fastest_overall_time = float('inf')
for text_name, text_results in results.items():
    fastest_in_text = None
    fastest_in_text_time = float('inf')
    for pattern_name, pattern_results in text_results.items():
        for algo_name, time_taken in pattern_results.items():
            if time_taken < fastest_in_text_time:
                fastest_in_text_time = time_taken
                fastest_in_text = algo_name
            if time_taken < fastest_overall_time:
                fastest_overall_time = time_taken
                fastest_overall = algo_name
    print(f"Найшвидший алгоритм для {text_name}: {fastest_in_text}")
print(f"Найшвидший алгоритм в цілому: {fastest_overall}")