# Assignment: Character Frequency Analysis of "Things Fall Apart"
# Author: Chinua Achebe
# Course: FAC 201: DIGITAL HUMANITIES: APPLICATION OF COMPUTER TO THE ARTS
# Date: 30th March 2026
# Description: This program counts occurrences of selected characters
# and visualizes the result using a pie chart.

import matplotlib.pyplot as plt
import re

def read_text(file_path):
    """Reads and returns the content of a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().lower()

def count_characters(text, characters):
    """
    Counts exact word occurrences of each character
    using regular expressions for accuracy.
    """
    counts = {}
    for name in characters:
        pattern = r'\b' + name + r'\b'   # ensures full word match
        matches = re.findall(pattern, text)
        counts[name] = len(matches)
    return counts

def plot_pie_chart(data):
    """Displays a pie chart of character occurrences."""
    labels = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Character Occurrence in Things Fall Apart")
    plt.axis('equal')  # makes the pie chart circular
    plt.show()

def main():
    file_path = "things_fall_apart.txt"
    characters = ["okonkwo", "okoye", "obiako", "okafo", "obierika"]

    try:
        text = read_text(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Please ensure the text file is in the same directory as the script.")
        return

    counts = count_characters(text, characters)

    print("Character Frequencies:")
    for name, count in counts.items():
        print(f"{name.capitalize()}: {count}")

    if sum(counts.values()) == 0:
        print("\nNo occurrences of the specified characters were found. Pie chart will not be drawn.")
        return

    plot_pie_chart(counts)

if __name__ == "__main__":
    main()