def main():
    # ask user what to print
    msg = input("insay imu ha?")
 
    # convert 
    result = convert(msg)

    # Print result 
    print(result)

def convert(msg):
    # replce :(
    msgq = msg.replace(":(",'🥹')

    # replace :)
    msgw = msgq.replace(":)", '😄')

    # return
    return msgw

main()