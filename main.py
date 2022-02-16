#coding:utf8

from functionsAndClass import *
from data import *

#create track_user_choice file if not exists

create_file_if_not_exists(tracked_user_choice)

optimus = HumanPlayer('Mark')

computer = ProgramPlayer('Siri')

print(description)

while True:
    print()

    file = open(tracked_user_choice,"r+")
    all_lines = file.readlines()

    first_player_input = optimus.choice_obj(fourniture)
    second_player_input = computer.choice_obj(fourniture,all_lines)


    if first_player_input == 'q':
        file_empty(tracked_user_choice,"")
        break

    all_choice = f"{first_player_input}:{second_player_input}"


    checker = control_box.get(all_choice,0)
    print(f"{optimus.get_name()} 👱> ",fourniture_long[first_player_input])
    print(f"{computer.get_name()} 💻>",fourniture_long[second_player_input])
    print()
    print(fourniture_long[first_player_input]," -versus ",fourniture_long[second_player_input])
    if checker:
        if checker == 1:

            optimus.PT += 1
            computer.PT -= 1
            if computer.get_pt() < 0:
                computer.PT = 0
            computer.LS += 1
            print(f'--Human: {optimus.get_name()} Win a point !')
            print(optimus.get_player_infos())

        else :

            computer.PT += 1
            optimus.PT -= 1
            if optimus.get_pt() < 0:
                optimus.PT = 0
            optimus.LS += 1
            print(f'Computer: {computer.get_name()} Win a point !')
            print(computer.get_player_infos())

    else:
        print('Nothing...')
    
    if len(all_lines) <= 8:
        file.write(first_player_input+"\n")
    else:
        file_empty(tracked_user_choice,ch=first_player_input+"\n")
    file.close()


print()
print("---Final---")

if optimus.get_pt() > computer.get_pt():
    print("Human win the part !:")
    print(optimus.get_player_infos())
    print("Computer lost !!!:")
    print(computer.get_player_infos())

elif optimus.get_pt() == computer.get_pt():
    print("Wawou its formidable !")
    print("Nobody won a part ")
    print("Human:")
    print(optimus.get_player_infos())
    print("Computer:")
    print(computer.get_player_infos())

else:
    print("Computer win the part !:")
    print(computer.get_player_infos())
    print("Human lost the part !!!:")
    print(optimus.get_player_infos())