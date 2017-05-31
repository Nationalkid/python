
# coding: utf-8

# #Cats and Dogs
import matplotlib
import matplotlib.pyplot as plt
import plotly.plotly as py
import pandas as pd
import seaborn as sns
import matplotlib.patches as mpatches

species = ["dog","dog","dog", "dog", "cat", "rabbit",
             "cat", "cat", "cat", "cat","dog", "cat",
             "cat", "cat", "cat","cat"]
sign = ["melena","melena","bloody diarrhea", "vomiting", "melena",
          "wattery diarrhea", "bloody diarrhea", "vomiting", "melena",
          "melena", "wattery diarrhea", "wattery diarrhea","wattery diarrhea",
          "bloody diarrhea", "bloody diarrhea","bloody diarrhea"]

is_positive = ["0","1","1","1","0","1","1","0","1","1","0","1","1","0","0","1"]

#Create a list
animal_list = {'sign': sign,'species' : species,'is_positive': is_positive}

#Or read from CSV
animal_list_csv = pd.read_csv('../data/GI_survey_results.csv')

#Create a data frame using the list. Use colmuns to specify the order
animal_df = pd.DataFrame(animal_list,
                         columns=['species', 'sign', 'is_positive'])

#subseting th dataframe: No rabbits allowed!
animal_df = animal_df.query('species != "rabbit" ')

#subseting th dataframe: No rabbits allowed!
count_tested = animal_df.groupby(['sign','species']).count()
count_tested = count_tested.reset_index()

count_positive = animal_df.query('is_positive == "1" ').groupby(['sign','species']).count()
count_positive = count_positive.reset_index()

all = pd.merge(count_tested,count_positive,on=['sign','species'],how='outer')
all = all.reset_index()
all.columns.values[3] = 'tested'
all.columns.values[4] = 'positive'
all.drop('index', axis=1, inplace=True)
print(all)
all = all.fillna(0)

#Metl to long format
all_melted = pd.melt(all,id_vars=['sign','species'])


# Markdown types are normal text, with different behaviors than code.
# A commennt : using "#" at the begining will make the comments below them as titles.

# In[199]:

#dog_plot = sns.countplot( y="sign",hue="is_positive", data=animal_df_dog)
#cat_plot = sns.countplot( y="sign",hue="is_positive", data=animal_df_cat)


# #Just like this

# $$\hat{f}(x) = \frac{1}{nh^d} \sum_{i=1}^n k\bigg(\frac{\norm{x-x_i}}{h}\bigg)$$

# $e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i$

# In[212]:

#Convert to dataframe
#all = pd.DataFrame(all)
print(all_melted)
all_pivot = pd.DataFrame(all_melted)

#Pivot table
#all_pivot.reset_index(level=2, drop=True,inplace=True)
all_pivot = pd.pivot_table(all_pivot,index=['sign'], columns=['species','variable'],values='value')
#remove top level of multiindex
#all_pivot.columns = all_pivot.columns.droplevel(0)
print(all_pivot)

print(all_pivot.columns)
#reset multicolumns
all_pivot.columns = ['_'.join(col).strip() for col in all_pivot.columns.values]
all_pivot = all_pivot.reset_index()

print(all_pivot.columns)

#all_pivot = all_pivot.reset_index()
    # 'a' : key on which to get cross section
    # axis=1 : get cross section of column
    # drop_level=True : returns cross section without the multilevel index

print(all_pivot)


# Must convert to numeric...otherwise, it will consider it as factor
# and will count frenquency of levels inside
pd.to_numeric(all_melted.value, errors='coerce')



# Setting the main plot first
sns.set(font_scale=2)
sns.set_style("white")
sns.despine()

plt.figure()
#Plot
g = sns.factorplot(y="sign",x="value",hue="variable",
                   col="species",col_order=["dog","cat"],kind="bar",
                   data=all_melted,size=9,
                   aspect=1,legend=False)
g.set_axis_labels("", "Survival Rate")
#g.set_titles("[]")
g.set_titles("{col_name}")
g.fig.suptitle('Number of dogs and cats')

#Some Matplot methods to help on graph plot customization
plt.subplots_adjust(top=0.85)
plt.legend(loc='lower right')

#More pararms at https://matplotlib.org/api/legend_api.html

plt.figure()
all['percent_pos'] = all.positive / all.tested * 100
all.sort_values(by=['percent_pos'],ascending=False)

print(all)
#A second plot
f = sns.factorplot(y='sign',x='percent_pos',hue='species',
                   data=all,kind="bar",size=9,aspect=1,legend=True)

#Some Matplot methods to help on graph plot customization

plt.subplots_adjust(top=0.85)
#plt.legend(loc='lower right')
#More pararms at https://matplotlib.org/api/legend_api.html



# In[ ]:




# In[ ]:
