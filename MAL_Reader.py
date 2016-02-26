class ErrorCheck:
    def clean(self, mystr): #remove commas from strings

        for j in range(len(mystr)):

            if "," in mystr[j]:
                nocom = mystr[j]
                mystr[j] = nocom[:nocom.index(",")]

    def delabel(self, mystr): #remove first item from the list (the label)
        return mystr.pop(0)


    lineNum = 0
    errorCount = 0
    noErrors = True
    numOfOctErr = 0

    def __init__(self, oFile):
        self.oplist = ["MOVE", "MOVEI", "ADD", "INC", "SUB", "DEC", "MUL", "DIV", "BEQ", "BLT", "BGT", "BR", "END"]
        self.oFile = oFile
        self.errorCount = 0
        self.noErrors = True
        self.numOfInvOp = 0
        self.numOfTooFewOp = 0
        self.numOfTooMnyOp = 0
        self.numOfIllFormOp = 0
        self.numOfOctErr = 0

    def checkOpCode(self, mystr, lineNum):
        self.lineNum = lineNum
        if not any(mystr[0] in ite for ite in self.oplist): #check list of opcodes
            print("Invalid OP Code "+mystr[0])
            self.logerror("Error at line number " + str(lineNum) +": Invalid OP Code "+mystr[0]+"\n")
            self.numOfInvOp += 1
        else:
            if mystr[0] == "MOVE":
                self.checkmove(mystr)
            if mystr[0] == "MOVEI":
                self.checkmovei(mystr)
            if mystr[0] == "ADD":
                self.checkadd(mystr)
            if mystr[0] == "INC":
                self.checkinc(mystr)
            if mystr[0] == "SUB":
                self.checksub(mystr)
            if mystr[0] == "DEC":
                self.checkdec(mystr)
            if mystr[0] == "MUL":
                self.checkmul(mystr)
            if mystr[0] == "DIV":
                self.checkmul(mystr)
            if mystr[0] == "BEQ":
                self.checkdiv(mystr)
            if mystr[0] == "BLT":
                self.checkbeq(mystr)
            if mystr[0] == "BGT":
                self.checkblt(mystr)
            if mystr[0] == "BGI":
                self.checkbgt(mystr)
            if mystr[0] == "BR":
                self.checkbr(mystr)
            if mystr[0] == "END":
                self.checkend(mystr)

    def checkmove(self, mystr):
        self.check_length_ok(3, mystr)
        self.check_memid_ok(mystr[1])
        self.check_memid_ok(mystr[2])

    def checkmovei(self, mystr):
        self.check_length_ok(3, mystr)
        self.octalCheck(mystr[1])
        self.check_memid_ok(mystr[2])

    def checkadd(self, mystr):
        self.check_length_ok(4, mystr)
        self.octalCheck(mystr[1])
        self.check_memid_ok(mystr[1])
        self.octalCheck(mystr[2])
        self.check_memid_ok(mystr[2])
        self.octalCheck(mystr[3])
        self.check_memid_ok(mystr[3])

    def checkinc(self, mystr):
        self.check_length_ok(2, mystr)
        self.octalCheck(mystr[1])
        self.check_memid_ok(mystr[1])

    def checksub(self, mystr):
        self.check_length_ok(4, mystr)
        self.octalCheck(mystr[1])
        self.check_memid_ok(mystr[1])
        self.octalCheck(mystr[2])
        self.check_memid_ok(mystr[2])
        self.octalCheck(mystr[3])
        self.check_memid_ok(mystr[3])

    def checkdec(self, mystr):
        self.check_length_ok(2, mystr)
        self.octalCheck(mystr[1])
        self.check_memid_ok(mystr[1])

    def checkmul(self, mystr):
        self.check_length_ok(4, mystr)
        self.octalCheck(mystr[1])
        self.check_memid_ok(mystr[1])
        self.octalCheck(mystr[2])
        self.check_memid_ok(mystr[2])
        self.octalCheck(mystr[3])
        self.check_memid_ok(mystr[3])

    def checkdiv(self, mystr):
        self.check_length_ok(4, mystr)
        self.octalCheck(mystr[1])
        self.check_memid_ok(mystr[1])
        self.octalCheck(mystr[2])
        self.check_memid_ok(mystr[2])
        self.octalCheck(mystr[3])
        self.check_memid_ok(mystr[3])

    def checkbeq(self, mystr):
        self.check_length_ok(4, mystr)
        self.octalCheck(mystr[1])
        self.check_memid_ok(mystr[1])
        self.octalCheck(mystr[2])
        self.check_memid_ok(mystr[2])
        self.octalCheck(mystr[3])
        self.check_memid_ok(mystr[3])

    def checkblt(self, mystr):
        self.check_length_ok(4, mystr)
        self.octalCheck(mystr[1])
        self.check_memid_ok(mystr[1])
        self.octalCheck(mystr[2])
        self.check_memid_ok(mystr[2])
        self.octalCheck(mystr[3])
        self.check_memid_ok(mystr[3])

    def checkbgt(self, mystr):
        self.check_length_ok(4, mystr)
        self.octalCheck(mystr[1])
        self.check_memid_ok(mystr[1])
        self.octalCheck(mystr[2])
        self.check_memid_ok(mystr[2])
        self.octalCheck(mystr[3])
        self.check_memid_ok(mystr[3])

    def checkbr(self, mystr):
        self.check_length_ok(2, mystr)
        self.octalCheck(mystr[1])
        self.check_memid_ok(mystr[1])

    def checkend(self, mystr):
        self.check_length_ok(1, mystr)

    def check_length_ok(self, ops, mystr): # check the number of operands/operators for correct length
        if len(mystr)==ops:
            return True
        if len(mystr)>ops:
            self.logerror("Syntax error line:" + str(self.lineNum) +" invalid length, possibly too many operands")
            self.numOfTooMnyOp += 1
        if len(mystr)<ops:
            self.logerror("Syntax error, line:" + str(self.lineNum) +" invalid length, possibly too few operands")
            self.numOfTooFewOp += 1
        return False

    def check_memid_ok(self, memid): # check the string length of mem id for <=5
        if len(memid)<=5:
            return True
        else:
            self.logerror("Invalid Register or Mem ID: line:" + str(self.lineNum) +" Registers must be R0-R7 and Memory ID's must be 5 or less length")
            self.numOfIllFormOp += 1
        return False

    def logerror(self, error): # write to the log life and the output console
        self.errorCount += 1
        self.noErrors = False
        print(error)
        self.oFile.write(error+"\n")

    def octalCheck(self, myint):
        if "8" in myint or "9" in myint:
            self.logerror("Invalid number: Cannot contain 8 or 9 in numeral values")
            self.numOfOctErr = self.numOfOctErr + 1
            return False
        else:
            return True

    @staticmethod
    def register_check(rstr): #make sure a register is a valid register
        registerlist = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7"]
        if not any(rstr in ite for ite in registerlist):
            return False
        else:
            return True



#end of ErrorCheck


#START OF PROGRAM


fileName = "MAL Program 3" #Input file
fileName = fileName+".mal"
i = 1; #Line number
labelList = []


with open(fileName[:fileName.index(".mal")]+".log", 'w') as outFile: #creates the output file with Filename+_out
    e = ErrorCheck(outFile)
    outFile.write("             "+fileName+"\n"+"              Jeremy Mattson\n                  "
                                                "CS 3210"+"\n\n"+"MAL Program Listing:\n\n")
    for line in open(fileName, encoding="utf8"): #loop to go through whole text file line by line

        if ";" in line:
            line = line[0:line.index(";")] #remove comment

        if line.isspace():  #if line is only whitespace characters make it just it a "" string
            line = ""

        if not line == "": #line isn't comment or blank
            lineSplit = line.strip().split() # split line into a list of strings

            if ":" in lineSplit[0]: # if lineArray[0] is a label, has :
                labelList.append(lineSplit[0]) # add the label to label list
                lineCopy = lineSplit
                e.delabel(lineSplit) #remove label element

            labelList.append(e.clean(lineSplit))

            if len(lineSplit)>=1: #if not empty
                print(lineSplit)
                outFile.write(str(i)+" "+str(lineSplit)+"\n") #print to output file
                e.checkOpCode(lineSplit, i)




        i += 1 #inc line counter
        #end for loop
    if not e.noErrors:  # if errors were encountered
        outFile.write("\n__________\n"
                      "total errors = "+str(e.errorCount)+"\n")
    if e.numOfIllFormOp>0: outFile.write("   "+str(e.numOfIllFormOp) + " ill formed operand")
    if e.numOfInvOp>0: outFile.write("   "+str(e.numOfInvOp) + " invald opcode")
    if e.numOfTooFewOp>0: outFile.write("   "+str(e.numOfTooFewOp)+  "too few operands")
    if e.numOfTooMnyOp>0: outFile.write("   "+str(e.numOfTooMnyOp)+ " too many operands")
    if e.numOfOctErr>0: outFile.write("   "+str(e.numOfOctErr)+ " number of octal errors")
