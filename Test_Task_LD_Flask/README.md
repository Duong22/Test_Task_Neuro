# Test_Task_LD_Flask
### 1. Running on local machine
- Clone this repo
- Create a conda environment for python==3.8
- Install required packages

        pip install -r requirements.txt

**Without Docker**
- cd to repo where the `app.py` file is located
- Run the command

        python app.py

**With Docker**
- cd to repo where the `Dockerfile` file is located
- Build the test_task_ld_flask:latest image from `Dockerfile`

        docker build -t test_task_ld_flask:latest .

- Run the image which has been build

        docker run -p 5002:5002 test_task_ld_flask:latest

### 2. Endpoint `/finddistance`
- Request format:

        {"address": "Ha Noi, Viet Nam"}

- Example curl:

        curl --location --request POST 'http://0.0.0.0:5002/finddistance' \
            --header 'Content-Type: application/json' \
            --data-raw '{"address": "Ha Noi, Viet Nam"}'

- Result save in result.log file

### 2. Testing flask functions
- cd to repo where `app.py` is located
- Run the command

        python tests/basic_test.py
