import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.model_selection import KFold,StratifiedKFold
from sklearn.model_selection import train_test_split
from mads.lib.path import assets

class StrokeKaggle():
    def __init__(self, assignment_1a=True):
        self.scaler = StandardScaler()
        self.random_state = 0 # results are sensitive to the random_state during train_test_split
        
        file = assets.find("assignment1/healthcare-dataset-stroke-archive.csv")
        df = pd.read_csv(file)
        if assignment_1a:
            a = ['infant', "preschool","child",\
                    "adolescent","adult","middle aged",\
                    'aged','80 and over']
            self.random_state = 4321
        else:
            df = df[df['age']>=45]
            df.reset_index(inplace=True, drop=True)
            a = ["middle aged","aged","80 and over"]
        
        df["bmi"] = df["bmi"].fillna(value=df["bmi"].mean())
        
        total_dataset = pd.get_dummies(df, columns=["smoking_status","Residence_type","work_type","ever_married","gender"])
        
        total_dataset["age_cat"]=total_dataset["age"].apply(self.mesh_age_categories)

        self.mesh_age_num = {a[i]:i for i in range(len(a))}

        total_dataset["age_num"]=total_dataset["age_cat"].map(self.mesh_age_num)
        
        train_df = total_dataset.drop(labels=["age_cat","age_num"],axis=1) 
        y =  train_df["stroke"]
        X =  train_df.loc[:, ( train_df.columns != "stroke") & (train_df.columns != "id")]
             
        self.y = y
        self.X = X
        self.total_dataset = total_dataset
        self.age_groups = total_dataset.groupby("age_cat")
        self.X_std  = self.scaler.fit_transform(self.X)

    def mesh_age_categories(self,age):
        if age<2:
            return 'infant'
        elif age>=2 and age<6:
            return "preschool"
        elif age>=6 and age<13:
            return "child"
        elif age>=13 and age<19:
            return "adolescent"
        elif age>=19 and age<45:
            return "adult"
        elif age>=45 and age<65:
            return "middle aged"
        elif age>=65 and age<80:
            return 'aged'
        elif age>=80:
            return '80 and over'

    def get_indices(self,df_indices):
        group_X = self.X.iloc[df_indices]
        group_y = self.y.iloc[df_indices]
        
        X_k_folds, X_hold_out, y_k_folds, y_hold_out = train_test_split(group_X, group_y,
                                                                        test_size=0.1, random_state=self.random_state)
        skf = StratifiedKFold(n_splits=5, random_state=0, shuffle=True)
        
        fold=0
        cv_dict = {}
        index_to_index = {i:j for i,j in zip(range(len(X_k_folds)), X_k_folds.index)}
        for train_index, test_index in skf.split(X_k_folds, y_k_folds):
            cv_dict[fold]=[[index_to_index[i] for i in train_index],
                           [index_to_index[i] for i in test_index]]
            fold = fold +1
        return cv_dict

    #Returns the train and test indices for each fold
    def get_all_train_test_indices_ng(self):
        cv_dict = self.get_indices(self.X.index)
        return  {},cv_dict
    
    #Returns a dictionary with train and test indices for each fold,
    #for each group
    def get_all_train_test_indices_group(self):
        group_train = {}
        train_all_folds = {i:[[],[]] for i in range(5)}
    
        for gkey in self.age_groups.groups:
            gdf = self.age_groups.get_group(gkey)
            cv_dict = self.get_indices(gdf.index)
            group_train[gkey]=cv_dict
            for k,v in cv_dict.items():
                train_all_folds[k][0].extend(v[0])
                train_all_folds[k][1].extend(v[1])
        return  group_train,train_all_folds