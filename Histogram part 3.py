#;====================================
#; Title:  Matplotlib Histogram part 3
#; Author: @AyemunHossain
#;====================================

#.....................>>> Weighted Histogram <<<...........................#
import matplotlib.pyplot as plt

ages_of_people=[22,55,62,45,21,22,34,42,
                42,4,99,102,110,120,121,122,
                130,111,115,112,80,75,65,54,
                44,43,42,48]

bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

wg = [6,-1,0,6,0,12,6,-5,4,0,0,
      1,11,8,0,-1,6,0,0,4,
      0,0,0,7,0,6,0,0]


plt.hist(ages_of_people,bins,histtype='stepfilled',
         rwidth=0.8,color="c",stacked =True,weights=wg,label="Age of people")

plt.title("American People's age histogram")
plt.legend()
plt.xlabel('Age Bin')
plt.ylabel('People\'s age')
plt.show()
