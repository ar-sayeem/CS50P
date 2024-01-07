"""
def main():
    yell("This is CS50P")
def yell(phrase):
    print(phrase.upper())
if __name__ == "__main__":
    main()
"""

def main():
    yell("This", "is", "CS50P")
def yell(*words):
    uppercase = []
    for word in words:
        uppercase.append(word.upper())
    # print(uppercase)      # print as list, with qoutes
    print(*uppercase)

if __name__ == "__main__":
    main()