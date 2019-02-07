points = 0
play_list = []


def point_function(point):
    global points
    points = point + 1
    print("you get one point")
    print("you are now at", points, "points")


def word_search(gusword, gusnum, file_name, line_num, first_num, second_num):
    try:
        completed_list = []
        print("you get", gusword, "guesses")
        print("")
        wordfile = open(file_name, "r")
        finish = 0
        for line in wordfile:
            if finish == line_num:
                break
            print(line, end="")
            finish = finish + 1
        wordfile.seek(0)
        x = wordfile.readlines()[first_num:second_num]
        answer_list = [x]
        for guess in range(gusnum):
            question_input = input("what words do you see?  ")
            if question_input in completed_list:
                print("you already chose this")
            elif (question_input + "\n") in answer_list[0]:
                print("correct you found ", question_input)
                completed_list.append(question_input)
                point_function(points)
            elif (question_input + "\n") not in answer_list:
                print(question_input, "does not exist")
        wordfile.close()
        print("your turns are up")
        print("you found", completed_list)
    except IOError:
        print("brokeoz")


print("welcome to word search")
while "1" not in play_list or "2" not in play_list or "3" not in play_list:
    choice_input = input("what level do you want 1_easy, 2_medium, 3_hard")
    while choice_input != "1" and choice_input != "2" and choice_input != "3":
        print("input not valid")
        choice_input = input("what level do you want 1_easy, 2_medium, 3_hard")

    if choice_input == "1":
        if "1" in play_list:
            print("you already chose this")
        if "1" not in play_list:
            word_search("ten", 10, "easy file.txt", 7, 8, 18)
            play_list.append("1")
    if choice_input == "2":
        if "2" in play_list:
            print("you already chose this")
        if "2" not in play_list:
            word_search("six", 6, "medium file.txt", 9, 10, 16)
            play_list.append("2")
    if choice_input == "3":
        if "3" in play_list:
            print("you already chose this")
        if "3" not in play_list:
            word_search("seven", 7, "hard file.txt", 12, 13, 20)
            play_list.append("3")
print("thank you for playing :)")
print("final score", points)
