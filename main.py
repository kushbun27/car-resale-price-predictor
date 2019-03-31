
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#get_ipython().magic('matplotlib inline')


# In[1025]:
def carModel(List) :
    print("reached here")
    data = pd.read_csv('onlycar1.csv')


    # In[1026]:

    data.tail()


    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[1027]:

    #data.info()


    '''# In[1028]:

    sns.pairplot(data)


    # In[1029]:

    sns.distplot(data['Selling_Price'],bins=100)


    # In[1032]:

    sns.distplot(data['Present_Price'],bins=100)


    # In[1034]:

    sns.heatmap(data.corr())


    # In[1035]:

    plt.scatter(data['Year'],data['Kms_Driven'])'''


    # In[1058]:

    from sklearn import preprocessing
    from sklearn.preprocessing import LabelEncoder


    # In[1059]:

    label_encoder = preprocessing.LabelEncoder()
    trans = label_encoder.fit_transform(data['Transmission'])
    #1 manual 0 auto
    fuel = label_encoder.fit_transform(data['Fuel_Type'])
    #2 petrol 1 diesel 0 cng
    data['Transmission'] = trans
    data['Fuel_Type'] = fuel
    data.head(5)


    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[ ]:




    # In[1060]:

    X = data[[ 'Year', 'Present_Price', 'Kms_Driven','Fuel_Type','Transmission', 'Owner']]
    y = data['Selling_Price']


    # In[1061]:

    from sklearn.model_selection import train_test_split


    # In[1102]:

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state = 42)


    # In[1103]:

    from sklearn.linear_model import LinearRegression


    # In[1104]:

    lm = LinearRegression()


    # In[1105]:

    lm.fit(X_train,y_train)


    # In[1106]:

    print(lm.intercept_)


    # In[1107]:

    lm.score(X_train,y_train)

    print('i reached here')
    # In[1108]:

    print(lm.score(X_test,y_test))


    # In[1101]:

    #predictions = lm.predict(X_test)


    # In[1070]:

    X_test


    # In[ ]:




    # In[1071]:

    y_test


    # In[ ]:




    # In[1072]:

    #predictions


    # In[1073]:

    #sns.regplot(y_test,predictions)


    # In[1074]:

    #sns.distplot((y_test-predictions),bins=30);


    # In[1075]:
    print("i reached here")
    coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
    coeff_df


    # In[1076]:

    x_test = np.array(List)


    # In[1077]:

    prediction = x_test.reshape(1,-1)
    x_test

    r = lm.predict(prediction)[0]
    #r = r*100000

    if r<=0.1*List[1] :
        r1 = .1*List[1]
        r2 = r1+.05*r1
        jj = [r1,'to',r2]

    elif r >= .9*List[1] :
        r2 = .9*List[1]
        r1 = r2-r2*.05
        jj = [r1,'to',r2]
    
    elif List[1] < 5 : 
        r1 = r+r*.15
        jj = [r,'to',r1]

    else :
        r1 = r-r*.05
        r2 = r+r*.05
        jj = [r1,'to',r2]
    # In[1078]:

    return(jj)

"---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"




def bikeModel(List) :
    data2 = pd.read_csv('bike data.csv')
    print("i reached here")

    # In[7]:


    data2.shape


    # In[8]:


    data2.head()


    # In[9]:


    data2.describe()


    # In[10]:


    plt.scatter(data2['Year'],data2['Selling_Price'],cmap='coolwarm',edgecolors = 'red')
    plt.xlabel('Year')
    plt.ylabel('Selling_Price')


    # In[11]:


    from sklearn import preprocessing
    from sklearn.preprocessing import LabelEncoder


    # In[35]:


    label_encoder = preprocessing.LabelEncoder()
    trans = label_encoder.fit_transform(data2['Transmission'])
    #1 manual 0 auto
    fuel = label_encoder.fit_transform(data2['Fuel_Type'])
    #2 petrol 1 diesel 0 cng
    data2['Transmission'] = trans
    data2['Fuel_Type'] = fuel
    data2.head(7)


    # In[13]:


    X1 = data2[[ 'Year', 'Present_Price', 'Kms_Driven','Fuel_Type', 'Transmission', 'Owner']]
    y1 = data2['Selling_Price']
    from sklearn.model_selection import train_test_split
    print("i reached here")

    # In[14]:


    X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.2,random_state = 101)


    # In[15]:


    from sklearn.linear_model import LinearRegression


    # In[16]:


    lm = LinearRegression()


    # In[17]:


    lm.fit(X_train,y_train)


    # In[18]:


    print(lm.intercept_)


    # In[19]:


    lm.score(X_train,y_train)


    # In[20]:


    print('SCORE                     ',lm.score(X_test,y_test))


    # In[21]:


    x_test = np.array(List)


    # In[22]:


    x_test = x_test.reshape(1,-1)
    x_test


    # In[30]:
    print("i reached here lulla bin lulaa")

    '''predictions = lm.predict(X_test)


    # In[31]:


    sns.regplot(y_test,predictions)


    # In[32]:


    predictions'''


    # In[33]:


    y_test


    # In[34]:


    X_test


    # In[36]:


   # sns.distplot((y_test-predictions),bins=30);


    # In[24]:


    #coeff_df = pd.DataFrame(lm.coef_, X1.columns, columns=['Coefficient'])  
    #coeff_df


    # In[25]:


    prediction = lm.predict(x_test)
    print(prediction)

    r = prediction[0]
    #r = r*100000

    
    if r<=0.1*List[1] :
        r1 = .1*List[1]
        r2 = r1+.05*r1
        jj = [r1,'to',r2]

    elif r >= .85*List[1] :
        r2 = .85*List[1]
        r1 = r2-r2*.05
        jj = [r1,'to',r2]
    
   

    else :
        r1 = r-r*.05
        r2 = r
        jj = [r1,'to',r2]

    return(jj)




