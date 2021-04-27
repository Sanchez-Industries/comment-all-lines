#!/usr/bin/python3
txt_banner= """
+=====================+
|  Comment All Lines  |
|   Version ONESHOT   |
|                     |
|   By Rick Sanchez   |
+=====================+
"""
print(txt_banner)
import argparse # the only one import, i don't care i have no need more
parser = argparse.ArgumentParser(description="Tool for comment all in an file... like an config file... I don't know haha...")
parser.add_argument("file", help="File to place at the begin of all line an '#' to comment him", type=str)
parser.add_argument("-y", "--yes", help="No confirmation mode ( !!! DANGER !!! )", action="store_true")
args = parser.parse_args()
filepath = args.file
yes_case = args.yes

# because it's cool
def YesOrNo():
    reply = input("Are you sure ?[yes/NO]")
    reply = reply.upper()
    if (reply=="YES") or (reply=="Y"):
        return True
    else:
        print ("'{}' is not an good reply. The program can't give the authorisation for continue, sorry...\n(if is an mistake please be calm and write correctly...)".format(reply))
        return False

# yeah... work....
def little_work():
    print("Okay the short work had to start...")
    with open(filepath, 'rb') as f:
        data = f.read().decode().split("\n")
        f.close()
    new_data=[]
    for d in data:
        if len(d) > 0:
            if d[0] != "#": 
                new_data.append("#" + d)
            else: 
                new_data.append(d)
    with open(filepath,'wb') as f:
        data = "\n".join(new_data)
        f.write(data.encode())
        f.close()
    print("All not commented are commented now! Done.")


if yes_case:
    print("no-confirmation mode enabled!")
    little_work()
elif YesOrNo():
    little_work()

# I am rick sanchez, I have do, cuz man I can and I want do that, no care about other shitty reasons to made that....

