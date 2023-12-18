![olympic pic](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/cf028b16-985c-4eaf-befc-f587e02428e8)

## Title and Author

**Project Title:** Olympics Data Analysis Recommendation System

**Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang**

**Author Name:** Ranga Swamy Reddy Kappeta

**GitHub Profile:** ![GitHub](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy)

**LinkedIn Profile:** ![LinkedIn](https://www.linkedin.com/in/rangaswamyreddy-kappeta-a42b0b272/)

**PowerPoint Presentation:** https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/blob/main/docs/OLYMPIC%20DATA%20ANALYSIS.pptx

**YouTube Video:** https://youtu.be/z2CohKXF3T0

## Background

### What is it about?
The success of athletes from different nations might be tracked, trends in athletes' ages, heights, and weight could be examined over time, and it could be determined which sports and events had a higher chance of producing medals.

### Why does it matter?
The dataset is significant because it offers useful data for sports analysis, worldwide and national comparisons, historical research, and decision-making about the growth and development of sports. Additionally, it advances our knowledge of the Olympic Games and its relevance in the sports world.

### What are your research questions?
The outcome from research on the Olympic dataset may undoubtedly help us better comprehend the larger sociological and cultural shifts that have affected the world of sports throughout time, in addition to influencing sports policy and practice. They can also provide helpful information for organizing events, allocating resources, and encouraging people to participate in sports and physical exercise at the local, state, and federal levels.

## Data

### Data Size : 39.5 MB

### Data Shape : 271116 rows x 15 columns , 230 rows x 3 Columns

### Columns Details:
- **ID:** A unique identifier for each entry (athlete).
- **Name:** The name of the athlete.
- **Sex:** The gender of the athlete (M for male in this case).
- **Age:** The age of the athlete at the time of the event.
- **Height:** The height of the athlete.
- **Weight:** The weight of the athlete.
- **Team:** The national team that the athlete represents (in this case, China).
- **NOC:** The National Olympic Committee (NOC) code for the country (in this case, CHN for China).
- **Games:** A combination of the year and season of the Olympic Games (e.g., "1992 Summer" indicates the 1992 Summer Olympics).
- **Year:** The year of the Olympic Games (e.g., 1992).
- **Season:** The season of the Olympic Games (e.g., Summer).
- **City:** The host city of the Olympic Games (e.g., Barcelona).
- **Sport:** The sport in which the athlete is competing (e.g., Basketball).
- **Event:** The specific event or competition within the sport (e.g., Men's Basketball).
- **Medal:** an athlete won a medal in a particular event during the Olympics

## Target Variable
-  The "Medal" column is the target variable . The variable  I want to predict based on the values of other features.
-  I want to predict whether an athlete will win a Gold, Silver, or Bronze medal (multiclass classification), or whether they won a medal or not 
## Exploratory Data Analysis(EDA)

### Checking and removing Duplicates from the Data Set.
* Checking the duplicates from in the data set and we can see that there are no duplicates present in the data. So the data is free from duplicates.

### Analysing the data and Visualizations.
* Exploratory Data Analysis (EDA) involves a thorough examination of the dataset to uncover patterns, trends, and relationships. 
* In the upcoming section data cleaning, ensuring there are no duplicates on a detailed analysis, utilizing visualizations to gain insights into the Olympic dataset.
* The below is the distribution of these types throughout the data set.
* The image shows a graph that illustrates the growth of the number of countries in the world 
  from 1900 to 2000, with a peak of 190 countries in 2000. The graph demonstrates a steady 
  increase in the number of countries throughout the 20th century, with a slight decline in 
  the number of countries after 2000.
- ![Screenshot 2023-12-18 003144](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/98a92c94-9986-488c-8707-690f898478d1)

* The graphic includes a timeline with the years 1900, 1920, 1940, 1960, 1980, 2000, and 2020 
  marked, indicating the years in which the Olympic Games took place. The sports represented 
  in the graphic include Basketball, Judo, Football, Tug-Of-War, Athletics, Swimming, 
  Badminton, Sailing, Gymnastics, Art Competitions, Handball, Weightlifting, Wrestling, Water 
  Polo, and Hockey. Each sport is represented by a different color, allowing for easy 
  identification and comparison of their performance across the years.
![Screenshot 2023-12-18 003206](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/810e2b42-54c4-45a8-8a52-989aff65d753)
* The heatmap provides a visual representation of the correlation coefficients among numerical variables in the DataFrame. Utilizing a color scale where red indicates positive correlations and blue denotes negative ones, the chart is annotated with correlation values. Typically, stronger correlations gravitate towards -1 or 1, while weaker associations are closer to 0.
![Screenshot 2023-12-18 003255](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/22c24a57-6ded-4de5-8e06-e3378610bb72)
* This code utilizes Plotly Express to create a line plot. The x-axis represents the 'Year' column from the DataFrame, and the y-axis corresponds to the 'Medal' column. The resulting figure displays the trend or distribution of medals over the specified years.
 ![Screenshot 2023-12-18 003315](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/3e84dd1e-d5b9-4e19-8eea-050df050d8d5)
* The code employs Plotly Figure Factory (ff.create_distplot) to visualize the age distribution of athletes, distinguishing between overall participants and those who won gold, silver, or bronze medals. By excluding histograms and the rug plot, the resulting figure offers a clear and concise representation, shedding light on the age demographics in the context of different medal achievements. 
![Screenshot 2023-12-18 003339](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/ff9d06d5-26bc-4590-9a9b-492f3c20f8c2)
* This code utilizes Matplotlib and Seaborn to create a scatter plot with a specified figure size. It focuses on the 'Athletics' sport, showcasing the relationship between athletes' weight and height.
![Screenshot 2023-12-18 003409](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/9eab4cf5-f1e2-49e9-8693-2076c96597b8)
* This code generates a line plot using Plotly Express to illustrate the participation trends of male and female athletes over the years. The data is first grouped by gender ('M' and 'F') and then aggregated by counting the number of athletes for each gender in each year. The resulting figure provides a dynamic representation of the changing participation levels of male and female athletes in the dataset across different years.
![Screenshot 2023-12-18 003447](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/af6ed0a8-ae19-4408-9308-96aba3a81319)
* The code employs Plotly Express to generate a visually informative histogram illustrating the distribution of Gold, Silver, and Bronze medals over the years. By cleaning the dataset and using color-coded bars, the plot effectively communicates the count of each medal type across different years, enhancing the understanding of medal distribution patterns. The inclusion of a 90-degree tick angle improves the clarity of the visualization.
![Screenshot 2023-12-18 003457](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/891511b6-de1d-4d34-9f3c-ad0b527d35a4)
* This code leverages Plotly Express to create a bar chart visualizing the distribution of medals across the top 10 sports. The dataset is filtered to include only rows with non-null 'Medal' values, and the bar chart displays the count of medals for each sport. The x-axis represents the Medal Count, while the y-axis corresponds to different sports. The resulting visualization provides a clear comparison of medal distribution across the selected sports.
![Screenshot 2023-12-18 003514](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/11ec90d4-a012-45ba-8245-e9d9ce31b990)
* This code utilizes Plotly Express to create a pie chart illustrating the distribution of medals by gender. The dataset is filtered to include only rows with non-null 'Medal' values, and the pie chart represents the proportion of medals awarded to different genders. The resulting visualization offers a concise overview of how medals are distributed among male and female athletes.
 ![Screenshot 2023-12-18 003534](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/67087e65-8c3a-43fc-bdfa-d96c699bb6ad)
 

## Model Training:
* Model Selection involves choosing an appropriate machine learning algorithm based on the problem type (classification, regression) and data characteristics.
* Model Training is the process of using training data to educate the model, enabling it to identify patterns and relationships within the dataset.

### Linear Regression Model Evaluation:
* Evaluating the Linear Regression model involves assessing its performance metrics, such as Mean Squared Error (MSE) or R-squared, to measure the accuracy and effectiveness of predictions.
![Screenshot 2023-12-18 010245](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/1463fd8a-a12b-47de-b567-529937843a7f)

* This code utilizes Plotly to create a table visualizing the classification report for a logistic regression model. The classification report includes metrics such as precision, recall, and F1-score for each class. By converting the report into a DataFrame and presenting it as a table, it offers a comprehensive overview of the model's performance across different classes.
![Screenshot 2023-12-18 010557](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/654f2a5c-e471-4013-8f1d-ddb6f85e44bd)

 ### Random Forest Regression Model Evaluation:
* Evaluating the Random Forest Regression model entails examining its predictive performance using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), or R-squared. These metrics help assess how well the model captures the variance in the target variable and provides insights into its accuracy and effectiveness in making predictions.
![Screenshot 2023-12-18 010407](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/740143af-5f6d-4309-968c-428cf8b4dbcf)

* The code employs scikit-learn's confusion_matrix to create a table illustrating a classification model's performance. Converting this matrix into a Plotly heatmap provides a visual representation of predicted versus actual class labels, aiding in the assessment of accuracy and misclassifications.
![Screenshot 2023-12-18 010417](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/e235742d-25be-4bcb-908c-c8364c92b54c)

 ### Decision Tree Model Evaluation: 
* This code creates a machine learning pipeline incorporating data preprocessing (handled by the preprocessor) and a Decision Tree classifier. The pipeline is trained on the training set, and predictions are made on the test set. Evaluation metrics, including accuracy and a detailed classification report, are then computed and displayed to assess the Decision Tree model's performance. The goal is to provide a streamlined and reproducible workflow for training and evaluating the model.
  ![Screenshot 2023-12-18 010802](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/1e963165-22cd-405b-ac76-708c6d2a7615)
* The code utilizes scikit-learn's confusion_matrix to create a matrix for a Logistic Regression model. It transforms the matrix into a DataFrame for Plotly compatibility and generates a heatmap with Plotly Express, visually depicting the model's performance in predicting and classifying different labels.
![Screenshot 2023-12-18 010905](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/bb081dc4-1ce9-443d-b2e8-ca0c1a7d35c7)

 ### Support Vector Regression (SVR) Model Evaluation:
 
* The code creates a pipeline for a Support Vector Machine (SVM) classifier with preprocessing steps. It then trains the SVM model using the pipeline, makes predictions on the test set, and evaluates the model's accuracy and classification report. The resulting metrics provide insights into the SVM model's performance in classifying instances.
  ![Screenshot 2023-12-18 011056](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/a1d3559f-eba7-4997-b0d9-b0f656af9fb7)

* This code utilizes Plotly Express to create a confusion matrix figure for a Support Vector Machine (SVM) model. The confusion matrix is generated using scikit-learn's confusion_matrix function, and the resulting matrix is visualized as an interactive heatmap. The figure provides a clear representation of the model's performance by comparing predicted and actual class labels, aiding in the analysis of correct predictions and misclassifications across different classes.
  ![Screenshot 2023-12-18 011217](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/7dadfb56-8ea2-4c61-912f-6f7e4b556a26)

 ### KNN Model Evaluation:
* The provided code creates a full pipeline for preprocessing and the K-Nearest Neighbors (KNN) classifier using scikit-learn. The model is trained on the training set, and predictions are made on the test set. The accuracy and classification report metrics are then displayed to evaluate the performance of the KNN model.
  ![Screenshot 2023-12-18 011438](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/80210235-377c-4bf9-aa16-457644f2668a)
* A confusion matrix heatmap for the K-Nearest Neighbors (KNN) model. The confusion matrix is constructed using scikit-learn's confusion_matrix function, and the resulting matrix is visualized as an interactive heatmap. The figure aids in assessing the model's performance by illustrating predicted and actual class labels, providing insights into correct predictions and misclassifications across different
  ![Screenshot 2023-12-18 011535](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/914fe8fd-4a90-4b5e-8f68-53ab8ef09f22)

## Application of the Trained Models

### Medal Tally:
* Allows users to select a specific year and country to view the corresponding medal tally.
* Displays the gold, silver, bronze, and total medals won by the selected country in the chosen year.
![Screenshot 2023-11-14 185711](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/33a6d62d-fba1-4a7b-becd-bdf3e1800c5a)

![Screenshot 2023-12-18 013932](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/005b6505-61ef-428e-b249-3b0aded70b31)


### Overall Analysis:
* Provides overall statistics such as the number of editions, cities, sports, events, athletes, and nations.
* Presents a heatmap showing the number of events in different sports over the years.
Highlights the most successful athletes based on total medals won.
![Screenshot 2023-11-14 185344](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/78254935-ba80-4fc9-b9b7-1fa77997a7c5)

![Screenshot 2023-12-18 013732](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/881585e0-d13d-449f-9b97-c5505263ce72)

### Country wise Analysis:
* Enables users to explore medal tallies of a specific country over the years.
Displays a heatmap showcasing the country's performance in various sports across different editions.
* Lists the top 10 athletes from the selected country.
![Screenshot 2023-12-18 013656](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/76263fda-75c5-4c34-891a-a0d082dcd349)

 ![Screenshot 2023-12-18 013713](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/71e78b38-24ef-4168-9cc2-b3c68e9e83e2)
 
### Athletes Analysis:
* Features distribution plots showing the overall age distribution and age distribution of medalists.
* Presents age distribution based on sports, specifically focusing on gold medalists.
* Visualizes the relationship between height and weight of athletes in a selected sport.
* Includes a line chart comparing the participation of men and women over the years.
![Screenshot 2023-12-18 013754](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/2f03d4b9-bb53-4101-9df6-42625bc6c348)

![Screenshot 2023-12-18 013819](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/9d833687-aed6-42c9-bf87-e0a87eff7a5f)

![Screenshot 2023-12-18 013841](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/73565ba4-328a-4985-9cec-d599cbc70e6b)

![Screenshot 2023-12-18 013905](https://github.com/DATA-606-2023-FALL-TUESDAY/Kappeta-Rangaswamyreddy/assets/130123607/72818745-49e9-4aa5-8b99-5566498d2090)

### Conclusion
* In conclusion, this Streamlit app offers a user-friendly exploration of Olympic data, facilitating effortless comparisons of medal tallies across countries and years. Its comprehensive analysis spans diverse aspects of the Olympics, from editions and cities to detailed statistics on sports, events, athletes, and nations. The app allows users to uncover insights into country-wise performance, athlete demographics, and the interplay between physical attributes like height and weight in different sports. With gender participation trends, it provides a clear view of evolving representation over the years. Overall, this app serves as a powerful tool for enthusiasts and analysts, deepening understanding of historical Olympic trends.

## Future Predictions
* Technological Advancements: Continued integration of technology, including advanced analytics, wearable devices, and virtual/augmented reality, could enhance athlete performance, training methods, and the overall spectator experience.

* Sustainability Initiatives: Future Olympics may prioritize sustainability, with eco-friendly venues, renewable energy sources, and efforts to minimize the environmental impact.

* Global Inclusivity: The Olympics may see increased participation from nations and regions that were historically underrepresented, fostering a more inclusive and diverse sporting landscape.

* Changing Sports Landscape: The sports program could evolve to reflect changing global interests and emerging sports trends, ensuring the Olympics remain a reflection of contemporary sporting culture.

### References
* https://www.kaggle.com/code/matskovsky/starter-120-years-of-olympic-history-57e57856-4
* https://www.ijraset.com/research-paper/olympic-data-analysis-using-data-science
* https://ieeexplore.ieee.org/abstract/document/10084943
* https://towardsdatascience.com/120-years-of-olympic-games-how-to-analyze-and-visualize-the-history-with-r-3c2a5f3bf875
