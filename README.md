# Convert Machine learning models in Python to APIs

This is a sample project to convert a machine learning (ML) algorithm in Python Jupyter notebooks to APIs.

#### Why use APIs?
Most of the ML models are built using Python or R to take advantage of the wide range of libraries. But end-users of the ML models are software developers who use a different technology stack such as .Net, JAVA, C#, etc. 
One way to solve this problem is by developing the ML application in the same technology used for software development, which consumes much more time and effort for development. Another way is to use APIs to set up a communication link between ML applications and Software applications. Some of the advantages for using APIs are,

  - Continuous Integration (CI)/ Continuous Deployment (CD) 
  - Efficiency
  - Integration

#### Flask

Flask is an open-source web services library in Python similar to Django. Flask framework comes with an inbuilt light-weighted web server which needs minimal configuration, and it can be controlled from the Python code.
To install,
```sh
pip install flask
```

#### Tutorial
The structure of the project should be in the following format,

- **ML model in .py or .ipynb** : ML algorithm/ analyses of the data
- **Saved model in pickle (.pkl or other format)** : Final model from the analysis saved as a pickle
- **flask application in .py** : Web services setup and code for prediction 

Once the prject is set up and the ML model is built, start the application using the following command in command prompt,
```sh
python flask_app.py
```
This command will start the server and the API url:port can be found in the output.

#### Testing
In order to test the API, use any API client like postman. start the flask server usig above command and post the parameters to API. The results can be achieved with in the client sent from the API built using the ML model.
Sample output of the Logistic regression used on the Titanic dataset is shown below,

![Sample result](https://user-images.githubusercontent.com/47184170/86269666-13cf5780-bb98-11ea-84c1-b1a00731b083.png?raw=true "Title")
