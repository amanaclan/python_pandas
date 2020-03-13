import pandas as pd 

##----START_METHOD 1----##
rangkings = {'test':['India','South Africa','England','New Zealand','Australia'],
                'odi':['England','India','New Zealand','South Africa','Pakistan'],
                't20':['Pakistan','India','Australia','England','New Zealand']}
rangkings_pd = pd.DataFrame(rangkings) ###-----> CONVERT DATABASE TO DATAFRAME

print(rangkings_pd)

rangkings_pd.rename(columns={'test':'RACUN'}, inplace =True) ###---->RENAME COLUMN

print ("\nAfter modifying first column:\n", rangkings_pd.columns)
print(rangkings_pd)

##----END_METHOD 1----##

##----START_METHOD 2---##
rangkings_pd.columns = ['TEST','ODI','T-20']

print(rangkings_pd)

##---END_METHOD 2---###