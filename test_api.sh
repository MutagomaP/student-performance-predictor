#!/bin/bash

# Test script for Student ML API
# Usage: ./test_api.sh https://your-app-name.onrender.com

if [ -z "$1" ]; then
    echo "Usage: ./test_api.sh <API_URL>"
    echo "Example: ./test_api.sh https://student-ml-api.onrender.com"
    exit 1
fi

API_URL=$1

echo "🧪 Testing Student ML API at: $API_URL"
echo ""

# Test 1: Health Check
echo "1️⃣ Testing Health Check..."
curl -s "$API_URL/api/health/" | python3 -m json.tool
echo ""
echo ""

# Test 2: Prediction with good student
echo "2️⃣ Testing Prediction (Good Student)..."
curl -s -X POST "$API_URL/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{
    "hours_studied": 8,
    "previous_scores": 85,
    "extracurricular": true,
    "sleep_hours": 7,
    "sample_papers": 5
  }' | python3 -m json.tool
echo ""
echo ""

# Test 3: Prediction with average student
echo "3️⃣ Testing Prediction (Average Student)..."
curl -s -X POST "$API_URL/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{
    "hours_studied": 5,
    "previous_scores": 70,
    "extracurricular": false,
    "sleep_hours": 6,
    "sample_papers": 3
  }' | python3 -m json.tool
echo ""
echo ""

# Test 4: Prediction with struggling student
echo "4️⃣ Testing Prediction (Struggling Student)..."
curl -s -X POST "$API_URL/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{
    "hours_studied": 2,
    "previous_scores": 50,
    "extracurricular": false,
    "sleep_hours": 4,
    "sample_papers": 1
  }' | python3 -m json.tool
echo ""
echo ""

echo "✅ All tests completed!"
echo ""
echo "📚 View full documentation at: $API_URL/swagger/"
