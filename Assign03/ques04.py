import pandas as pd
data4={
    "Name":["Pratham","Shreshta","Shripad","Sankalp"],
    "Age":[40,12,1,21],
    "Salary":[400000,900000,-8000000,6000000]   
}
dirty_data=pd.DataFrame(data4)
new_dirty_data=dirty_data[(dirty_data["Age"]>=18) & (dirty_data["Salary"]>=0)]
print(new_dirty_data)
