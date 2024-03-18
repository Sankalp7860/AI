import pandas as pd
data2={
    "Subjects":["Physics","Algorithm","DSA","OS"],
    "Book_Authors":["Pratham","Shreshta","Shripad","Sankalp"],
    "No_of_Books":["11","23","40","31"]
}
IIIT_Library=pd.DataFrame(data2)
total_books=IIIT_Library.groupby('Subjects')['No_of_Books'].sum()

print("Total Number of Books for Each Subject:")
print(total_books)
