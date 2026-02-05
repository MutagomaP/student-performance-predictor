#!/bin/bash

# Test script for realistic validation
API_URL=${1:-http://127.0.0.1:8000}

echo "🧪 Testing Realistic Validation for Student ML API"
echo "API URL: $API_URL"
echo ""

# Test 1: Impossible - More than 24 hours
echo "❌ Test 1: Impossible scenario (24 study + 1 sleep = 25 hours)"
curl -s -X POST "$API_URL/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{"hours_studied": 24, "previous_scores": 85, "extracurricular": true, "sleep_hours": 1, "sample_papers": 5}' | python3 -m json.tool
echo ""
echo ""

# Test 2: Unrealistic study hours
echo "❌ Test 2: Unrealistic study hours (18 hours)"
curl -s -X POST "$API_URL/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{"hours_studied": 18, "previous_scores": 85, "extracurricular": false, "sleep_hours": 5, "sample_papers": 5}' | python3 -m json.tool
echo ""
echo ""

# Test 3: Unsustainable (high study, low sleep)
echo "❌ Test 3: Unsustainable (14 hours study, 4 hours sleep)"
curl -s -X POST "$API_URL/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{"hours_studied": 14, "previous_scores": 85, "extracurricular": false, "sleep_hours": 4, "sample_papers": 5}' | python3 -m json.tool
echo ""
echo ""

# Test 4: Dangerously low sleep
echo "❌ Test 4: Dangerously low sleep (3 hours)"
curl -s -X POST "$API_URL/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{"hours_studied": 6, "previous_scores": 70, "extracurricular": false, "sleep_hours": 3, "sample_papers": 3}' | python3 -m json.tool
echo ""
echo ""

# Test 5: Excessive sleep
echo "❌ Test 5: Excessive sleep (15 hours)"
curl -s -X POST "$API_URL/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{"hours_studied": 5, "previous_scores": 70, "extracurricular": false, "sleep_hours": 15, "sample_papers": 3}' | python3 -m json.tool
echo ""
echo ""

# Test 6: Realistic - Excellent student
echo "✅ Test 6: Realistic - Excellent student"
curl -s -X POST "$API_URL/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{"hours_studied": 8, "previous_scores": 85, "extracurricular": true, "sleep_hours": 7, "sample_papers": 5}' | python3 -m json.tool
echo ""
echo ""

# Test 7: Realistic - Average student
echo "✅ Test 7: Realistic - Average student"
curl -s -X POST "$API_URL/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{"hours_studied": 5, "previous_scores": 70, "extracurricular": false, "sleep_hours": 7, "sample_papers": 3}' | python3 -m json.tool
echo ""
echo ""

# Test 8: Realistic - Struggling student with feedback
echo "✅ Test 8: Realistic - Struggling student (with improvement suggestions)"
curl -s -X POST "$API_URL/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{"hours_studied": 2, "previous_scores": 55, "extracurricular": false, "sleep_hours": 5, "sample_papers": 1}' | python3 -m json.tool
echo ""
echo ""

# Test 9: Realistic - Hardworking student
echo "✅ Test 9: Realistic - Hardworking student"
curl -s -X POST "$API_URL/api/predict/" \
  -H "Content-Type: application/json" \
  -d '{"hours_studied": 10, "previous_scores": 90, "extracurricular": true, "sleep_hours": 7, "sample_papers": 8}' | python3 -m json.tool
echo ""
echo ""

echo "✅ All tests completed!"
