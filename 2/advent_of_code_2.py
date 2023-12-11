
POSSIBLE_CONFIGURATION = { "red": 12 , "green": 13, "blue": 14}

def remove_prefix(str):
    out = str.split(":")
    return out[1]

def separate_games(str):
    return str.split(";")


def extract_pairs(str):
    return str.split(",")

def extract_count_and_color(str):
    return str.split(" ")

def read_file():
     return open("input.txt", "r")

def remove_blanks(input):
    return [i for i in input if i]

def part1():
    input = read_file()

    sum_of_ids = 0
    

    for  idx, item in enumerate(input):    
        out = remove_prefix(item.rstrip("\n"))
        games = separate_games(out)

        is_valid_game = True

        for game in games:

            pairs = extract_pairs(game)

            for pair in pairs:
          
                count_and_color_pair =  extract_count_and_color(pair)
                
                count, color = remove_blanks(count_and_color_pair)

                if int(count) > POSSIBLE_CONFIGURATION[color]:
                    is_valid_game = False
                    continue
            
        if is_valid_game == True:
            sum_of_ids += idx + 1
        
    print(sum_of_ids)


def part2():
    input = read_file()

    sum_of_powers = 0

    for item in input: 

        min_config = {"red": 0, "blue": 0, "green": 0}   

        out = remove_prefix(item.rstrip("\n"))
        games = separate_games(out)

        for game in games:
            pairs = extract_pairs(game)
            for pair in pairs:
                count_and_color_pair =  extract_count_and_color(pair)
                count, color = remove_blanks(count_and_color_pair)

                if int(count) > min_config[color]:
                    min_config[color] = int(count)

        sum_of_powers += (min_config["red"] * min_config["blue"] * min_config["green"]) 

    print(sum_of_powers)


if __name__ == "__main__":
    part1()

    part2()
    
