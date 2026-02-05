# 🚀 Render Quick Start (5 Minutes)

## What You'll Get
A live, public URL like: `https://student-ml-api.onrender.com`

People can test your API at: `https://your-app.onrender.com/swagger/`

## Steps

### 1. Push to GitHub (2 min)
```bash
cd student_ml
git init
git add .
git commit -m "Student ML API"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/student-ml-api.git
git push -u origin main
```

### 2. Deploy on Render (3 min)

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repo
4. Click **"Apply"**
5. Wait 5-10 minutes for deployment

### 3. Set ALLOWED_HOSTS

1. Go to your web service in Render
2. Click **"Environment"**
3. Add variable:
   - Key: `ALLOWED_HOSTS`
   - Value: `your-app-name.onrender.com`
4. Click **"Save Changes"**

### 4. Done! 🎉

Your API is live at:
- **Swagger**: `https://your-app-name.onrender.com/swagger/`
- **API**: `https://your-app-name.onrender.com/api/predict/`

## Test It

### In Browser:
Visit: `https://your-app-name.onrender.com/swagger/`

### With cURL:
```bash
curl -X POST https://your-app-name.onrender.com/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{
    "hours_studied": 8,
    "previous_scores": 85,
    "extracurricular": true,
    "sleep_hours": 7,
    "sample_papers": 5
  }'
```

## Share With Others

Send them this link:
`https://your-app-name.onrender.com/swagger/`

They can test your ML model directly in the browser!

## Important

⚠️ **Free tier spins down after 15 min of inactivity**
- First request after sleep takes ~30 seconds
- Perfect for demos and testing!

## Need More Details?

See [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for full guide.
