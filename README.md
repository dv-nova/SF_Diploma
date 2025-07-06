# Sf_data_science_Diploma_project

# Real estate price prediction


### Project description    
Perform EDA. Choose the features with the most impact on the price. Build a model. Build a web-server.


### Case to solve    
To develop a model for a real estate agency to outperform its competitors in terms of the speed and quality of transactions.



### Short summary of data
The dataset stores information on a range of features, including:
- 'status' — the status of the sale;
- 'private pool' and 'PrivatePool' — having an own pool;
- 'PropertyType' — the type of the property;
- 'street' — the address of the object;
- 'baths' — the number of bathrooms;
- 'homeFacts' — information about the construction of the facility (contains several types of information that affect the assessment of the facility);
- 'fireplace' — the availability of a fireplace;
- 'city' — the city;
- 'schools' — information about schools in the area;
- 'sqft' — area in square feet;
- 'zipcode' — postal code;
- 'beds' — the number of bedrooms;
- 'state' — the state;
- 'stories' — the number of floors;
- 'mls-id' and 'MlsId' — MLS identifier (Multiple Listing Service, multi-listing system);
- 'target' — the price of the property (the target variable that needs to be predicted).




### Project stages  
Study the structure of the data.
Pre-process and clean the dataset.
Perform EDA.
Choose the best model and perform training and prediction.


### Results:  

The code for data processing is here (https://github.com/dv-nova/SF_Diploma/blob/main/Diploma_real_estate_2025_07_06.ipynb)
Service example is here (https://github.com/dv-nova/SF_Diploma/blob/main/diploma_catboost_web_servise.py)


### Conclusions:  
All the tasks are solved. The model predicts with a 0.83% MAPE on both training and test data. The metrics improved nearly two times, compared to the baseline.

