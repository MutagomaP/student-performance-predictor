# Student ML API Deployment Guide

## Deployment Options

### Option 1: Docker Compose (Recommended)

#### Prerequisites
- Docker and Docker Compose installed
- Git

#### Steps

1. **Clone and navigate to project**
```bash
cd student_ml
```

2. **Build and run with Docker Compose**
```bash
docker-compose up --build
```

The API will be available at:
- API: http://localhost:8000/api/predict/
- Swagger: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/
- Admin: http://localhost:8000/admin/

3. **Stop the services**
```bash
docker-compose down
```

---

### Option 2: Heroku Deployment

#### Prerequisites
- Heroku CLI installed
- Heroku account

#### Steps

1. **Create Procfile**
```bash
echo "web: gunicorn student_ml.wsgi --log-file -" > Procfile
```

2. **Create runtime.txt**
```bash
echo "python-3.11.0" > runtime.txt
```

3. **Login to Heroku**
```bash
heroku login
```

4. **Create Heroku app**
```bash
heroku create your-app-name
```

5. **Add PostgreSQL addon**
```bash
heroku addons:create heroku-postgresql:mini
```

6. **Set environment variables**
```bash
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS='your-app-name.herokuapp.com'
```

7. **Deploy**
```bash
git push heroku main
```

8. **Run migrations**
```bash
heroku run python manage.py migrate
```

---

### Option 3: AWS EC2 Deployment

#### Prerequisites
- AWS account
- EC2 instance (Ubuntu 22.04)
- SSH access to instance

#### Steps

1. **SSH into EC2 instance**
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

2. **Install dependencies**
```bash
sudo apt update
sudo apt install python3-pip python3-venv postgresql nginx -y
```

3. **Clone repository**
```bash
git clone your-repo-url
cd student_ml
```

4. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

5. **Set up PostgreSQL**
```bash
sudo -u postgres createdb student_ml_db
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'your-password';"
```

6. **Create .env file**
```bash
cp .env.example .env
# Edit .env with your values
nano .env
```

7. **Run migrations**
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

8. **Set up Gunicorn service**
```bash
sudo nano /etc/systemd/system/student_ml.service
```

Add:
```ini
[Unit]
Description=Student ML API
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/student_ml
Environment="PATH=/home/ubuntu/student_ml/venv/bin"
ExecStart=/home/ubuntu/student_ml/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 student_ml.wsgi:application

[Install]
WantedBy=multi-user.target
```

9. **Start service**
```bash
sudo systemctl start student_ml
sudo systemctl enable student_ml
```

10. **Configure Nginx**
```bash
sudo nano /etc/nginx/sites-available/student_ml
```

Add:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /home/ubuntu/student_ml/staticfiles/;
    }
}
```

11. **Enable site**
```bash
sudo ln -s /etc/nginx/sites-available/student_ml /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

### Option 4: Railway Deployment

#### Prerequisites
- Railway account
- GitHub repository

#### Steps

1. **Go to Railway.app**
2. **Click "New Project"**
3. **Select "Deploy from GitHub repo"**
4. **Add PostgreSQL database**
5. **Set environment variables in Railway dashboard**
6. **Deploy automatically on push**

---

## Testing the Deployment

### Test the API
```bash
curl -X POST http://your-domain/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{
    "hours_studied": 8,
    "previous_scores": 85,
    "extracurricular": true,
    "sleep_hours": 7,
    "sample_papers": 5
  }'
```

### Access Swagger Documentation
Visit: `http://your-domain/swagger/`

---

## Environment Variables

Required environment variables:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DB_NAME`: Database name
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_HOST`: Database host
- `DB_PORT`: Database port

---

## Security Checklist

- [ ] Set DEBUG=False in production
- [ ] Use strong SECRET_KEY
- [ ] Configure ALLOWED_HOSTS properly
- [ ] Use HTTPS in production
- [ ] Set up proper database backups
- [ ] Use environment variables for sensitive data
- [ ] Enable CSRF protection
- [ ] Set up monitoring and logging
