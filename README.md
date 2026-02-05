# Student Performance ML API

A Django REST API that predicts student performance using machine learning based on study habits, previous scores, and other factors.

## 🚀 Want a Public URL for Testing?

**👉 [START HERE](START_HERE.md) - Deploy in 6 minutes!**

Get a free public URL like: `https://your-app.onrender.com/swagger/`

## 🎯 Live Demo

**Want to deploy and share with others?** 

Deploy to Render in 5 minutes and get a public URL!

👉 **[Quick Deploy Guide](RENDER_QUICKSTART.md)**

## Features

- 🤖 Machine Learning prediction endpoint
- 📊 PostgreSQL database
- 📚 Swagger/OpenAPI documentation
- 🐳 Docker support
- 🔒 Production-ready configuration
- 🌐 Easy deployment to Render (free tier available)
- ✅ **Realistic validation** - Rejects impossible scenarios (24hr study days, etc.)
- 💡 **Personalized feedback** - Get actionable suggestions for improvement
- 🎯 **Smart predictions** - Performance scores capped at 0-100%

## Quick Start

### Using Docker (Recommended)

```bash
./deploy.sh
```

Or manually:

```bash
docker-compose up --build
```

### Local Development

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Set up PostgreSQL**
```bash
sudo -u postgres createdb student_ml_db
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'password';"
```

3. **Run migrations**
```bash
python manage.py migrate
```

4. **Start server**
```bash
python manage.py runserver
```

## API Endpoints

### Predict Performance
**POST** `/api/predict/`

Request body:
```json
{
  "hours_studied": 8,
  "previous_scores": 85,
  "extracurricular": true,
  "sleep_hours": 7,
  "sample_papers": 5
}
```

Response:
```json
{
  "predicted_performance_index": 142.83
}
```

### Documentation
- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

## Web UI

This project now includes a simple web UI integrated into Django:

- Home UI: `http://localhost:8000/`
- It calls the existing prediction endpoint: `POST /api/predict/`

## Testing with cURL

```bash
curl -X POST http://localhost:8000/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{
    "hours_studied": 8,
    "previous_scores": 85,
    "extracurricular": true,
    "sleep_hours": 7,
    "sample_papers": 5
  }'
```

## Deployment

### 🌟 Render (Recommended for Public Demo)
Get a free public URL in 5 minutes!

```bash
# See RENDER_QUICKSTART.md for step-by-step guide
```

**Result**: `https://your-app.onrender.com/swagger/`

### Other Options
See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions for:
- Docker Compose (local)
- Heroku
- AWS EC2
- Railway

## Project Structure

```
student_ml/
├── performance/          # Main app
│   ├── models.py        # Database models
│   ├── views.py         # API views
│   ├── serializers.py   # DRF serializers
│   ├── urls.py          # App URLs
│   └── model.pkl        # ML model
├── student_ml/          # Project settings
│   ├── settings.py      # Django settings
│   └── urls.py          # Main URLs
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose config
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Tech Stack

- **Framework**: Django 6.0.1
- **API**: Django REST Framework 3.16.1
- **Database**: PostgreSQL
- **ML**: scikit-learn, joblib
- **Documentation**: drf-yasg (Swagger/OpenAPI)
- **Server**: Gunicorn
- **Containerization**: Docker

## License

MIT
