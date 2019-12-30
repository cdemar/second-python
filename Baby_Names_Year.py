nm = {}

# This looks at the file

def readone(fn):
        # Open and read file into buffer
        #f = open(fn,"r")
        #lines = f.readlines()

        # If we need to read line 33, and assign it to some variable
        #x = lines[33]
        #print(x)
        global nm
        with open(fn,"r") as f:
                for l in f:
                        flds = l.strip().split(",")
                        #print(flds[12])
                        if flds[1] == "M":
                                print(nm)
                                nm[flds[0]] = float(flds[2])
readone("C:\\Users\\coryd\\Desktop\\python_class_idle\\names_baby\\yob1992.txt")

print(nm["Cory"])

