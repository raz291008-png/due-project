import pandas as pd



def save(num,state,bush_lst,gamefield):
    data = {
        "state" : state,
        "bush_lst" : bush_lst,
        "gamefield" : gamefield
    }

    df = pd.DataFrame(data)
    with open(str(f"save{num}.csv"),"w") as save1:
        save1.write(str(df))

    df = pd.read_csv("save1.csv")
    print(df)

