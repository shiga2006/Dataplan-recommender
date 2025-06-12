Title: DataPlan Recommender

ABSTRACT
This project presents the development of a machine learning based Data Plan Recommender system, designed to personalize data plan suggestions based on user-specific attributes such as gender, occupation, location, age, and current plans on the user interface platform. Traditional methods of selecting data plans often fail to address users' evolving needs. By leveraging machine learning algorithms like CatBoost and XGBoost, the system predicts the most suitable data plan, and cost for each user. Integrated with a user-friendly Flask-based front-end and supported by a MongoDB backend, the system provides a seamless experience for users to explore personalized recommendations. The recommendation engine processes historical user data, analyzes trends in network usage, and provides tailored plan suggestions. By analyzing real-world data consumption behaviors, the system aids in reducing cost inefficiencies while ensuring uninterrupted internet access. The results demonstrate improved accuracy in predicting user preferences, leading to enhanced customer satisfaction and optimized network provider offerings.

DATASET
The dataset includes various attributes related to user demographics, device usage, and network preferences. The goal of this study is to identify key trends in data consumption, preferred network providers, and the cost-effectiveness of different network plans.
The dataset consists of the following attributes:
●Personal Details: Name, Age, Mobile Number, Password
●Occupation: IT Sector, Doctor, Teacher, etc.
●Location: Various city names
●Usage Data: Daily Usage in GB and MB, Monthly Usage in GB
●Device Type: Tablet, Smartphone, Television, etc.
●Network Preferences: Preferred Network (4G/5G), SIM Type (BSNL, Airtel, VI)
●Package Details: Network Package, Data Limit, and Package Cost

METHODOLOGY
![image](https://github.com/user-attachments/assets/bce7ff69-9c73-4508-85c8-83cb82682525)

TECH STACK
Layer	Technology
Backend	Flask(Python)
Database	MongoDB + PyMongo
Machine Learning	Sckit-learn, CatBoost, Pandas
Frontend	HTML, CSS, Javascript, Jinja2
API Handling	Flask + JSON

RESULTS
The developed system successfully analyzes user demographics and historical usage data to generate personalized data plan recommendations. The results highlight the following key findings:
●Prediction Accuracy: The machine learning models, including CatBoost and XGBoost, effectively predict suitable data limits, plans, and costs with high accuracy.
●User Engagement: The interactive front-end allows users to seamlessly receive and compare suggested plans, enhancing user satisfaction.
●Plan Optimization: Users receive recommendations that balance cost and data usage efficiency, reducing unnecessary expenses while ensuring adequate data availability.
●Network Provider Insights: The analysis provides valuable data for network providers to refine their pricing strategies and enhance service quality.

SNAPSHOTS
![image](https://github.com/user-attachments/assets/c50de068-9c07-4fc5-9acd-77e1807619fc)
![image](https://github.com/user-attachments/assets/4f639b44-43c7-49de-9f2d-53f761b45b7c)
![image](https://github.com/user-attachments/assets/45597dbf-c6dd-4d0a-bf60-aa204a5376fd)
![image](https://github.com/user-attachments/assets/4a22a2db-3909-47ac-bc83-b179644215ab)
![image](https://github.com/user-attachments/assets/fe502958-ec46-4999-af18-79653188fd0d)
![image](https://github.com/user-attachments/assets/ae72c66a-68f2-4665-843a-2a2aff64ecf8)
![image](https://github.com/user-attachments/assets/3aa55c1e-fb75-4d74-9acd-3c8ed19ea849)

DEMO VIDEO


