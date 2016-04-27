import sys

# vowels
vowels = set(['a','e','u','i','o'])

def segmentize(word):
    word = word.lower()
    bogins = []
    start = -1
    end = 0
    pc = ''
    for c in word:
        iv = (c in vowels)
        if (iv):
            if (start > -1):
                if (end - 2 == start and pc in vowels):
                    end = end + 1
                bogins.append(word[start:end-1])
                start = end - 1
            else:
                start = 0	
        end = end + 1
        pc = c
    if (start > -1):
        bogins.append(word[start:])
    else:
        print "Imposible input"

    return bogins


def main():
    if (len(sys.argv) > 1):
        word = sys.argv[1]
        print segmentize(word)
    else:
        # test cases

        print segmentize("ayiq")
        print segmentize("alomat")
        print segmentize("soat")
        print segmentize("ayolni")
        print segmentize("shtirlitz")
        print segmentize("sirk")

if __name__ == "__main__":main()
