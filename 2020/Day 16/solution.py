import re
import functools

with open("input.txt", "r") as file: 
    data = file.read().strip()
    
def parse(data): 
    sections = data.split("\n\n")
    
    #parse the rules first
    fields = {}
    for field in sections[0].split("\n"): 
        match = re.match("([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)", field).groups()
        fields[match[0]] = [(int(match[1]), int(match[2])), (int(match[3]), int(match[4]))]
    
    #parse my own ticket
    header, ticket = sections[1].split("\n")
    ticket = [int(x) for x in ticket.split(",")]
    
    #parse other tickets
    header, *tickets = sections[2].split("\n")
    tickets = [[int(n) for n in t.split(",")] for t in tickets]
    
    return fields, ticket, tickets

def validate(ticket, fields):
    """
    returns the list of invalid numbers in a ticket
    """
    numbers = []
    for number in ticket:  
        for field in fields: 
            if fields[field][0][0] <= number <= fields[field][0][1]: 
                break
            if fields[field][1][0] <= number <= fields[field][1][1]: 
                break
        else: 
            numbers.append(number)
    return numbers

def run(data): 
    fields, ticket, tickets = parse(data)
    return sum([sum(validate(t, fields)) for t in tickets])

print(f"The ticket scanning error rate is {run(data)}")

def check(number, field):
    """
    Checks a number is valid for a given field (list of bounds)
    """
    if field[0][0] <= number <= field[0][1]: 
        return True
    if field[1][0] <= number <= field[1][1]: 
        return True
    return False

def iseligible(ticket, fields):
    """
    Checks a ticket is valid, i.e. each number can correspond 
    to at least one field
    """
    return all(any(check(n, fields[f]) for f in fields) for n in ticket)


def run(data): 
    """
    Determines which field is in which position on each ticket
    and returns the product of the six fields on my own ticket
    which starts with departure. 
    """
    fields, mine, tickets = parse(data)

    #filter tickets which are ineligible
    tickets = [t for t in tickets if iseligible(t, fields)]
    
    
    #map fields to possible positions
    options = {f:set() for f in fields}
    
    for field in fields: 
        for index in range(len(fields)):
            if all(check(ticket[index], fields[field]) for ticket in tickets): 
                options[field].add(index)
            
    #resolve the position of each field
    mapping = dict()
    
    while(len(options)) > 0 : 
        for field in options: 
            if len(options[field]) != 1: 
                continue
            
            mapping[field] = list(options[field])[0]
            
            #rebuild the mapping having removed the previously found field
            options = {f:{i for i in options[f] if i not in options[field]} for f in options if f != field}
            break
        
    #return the product of the six fields on my ticket which starts with "departure"
    return functools.reduce(lambda acc, curr: acc * curr, 
                     [mine[mapping[f]] for f in mapping if f.startswith("departure")])
        
        
print(f"The product of the six departure fields on my ticket is {run(data)}")