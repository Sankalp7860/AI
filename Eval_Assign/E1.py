from Queue import PriorityQueue


def all_actions(state):
    actions = []
    m, c, b = state
    for dm, dc in [(0,1),(0,2),(1,0),(1,1),(2,0)]:
        if b==1:
            dm,dc = -dm,-dc
        new_state = (m+dm,c+dc,b^1)
        if is_valid(new_state):
            cost = 10*abs(dm)+20*abs(dc)
            actions.append((new_state, cost))
    return actions

def is_valid(state):
    m,c,b = state
    return (0<=m<=3 and 0<=c<=3 and (m==0 or m>=c) and (m==3 or m<=c))



def ucs():
    initial_state = ((3, 3, 1), 0)
    goal_state = (0, 0, 0)
    pq = PriorityQueue()
    pq.put((0, [initial_state]))
    vis = set()
    while not pq.empty():
        cost, path = pq.get()
        state = path[-1][0]
        if state == goal_state:
            return cost, path
        vis.add(state)
        for action in all_actions(state):
            new_state, action_cost = action
            if new_state not in vis:
                total_cost = cost + action_cost
                new_path = path + [(new_state, action_cost)]
                pq.put((total_cost, new_path))
    return -1, []


    
def main():  
    Total_cost, path = ucs()
    print("\tAssuming Boat cannot go empty from any side.....")
    for state, Curr_cost in path:
        m1,c1,b1=state
        m2,c2=abs(3-m1),abs(3-c1)
        print("\nOriginal Side of Bank: ("+str(m1)+", "+str(c1)+")")
        print("Crossed Side of Bank: ("+str(m2)+", "+str(c2)+")")
        print("Position of Boat(0: for crossed side, 1:for Original side): "+ str(b1))
        print("Cost:"+ str(Curr_cost))
    print("\n\tTotal cost: Rs %d" % Total_cost)
    
    
main()
    
    
    
    
    