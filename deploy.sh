#!/bin/bash

echo "🚀 Starting Student ML API Deployment..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"

# Build and start containers
echo "📦 Building Docker containers..."
docker-compose build

echo "🔄 Starting services..."
docker-compose up -d

echo "⏳ Waiting for database to be ready..."
sleep 10

echo "🗄️  Running migrations..."
docker-compose exec web python manage.py migrate

echo "✅ Deployment complete!"
echo ""
echo "📍 Your API is now running at:"
echo "   - API: http://localhost:8000/api/predict/"
echo "   - Swagger: http://localhost:8000/swagger/"
echo "   - ReDoc: http://localhost:8000/redoc/"
echo "   - Admin: http://localhost:8000/admin/"
echo ""
echo "To stop the services, run: docker-compose down"
