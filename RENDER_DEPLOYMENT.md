# 🚀 Deploy to Render - Step by Step Guide

## Prerequisites
- GitHub account
- Render account (free at https://render.com)
- Your code pushed to GitHub

## Step 1: Push Code to GitHub

```bash
cd student_ml
git init
git add .
git commit -m "Initial commit - Student ML API"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/student-ml-api.git
git push -u origin main
```

## Step 2: Deploy on Render

### Option A: Using render.yaml (Automatic - Recommended)

1. **Go to Render Dashboard**
   - Visit https://dashboard.render.com
   - Click "New +" → "Blueprint"

2. **Connect Repository**
   - Connect your GitHub account
   - Select your `student-ml-api` repository
   - Click "Connect"

3. **Render will automatically:**
   - Create a PostgreSQL database
   - Create a web service
   - Set up environment variables
   - Deploy your app

4. **Set ALLOWED_HOSTS**
   - Go to your web service
   - Click "Environment"
   - Add: `ALLOWED_HOSTS` = `your-app-name.onrender.com`
   - Save changes

### Option B: Manual Setup

#### 2.1 Create PostgreSQL Database

1. Click "New +" → "PostgreSQL"
2. Fill in:
   - **Name**: `student-ml-db`
   - **Database**: `student_ml_db`
   - **User**: `student_ml_user`
   - **Region**: Oregon (or closest to you)
   - **Plan**: Free
3. Click "Create Database"
4. **Copy the Internal Database URL** (you'll need this)

#### 2.2 Create Web Service

1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Fill in:
   - **Name**: `student-ml-api`
   - **Region**: Oregon (same as database)
   - **Branch**: `main`
   - **Runtime**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn student_ml.wsgi:application`
   - **Plan**: Free

#### 2.3 Set Environment Variables

In the "Environment" tab, add:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `SECRET_KEY` | Generate a random key (click "Generate") |
| `DEBUG` | `False` |
| `DATABASE_URL` | Paste the Internal Database URL from step 2.1 |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` |

4. Click "Create Web Service"

## Step 3: Wait for Deployment

- Render will build and deploy your app (takes 5-10 minutes)
- Watch the logs for any errors
- Once deployed, you'll see "Live" status

## Step 4: Access Your API

Your API will be available at:
- **Base URL**: `https://your-app-name.onrender.com`
- **Swagger**: `https://your-app-name.onrender.com/swagger/`
- **ReDoc**: `https://your-app-name.onrender.com/redoc/`
- **Health Check**: `https://your-app-name.onrender.com/api/health/`
- **Predict**: `https://your-app-name.onrender.com/api/predict/`

## Step 5: Test Your Deployed API

### Using cURL:
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

### Using Postman:
1. Open Postman
2. Create new POST request
3. URL: `https://your-app-name.onrender.com/api/predict/`
4. Headers: `Content-Type: application/json`
5. Body (raw JSON):
```json
{
  "hours_studied": 8,
  "previous_scores": 85,
  "extracurricular": true,
  "sleep_hours": 7,
  "sample_papers": 5
}
```
6. Click Send

### Using Browser:
Visit `https://your-app-name.onrender.com/swagger/` and test directly!

## Important Notes

### Free Tier Limitations
- ⚠️ **Spins down after 15 minutes of inactivity**
- First request after inactivity takes ~30 seconds (cold start)
- 750 hours/month free (enough for testing)
- Database: 90 days retention, 1GB storage

### Keep Your Service Awake (Optional)
Use a service like UptimeRobot or Cron-job.org to ping your API every 10 minutes:
- Ping URL: `https://your-app-name.onrender.com/api/health/`

## Troubleshooting

### Build Failed?
- Check the build logs in Render dashboard
- Ensure all files are committed to GitHub
- Verify `requirements.txt` is correct

### Database Connection Error?
- Verify `DATABASE_URL` is set correctly
- Use the **Internal Database URL**, not External
- Check database is in the same region as web service

### Static Files Not Loading?
- Ensure `build.sh` runs `collectstatic`
- Check `STATIC_ROOT` is set in settings.py
- Verify WhiteNoise is in `MIDDLEWARE`

### App Not Responding?
- Check if service is "Live" in dashboard
- View logs for errors
- Verify `ALLOWED_HOSTS` includes your Render domain

## Updating Your App

After making changes:
```bash
git add .
git commit -m "Your update message"
git push origin main
```

Render will automatically redeploy!

## Monitoring

- **Logs**: View in Render dashboard under "Logs" tab
- **Metrics**: Check "Metrics" tab for CPU/Memory usage
- **Health Check**: Monitor `/api/health/` endpoint

## Sharing Your API

Share these links with others:
- 📚 **Documentation**: `https://your-app-name.onrender.com/swagger/`
- 🔗 **API Endpoint**: `https://your-app-name.onrender.com/api/predict/`
- 📖 **ReDoc**: `https://your-app-name.onrender.com/redoc/`

## Example Public URLs

After deployment, your URLs will look like:
- `https://student-ml-api.onrender.com/swagger/`
- `https://student-ml-api.onrender.com/api/predict/`

## Cost

- **Free Tier**: $0/month
  - Web service: 750 hours/month
  - PostgreSQL: 90 days, 1GB storage
  
- **Paid Tier**: $7/month (if you need always-on)
  - No spin down
  - Better performance
  - More resources

## Next Steps

1. ✅ Deploy to Render
2. ✅ Test all endpoints
3. ✅ Share Swagger URL with others
4. 📊 Monitor usage and logs
5. 🔄 Set up auto-ping to keep awake (optional)
6. 🎉 Enjoy your live ML API!

---

**Need Help?**
- Render Docs: https://render.com/docs
- Check logs in Render dashboard
- Review error messages carefully
