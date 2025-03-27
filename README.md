# WebPythonApp

This is a small Python web app for testing purposes, deployed on an EC2 instance.

## Contributors
 Jamell Alvarez

## Setup Instructions

### 1. Launch an EC2 Instance
Use Amazon Linux and ensure HTTP traffic is allowed in the security group.

### 2. Clone the Repository
git clone <your-repo-url>  
cd WebPythonApp  

### 3. Create and Activate a Virtual Environment
python3 -m venv .venv  
source .venv/bin/activate  

### 4. Install Dependencies
pip install -r requirements.txt  

### 5. Run the App with Gunicorn on Port 80
sudo /home/**your-ec2-user**/WebPythonApp/.venv/bin/gunicorn --bind 0.0.0.0:80 app:app 



