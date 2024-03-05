1. Install the required packages:

bash
pip install fastapi uvicorn transformers

pip install torch --index-url https://download.pytorch.org/whl/cpu

2. git clone git@github.com:Nekhaenko/demo_deploy.git
3. Run the application:
    bash
    uvicorn main:app --reload