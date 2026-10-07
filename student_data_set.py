import pandas as pd

#Step 1:Create a dictionary with student data
data ={
'NAME':['ALI','SARA','IHTISHAM','ANUM','EMAN'],
'MATH':[80,90,70,67,88],
'PHYSICS':[70,56,90,67,88],
'COMPUTER':[50,70,99,86,66]
}

#Step 2:Convert dictionary to DATA FRAME
df= pd.DataFrame(data)

#Step 3:Display the data frame
print("Student data:\n",df)

#Step 4:Calculate average score of every student
df['Average']=df[['MATH','PHYSICS','COMPUTER']].mean(axis=1)

#Step 5:Display student with highest average
top_student=df.loc[df['Average'].idxmax()]
print("\nTOP STUDENT:")
print(top_student)

#Step 6:save the DATA FRAME TO csv file
df.to_csv('student_scores.CSV',index=False)
print("/n DATA saved to student_scores.csv")