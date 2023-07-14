# Fatih Semirgin 2019510068
# Ahmet Basbug 2020510135


# This function parses a string based on a list of symbols, creating a list of the symbols found in the string.
def parse_input(string_param, list_param):
    parsed_list = []
    while len(string_param) > 0:
        found_match = False
        for symbol in list_param:
            if string_param.startswith(symbol):
                parsed_list.append(symbol)
                string_param = string_param[len(symbol):].strip()
                found_match = True
                break
        if not found_match:
            break
    return parsed_list


# function checks if a given nested key exists within the
# keys of a value associated with a given key in a dictionary, and returns a boolean value indicating the result.
def isNestedKeyExist(dictParam, key, nestedKey):
    dictValue = dictParam.get(key)
    for value in dictValue.keys():
        if value == nestedKey:
            return True
    return False


# This function returns the key at the specified index in a dictionary.
def getKeyByIndex(indexParam, dictionaryParam):
    temp = 0
    for key in dictionaryParam.keys():
        if temp == indexParam:
            return key
        temp = temp + 1


# This function generates the output of an LL grammar for a given input and checks
# if a valid output can be generated according to the production rules specified in the grammar table.
def llParsing(dictionaryForLLParam, inputForLLParam):
    originalStack = ["$"]
    stack = ["$"]
    no = 1
    firstAction = ""

    for item in dictionaryForLLParam.values():
        firstAction = list(item.keys())[0] + "->" + list(item.values())[0]
        stack = stack + list(list(item.values())[0][::-1])
        break

    inputArray = parse_input(inputForLLParam, list(dictionaryForLLParam.keys()))

    if parse_input(inputForLLParam, list(dictionaryForLLParam.keys())) != []:
        print(("{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}".format("NO", "|", "STACK", "|", "INPUT", "|", "ACTION")))
        print(("{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}".format(no, "|", ''.join(originalStack), "|", ''.join(inputArray),
                                                                "|", firstAction)))

    while True:

        if parse_input(inputForLLParam, list(dictionaryForLLParam.keys())) == []:
            print("REJECTED (Input does not contain elements of terminals)")
            break

        firstTerminalInInput = inputArray[0]
        topElementOfStack = stack[len(stack) - 1]

        if firstTerminalInInput != topElementOfStack:
            no = no + 1
            if isNestedKeyExist(dictionaryForLLParam, firstTerminalInInput, topElementOfStack):
                firstAction = topElementOfStack + "->" + dictionaryForLLParam[firstTerminalInInput][topElementOfStack]
                print(("{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}".format(no, "|", ''.join(stack), "|",
                                                                        ''.join(inputArray), "|", firstAction)))

            else:
                print(("{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}".format(no, "|", ''.join(stack), "|",
                                                                        ''.join(inputArray), "|",
                                                                        "REJECTED (" + topElementOfStack + " does not have an action/step for " + firstTerminalInInput + ")")))
                break

        else:
            if len(firstTerminalInInput) == 1 and len(
                    topElementOfStack) == 1 and firstTerminalInInput == "$" and topElementOfStack == "$":
                no = no + 1
                print(("{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}".format(no, "|", "$", "|", "$", "|", "ACCEPTED")))
                break;
            no = no + 1
            print(("{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}".format(no, "|", ''.join(stack), "|", ''.join(inputArray),
                                                                    "|", f"Match and remove {firstTerminalInInput}")))

        if firstTerminalInInput == topElementOfStack:  # If the first terminal in input matches the top element of the stack
            stack.pop()  # Remove the top element from the stack
            inputArray.pop(0)  # Remove the first terminal from the input array

        else:  # If the first terminal in input does not match the top element of the stack
            stack.pop()  # Remove the top element from the stack
            if dictionaryForLLParam[firstTerminalInInput][topElementOfStack] != (
                    "ϵ" or "ε"):  # If there is a non-empty action/step for the current input symbol and stack symbol pair
                if allSymbols.__contains__(dictionaryForLLParam[firstTerminalInInput][
                                               topElementOfStack]):  # If the action/step is a single symbol
                    stack.append(dictionaryForLLParam[firstTerminalInInput][
                                     topElementOfStack])  # Add the action/step symbol to the stack
                else:  # If the action/step is a sequence of symbols
                    stack = stack + list(dictionaryForLLParam[firstTerminalInInput][topElementOfStack][
                                         ::-1])  # Add the sequence of symbols to the stack in reverse order

# This function checks the input according to the LR table and determined whether this input accepted or rejected.
def lrParsing(dictionaryForLRParam, inputForLRParam):
    no = 1
    stateStack = [list(dictionaryForLRParam.keys())[0]]
    read = ""
    inputArray = parse_input(inputForLRParam, actionAndGoTo)
    action = ""

    if parse_input(inputForLRParam, actionAndGoTo) != []:
        print(("{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}".format("NO", "|", "STATE STACK", "|", "READ", "|",
                                                                           "INPUT", "|", "ACTION")))
    rule_flag = False
    i = 0
    while True:
        if parse_input(inputForLRParam, actionAndGoTo) == []:
            print("REJECTED (Input does not contain elements of terminals)")
            break

        # Get the current symbol being read from the input
        read = inputArray[i]

        # Get the top state element of the stack
        firstStateElementOfStack = stateStack[len(stateStack) - 1]

        if not isNestedKeyExist(dictionaryForLRParam, firstStateElementOfStack, read):
            print(("{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}".format(no, "|", ' '.join(stateStack), "|", read,
                                                                               "|", ''.join(inputArray), "|",
                                                                               "REJECTED (State " + firstStateElementOfStack + " does not have an action/step for " + read + ")")))
            break

        # Get the action from the LR parsing table based on the current state and input symbol.
        # The action determines the next move of the parser.
        action = dictionaryForLRParam[firstStateElementOfStack][read]

        if action.lower() == "accept":
            print(("{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}".format(no, "|", ' '.join(stateStack), "|", read,
                                                                               "|", ''.join(inputArray), "|",
                                                                               "ACCEPTED")))
            break;

        elif not action.__contains__("->"):
            print(("{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}".format(no, "|", ' '.join(stateStack), "|", read,
                                                                               "|",

                                                                               ''.join(inputArray), "|",
                                                                               "Shift to state " + action)))

        else:
            print(("{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}{:^5}{:^16}".format(no, "|", ' '.join(stateStack), "|", read,
                                                                               "|",

                                                                               ''.join(inputArray), "|",
                                                                               "Reverse " + action)))

        # Initialize variables to empty strings
        value = ""
        key = ""

        # Check if action contains "State_" substring
        if action.__contains__("State_"):
            # Split the action string by "State_" substring
            splittedAction = action.split("State_")
            # Extract the second element of the splitted string and store it in value variable
            value = splittedAction[1]
            # Append value to the stateStack
            stateStack.append(value)

        # If action contains "->" substring
        elif action.__contains__("->"):
            rule_flag = True
            # Split the action string by "->" substring
            splittedAction = action.split("->")
            # Extract the first and second elements of the splitted string and store them in key and value variables respectively
            key = splittedAction[0]
            value = splittedAction[1]

        if rule_flag:
            # Pop the last len(parse_input(value, actionAndGoTo)) elements from the stateStack
            for x in range(len(parse_input(value, actionAndGoTo))):
                stateStack.pop()

            # Replace the first occurrence of value in the reversed part of inputArray before read with key
            temp_read_rest = ''.join(inputArray[:parse_input(''.join(inputArray), actionAndGoTo).index(read)])
            temp_read_rest = temp_read_rest[::-1].replace(value[::-1], key, 1)
            temp_read_rest = temp_read_rest[::-1]

            # Concatenate temp_read_rest and the remaining part of inputArray after read, and store it in inputArrayString
            inputArrayString = temp_read_rest + ''.join(
                inputArray[parse_input(''.join(inputArray), actionAndGoTo).index(read):])
            # Parse the inputArrayString and store it in inputArray
            inputArray = parse_input(inputArrayString, actionAndGoTo)

            # Decrease i by len(parse_input(value, actionAndGoTo)) + 1
            i -= len(parse_input(value, actionAndGoTo)) + 1
            rule_flag = False

        i += 1
        no = no + 1


try:
    FILE_LL = "ll.txt"
    FILE_LR = "lr.txt"
    FILE_INPUT = "input.txt"
    allSymbols = set()
    inputForLL = "";
    inputForLR = "";

    # Open LL(1) parsing table file
    file = open(FILE_LL, 'r', encoding='UTF-8')
    count = 0

    # Initialize dictionary for LL(1) parsing table
    dictionaryForLL = {}

    # Parse LL(1) parsing table
    while True:
        count += 1
        line = file.readline()
        if not line:
            break
        splittedlist = line.split(";")
        if count == 1:
            # Get all symbols from the first line
            for item in splittedlist:
                if item != "LL":
                    allSymbols.add(item.strip())
                    dictionaryForLL[item.strip()] = dict()
        else:
            # Get the current non-terminal symbol from the first element of the splitted list
            allSymbols.add(splittedlist[0])
            i = 1
            for key in dictionaryForLL.keys():
                # Parse each production rule
                if splittedlist[i].strip() != "":
                    temp = splittedlist[i].split("->")
                    # Add the production rule to the corresponding non-terminal symbol
                    dictionaryForLL[key][temp[0].strip()] = temp[1].strip().replace(" ", "")
                i += 1
    file.close()

    # Print a message after successfully reading the LL(1) parsing table
    print("Read LL(1) parsing table from file " + FILE_LL)

    # Open and read from the LR(1) parsing table file
    file = open(FILE_LR, 'r', encoding='UTF-8')
    count = 0
    dictionaryForLR = {}
    actionAndGoTo = []
    dictionaryCounter = 0

    # Loop through each line in the file
    while True:
        count += 1
        line = file.readline()
        if not line:
            break
        splittedlist = line.split(";")
        for i in range(len(splittedlist)):
            splittedlist[i] = splittedlist[i].strip()

        if count == 1:
            continue
        # If it's the second line, store "goto" states and actions
        elif count == 2:
            for item in splittedlist:
                actionAndGoTo.append(item.strip())
            actionAndGoTo.pop(0)
        else:
            num_state = splittedlist[0].split("_")
            dictionaryForLR[num_state[1]] = dict()
            index = 0
            # Add LR(1) parsing table actions and gotos to the dictionary
            for item in splittedlist:
                if index != 0:
                    if (item.strip() != ""):
                        keyFromDictionary = getKeyByIndex(dictionaryCounter, dictionaryForLR)
                        dictionaryForLR[keyFromDictionary][actionAndGoTo[index - 1]] = item.strip().replace(" ", "")
                index = index + 1
            if index != 0:
                dictionaryCounter = dictionaryCounter + 1

    file.close()
    print("Read LR(1) parsing table from file " + FILE_LR)
    print("Read input strings from file " + FILE_INPUT)

    # Open the input file in read mode
    file = open(FILE_INPUT, 'r', encoding='UTF-8')

    count = 0

    # Read the input file line by line
    while True:
        count += 1
        line = file.readline()

        # If there is no more line to read, exit the loop
        if not line:
            break

        # If this is not the first line of the file, process the input string
        if count != 1:
            splittedlist = line.split(";")

            # Check if the input string is for LL(1) or LR(1) parsing table
            if splittedlist[0].strip() == "LL":
                inputForLL = splittedlist[1].strip()
                print(f"\nProcessing input string {inputForLL.replace(' ','')} for LL(1) parsing table.\n")
                # Call the LL(1) parsing function for each input
                llParsing(dictionaryForLL, inputForLL)
            elif splittedlist[0].strip() == "LR":
                # Get the input string and remove any leading or trailing whitespaces
                inputForLR = splittedlist[1].strip()
                print(f"\nProcessing input string {inputForLR.replace(' ','')} for LR(1) parsing table.\n")
                # Call the LR(1) parsing function for each input
                lrParsing(dictionaryForLR, inputForLR)
            else:
                print("Invalid Format")

    file.close()
except:
    print("Please enter valid data or input form!")
