import matplotlib.pyplot as plt
def analisis_frecuencias(file):
    with open(file, 'r') as f:
        text = f.read().upper().replace(" ", "")
    
    frecuencies = {}
    
    for char in text:
        if char.isalpha():
            frecuencies[char] = frecuencies.get(char, 0) + 1

    # Hacer un histograma
    plt.hist(frecuencies.keys(), weights=frecuencies.values())
    plt.show()


analisis_frecuencias('tortilla.txt')