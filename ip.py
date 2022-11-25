

def check_ip():
    print("Enter ip address: ")
    IP_ADDRESS = str(input())
    octates = IP_ADDRESS.split(".")
    if len(octates) == 4:  
        for i, octate in enumerate(octates):
            try:
                int(octate)
                if i == 3:
                    print("ip address is valid.")
            except ValueError:
                print("ip address is invalid.")
                break
        
    else:
        print("ip address is invalid.")


if __name__ == "__main__":
    while True: 
        check_ip()
        