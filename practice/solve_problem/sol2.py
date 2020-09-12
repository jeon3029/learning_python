

def main():
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                if (x+y+z) == 100:
                    print("(x,y,z)=("+str(x)+","+str(y)+","+str(z)+")")


# main starts
if __name__ == "__main__":
    main()
