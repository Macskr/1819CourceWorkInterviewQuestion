# 1819CourceWorkInterviewQuestion
repository for files relating to 1819 Interview Question Course Work 


PROGRESS:
- Randomly Generated Data
   - IMPROVEMENTS 
        - Number of data imput will be exactly as requested
        - The number of individuals which can be created is now 18239^98 rather than the previous 18239 ( Look: Main-Improved-Data-Gen ) 
        - user can now specify ammount of people generated 
   - ISSUES
        -    the for loop responsible for generating an individual creates one identical one already in the dictionary. this means that if a large set is requested (10000) the returned file could only contain much less (~7000)  [RESOLVED]
        -    the generation is limited to the ammount of names avalible (~18000), to fix this may turn key of the individual to a set ( {name,surname,age}  OR  {name,age} ) [RESOLVED]

- Conversion back to Dict
   - Features
      - returns time taken for conversion 
      - allows user to specify which file to convert 
      - converts file back to dict 
      
