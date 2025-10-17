stations = ["HOW", "JAR", "LOY", "GRA"]

def insert_after(existing_station:str, new_station:str, in_list:list[str]):
    """
    Starting with
    stations = ["HOW", "JAR", "LOY", "GRA"]
    and calling  
    insert_after("JAR", "MORSE", stations):
    the stations list becomes 
    ["HOW", "JAR", "MOR", "LOY", "GRA"]
    """
    temp = [None] * (len(in_list)+1)
    shift = 0
    for i in range(len(in_list)):
        temp[i+shift] = in_list[i]
        if in_list[i] == existing_station:
            temp[i+1] = new_station
            shift = 1
    return temp

print(insert_after("JAR", "MOR", stations))


"""
Given a linked list: trainline

current = self.head
while current != None
  if current.data = existing_station
    new_node = Node(new_station:str)
    new_node.next = current.next
    current.next = new_node
    AAAAAAAAAAAAAA break
  current = current.next

"""
