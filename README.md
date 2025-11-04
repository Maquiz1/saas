# Create project directory
mkdir -p ~/projects/saas
cd ~/projects/saas

# macos/linux: Create and activate a virtual environment
python3 -m venv venv-saas
source venv-saas/bin/activate

# windows: Create and activate a virtual environment
c:\Python312\python.exe -m venv venv-saas
.\venv-saas\Scripts\activate

# Create requirements.txt
echo "Django>=5.0,<5.1" >> requirements.txt
echo "gunicorn" >> requirements.txt

# install requirements
pip install pip --upgrade
pip install -r requirements.txt

# Start the django project
mkdir -p saas
cd saas
django-admin startproject src .