import re

def test():
    input = open("input.txt", "r")

    processed = []
    for idx, item in enumerate(input):
        extracted_number = re.findall(r'\d', item)
        
        processed.append("%s%s" % (extracted_number[0], extracted_number[-1]))


    total = 0
    
    for item in processed:
        total += int(item)

    print(total)

def test2():
    input = open("input.txt", "r")
    processed = []


    mapping = {"one": 1,
               "two": 2,
               "three": 3,
               "four": 4,
               "five": 5,
               "six": 6,
               "seven": 7,
                "eight": 8,
               "nine":9}
        
                    
     
    for idx, item in enumerate(input):
        extracted_number = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', item)

        to_append = "%s%s" % (mapping.get(extracted_number[0], extracted_number[0]), mapping.get(extracted_number[-1],extracted_number[-1]))

        processed.append(to_append)



    t = 0
    
    for item in processed:
        t += int(item)

    print(t)
    
        
    
if __name__ == "__main__":
    test()
    test2()
    
