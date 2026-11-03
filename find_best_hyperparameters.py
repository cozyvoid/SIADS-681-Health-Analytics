from sklearn.metrics import precision_recall_fscore_support,average_precision_score
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,f1_score
from fairlearn.reductions import ExponentiatedGradient, DemographicParity
from fairlearn.reductions import FalsePositiveRateParity, UtilityParity, TruePositiveRateParity


def get_predictions(X_train,y_train,X_test,\
        C= 1, penalty= "l2"):
    """ 
    Returns prediction label on testing data. 
    
    Parameters:
    X_train (Numpy Array-like): Training data.
    y_train (Numpy Array-like): Training labels.
    X_test (Numpy Array-like): Testing data.
    y_test (Numpy Array-like): Testing labels.
    C (INT): Regularizer parameter.
    penalty (str): Norm of the penality. 
    
    Returns:
    Predicted class labels for samples in X_test.
    """
    # initialize logistic regression with balanced class weights
    model = LogisticRegression(
        C=C,
        penalty=penalty,
        class_weight="balanced"
    )

    # train the model
    model.fit(X_train, y_train)

    # return predicted class labels
    return model.predict(X_test)
    pass
    
def get_predictions_prob(X_train,y_train,X_test,\
        C= 1, penalty= "l2",threshold = .5):
    """ 
    Returns prediction probability on testing data. 
    
    Parameters:
    X_train (Numpy Array-like): Training data.
    y_train (Numpy Array-like): Training labels.
    X_test (Numpy Array-like): Testing data.
    y_test (Numpy Array-like): Testing labels.
    C (INT): Regularizer parameter.
    penalty (str): Norm of the penalty. 
    threshold (INT or None): Threshold on probabilities
    
    Returns:
    Predicted class probability for samples in X_test.
    """
    # initialize logistic regression with balanced class weights
    model = LogisticRegression(
        C=C,
        penalty=penalty,
        class_weight="balanced"
    )

    # train the model using the training data
    model.fit(X_train, y_train)

    # return predicted probabilities for both classes
    predictions = model.predict_proba(X_test)

    return predictions
    pass

def get_predictions_threshold_label(X_train,y_train,X_test,\
        C= 1, penalty= "l2", threshold = .5):
    """ 
    Returns prediction label on testing data based on threshold. 
    
    Parameters:
    X_train (Numpy Array-like): Training data.
    y_train (Numpy Array-like): Training labels.
    X_test (Numpy Array-like): Testing data.
    y_test (Numpy Array-like): Testing labels.
    C (INT): Regularizer parameter.
    penalty (str): Norm of the penalty. 
    threshold (INT or None): Threshold on probabilities
    
    Returns:
    Predicted threshold class labels for samples in X_test.
    """
    # initialize logistic regression with balanced class weights
    model = LogisticRegression(
        C=C,
        penalty=penalty,
        class_weight="balanced"
    )

    # train the model
    model.fit(X_train, y_train)

    # predict probabilities for the positive class (stroke = 1)
    probabilities = model.predict_proba(X_test)[:, 1]

    # convert probabilities into binary labels using the threshold
    predictions = (probabilities >= threshold).astype(int)

    return predictions
    pass


def get_scores(X_train,y_train,X_test,y_test,metric, threshold=None,range_c=np.arange(-3,3,1)):
    """ 
    Calculate score on testing data for a given metric and threshold. 
    
    Parameters:
    X_train (Numpy Array-like): Training data.
    y_train (Numpy Array-like): Training labels.
    X_test (Numpy Array-like): Testing data.
    y_test (Numpy Array-like): Testing labels.
    metric (str): Score metric to use.
    threshold (INT or None): Threshold on probabilities
    
    Returns:
    score_dict (dict): A dictionary mapping choice of penalty and C with the calculated score.
    """
    # dictionary to store scores for each hyperparameter combination
    score_dict = {}
    
    # loop through regularization penalties
    for penalty in ["l2",None]:
        
        # loop through different values of C
        for c in [10**int(i) for i in range_c]:
            
            # if threshold-based predictions if threshold is provided
            if threshold is not None:
                preds = get_predictions_threshold_label(\
                    X_train,y_train,X_test,\
                    C=c,penalty=penalty,\
                    threshold=threshold)
            else:
                # use class labels for accuracy and F1
                if(metric in ["f1","accuracy"]):
                    preds = get_predictions(\
                        X_train,y_train,X_test,\
                        C=c,penalty=penalty)
                # use probabilities for average precision
                else:
                    preds = get_predictions_prob(\
                        X_train,y_train,X_test,\
                        C=c,penalty=penalty,\
                        threshold=threshold)
            # calculate accuracy
            if metric == "accuracy":
                score = accuracy_score(y_test,preds)
            # calculate F1-score    
            elif metric=="f1":
                score = f1_score(y_test,preds)
            # calculate average precision
            elif metric == "average_precision":
                score = average_precision_score(y_test, preds[:, 1])

            # store score for penalty and C combination
            score_dict["{}-{}".format(
                penalty, str(float(c))
            )]=score
    return score_dict


def run_gridsearch_all_evaluate_all(\
    pop_cv,dataset,metric,threshold=None):
    """ 
    Grid search for finding best hyperparameter when training and evaluating on
    all patient ids. 
    
    Parameters:
    pop_cv (dict): Data representing the whole population in K-folds.
    dataset (StrokeKaggle): A custom defined class that contains information about
                            the whole population.
    metric (str): Score metric to use.
    threshold (INT or None): Threshold on probabilities
    
    Returns:
    score (Python list): A list of tuples whose first element is choice of penalty and C
    in a string format for example ('penalty-C') and whose second element is the corresponding calculated score.
    The scores are in sorted order. 
    """
    scores = {}
    for k,v in pop_cv.items():
        X_train = dataset.X_std[pop_cv[k][0]]
        y_train = dataset.y.iloc[pop_cv[k][0]]
        X_test = dataset.X_std[pop_cv[k][1]]
        y_test = dataset.y.iloc[pop_cv[k][1]]
        fold_score =\
                get_scores\
                (X_train,y_train,X_test,y_test,metric,\
                threshold)
        for p,s in fold_score.items():
            if p not in scores:
                scores[p]=[]
            scores[p].append(s)
    norm_scores =  {k:np.array(v).mean() \
            for k,v in scores.items()}
    return sorted(norm_scores.items(),\
        key=(lambda x: x[1]),reverse=True)

def run_gridsearch_all_evaluate_group(group_specific_cv,\
        pop_cv,dataset,metric,threshold):
    """ 
    Grid search for finding best hyperparameter when training on all patient ids
    and evaluating the best hyperparameter on a specific group (particular age group). 
    
    Parameters:
    group_specific_cv (dict): K-folds where each fold representing data of a specific group. 
    pop_cv (dict): Data representing the whole population in K-folds.
    dataset (StrokeKaggle): A custom defined class that contains information about
                            the whole population.
    metric (str): Score metric to use.
    threshold (INT or None): Threshold on probabilities
    
    Returns:
    score (tuple): A tuples whose first element is choice of penalty and C
    in a string format for example ('penalty-C') and second element is the corresponding calculated score.
    
    NOTE: Please make sure C is python float datatype before converting it into string.
    """
    pass

def run_gridsearch_on_group_only(\
        group_cv,dataset,metric,threshold):
    """ 
    Grid search for finding best hyperparameter when training and evaluating 
    on a specific group (particular age group). 
    
    Parameters:
    group_cv (dict): K-folds where each fold representing data of a specific group. 
    dataset (StrokeKaggle): A custom defined class that contains information about
                            the whole population.
    metric (str): Score metric to use.
    threshold (INT or None): Threshold on probabilities
    
    Returns:
    score_dict (Python list): A list of tuples whose first element is choice of penalty and C
    in a string format for example ('penalty-C') and second element is the corresponding calculated score.
    
    NOTE: Please make sure C is python float datatype before converting it into string.
    """
    pass


def get_constrained_models(pop_cv,dataset):
    """
    Get constrained model trained on whole population for each fold
    
    Parameters:
    pop_cv (dict): Data representing the whole population in K-folds.
    dataset (StrokeKaggle): A custom defined class that contains information about
                            the whole population.
    
    Returns:
    models (dict): A dictionary containing trained model for each fold where keys represent
    the folds. 
    """

    models = {}
    for k in pop_cv.keys():
        X_train = dataset.X_std[pop_cv[k][0]]
        y_train = dataset.y.iloc[pop_cv[k][0]]
        ages = dataset.total_dataset['age_num'][\
                pop_cv[k][0]]
        constraint = TruePositiveRateParity()
        our_model = LogisticRegression(class_weight="balanced",penalty='l2',C=0.1)
        mitigator = ExponentiatedGradient(our_model, constraint)
        mitigator.fit(X_train,y_train, sensitive_features=ages)
        models[k]=mitigator
    return models


def get_scores_constrained_with_model(model,X_test,y_test):
    """
    Get score for constrained model trained on whole population for each fold
    
    Parameters:
    model: Trained ExponentiatedGradient model
    X_test (Numpy Array-like): Testing data.
    y_test (Numpy Array-like): Testing labels.
    
    Returns:
    score (float): metric score evaluated on testing data with the trained model.
    """
    score_dict = {}
    preds = model._pmf_predict(X_test)
    score = average_precision_score(y_test,preds[:,1])
    return score

def get_best_hyperparameters_weighted(pop_cv, dataset, weights_dict):
    """ 
    Grid search for finding best hyperparameter when training and evaluating 
    on the whole dataset. 
    
    Parameters:
    pop_cv (dict): Data representing the whole population in K-folds.
    dataset (StrokeKaggle): A custom defined class that contains information about
                            the whole population.
    weights_dict (dict): weights incorporating information about groups.
    
    Returns:
    C (float): Best regularizer parameter.
    penalty (str): Best norm penalty
    """
    C, penalty=None, None
    pass
    
    return C, penalty

def run_gridsearch_all_evaluate_group_resampled(group_cv, pop_cv, dataset, weights_dict, C, penalty):
    """ 
    Grid search for finding best hyperparameter when training and evaluating 
    on a specific group (particular age group). 
    
    Parameters:
    group_cv (dict): K-folds where each fold representing data of a specific group. 
    pop_cv (dict): Data representing the whole population in K-folds.
    dataset (StrokeKaggle): A custom defined class that contains information about
                            the whole population.
    weights_dict (dict): weights incorporating information about groups.
    C (float): Best regularizer parameter.
    penalty (INT): Best norm penalty
    
    Returns:
    Return the average precision for the group who's group_cv you passed in. 
    
    Note :- In this function you will call get_precisions_weights k times, once for each fold.
    When you call get_precision make sure the training data depends on pop_cv, while the testing data 
    depends on group_cv. 
    """
    
    pass

def run_gridsearch_on_all_constrained_with_model(\
        group_cv,pop_cv,dataset):
    """ 
    Grid search for finding best hyperparameter for constrained model.
    
    Parameters:
    group_cv (dict): K-folds where each fold representing data of a specific group. 
    pop_cv (dict): Data representing the whole population in K-folds.
    dataset (StrokeKaggle): A custom defined class that contains information about
                            the whole population.

    Returns:
    scores (float): Average precision for the group who's group_cv you passed in. 
    
    Note :- In this function you will call get_scores_constrained_with_model once for each fold and use 
    the trained model for that fold returned by get_constrained_models. When you call 
    get_scores_constrained_with_model, make sure to pass the test data for that group only.
    """
    scores = []
    constrained_models = get_constrained_models(\
            pop_cv,dataset)
    #your code goes here 
    #you will use the models stored in constrained_models
    #to generate predictions
    pass

def instantiate_weights_dict(total_dataset):
    """
    Create a weight dictionary containing information about porporation of each group
    in entire population. Note that you can refer to the class video for the formula on
    how to calculate the weights.
    
    Parameters:
    total_dataset (pandas.DataFrame): Information containing about each age group
    
    Returns:
    weights_dict (dict): dictionary whose keys are age group and values are corresponding
    weights.
    """
    weights_dict = {}
    #your code goes here
    #nested dictionary
    return weights_dict

def get_predictions_weights(X_train,y_train,X_test,C= 1, penalty= "l2",weights_train=None,weights_test=None):
    """ 
    Returns prediction label probability on testing data. 
    
    Parameters:
    X_train (Numpy Array-like): Training data.
    y_train (Numpy Array-like): Training labels.
    X_test (Numpy Array-like): Testing data.
    C (float): Regularizer parameter.
    penalty (str): Norm of the penality. 
    weights_train (python list): weight of each training sample.
    weights_test (python list): weight of each testing sample.
    
    Returns:
    Predict class probability for samples in X_test.
    """
    our_model = LogisticRegression(penalty=penalty,C=C)
    our_model.fit(X_train,y_train,sample_weight=weights_train)
    return our_model.predict_proba(X_test)

def get_scores_weights(X_train,y_train,X_test,y_test,weights_train=None,weights_test=None):
    """ 
    Returns average precision score evaluated on testing data. 
    
    Parameters:
    X_train (Numpy Array-like): Training data.
    y_train (Numpy Array-like): Training labels.
    X_test (Numpy Array-like): Testing data.
    y_test (Numpy Array-like): Testing labels.

    weights_train (python list): weight of each training sample.
    weights_test (python list): weight of each testing sample.
    
    Returns:
    score_dict (dict): A dictionary mapping choice of penalty and C with the calculated score.
    """
    score_dict = {}
    for penalty in ["l2",None]:
        for c in [10**int(i) for i in np.arange(-2,2,1)]:
            preds = get_predictions_weights(X_train,y_train,X_test,\
                                    C=c,penalty=penalty,weights_train=weights_train,weights_test=weights_test)
            score = average_precision_score(y_test,preds[:,1])
            score_dict["{}-{}".format(penalty,str(c))]=score
    return score_dict

