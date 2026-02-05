# ✅ Render Deployment Checklist

## Before You Deploy

- [ ] Code is working locally
- [ ] All files are committed
- [ ] GitHub repository is created
- [ ] Code is pushed to GitHub

## Files Ready for Render

- [x] `render.yaml` - Automatic deployment config
- [x] `build.sh` - Build script
- [x] `requirements.txt` - Python dependencies
- [x] `settings.py` - Updated with DATABASE_URL support
- [x] `model.pkl` - ML model in /performance/
- [x] WhiteNoise - For static files
- [x] Gunicorn - Production server

## Deployment Steps

1. [ ] Go to https://dashboard.render.com
2. [ ] Click "New +" → "Blueprint"
3. [ ] Connect GitHub repository
4. [ ] Click "Apply"
5. [ ] Wait for deployment (5-10 min)
6. [ ] Add `ALLOWED_HOSTS` environment variable
7. [ ] Test the API

## After Deployment

- [ ] Visit `/swagger/` to see documentation
- [ ] Test `/api/predict/` endpoint
- [ ] Check `/api/health/` for status
- [ ] Share the URL with others!

## Your URLs Will Be

Replace `your-app-name` with your actual Render app name:

- 📚 Swagger: `https://your-app-name.onrender.com/swagger/`
- 🔗 API: `https://your-app-name.onrender.com/api/predict/`
- 💚 Health: `https://your-app-name.onrender.com/api/health/`
- 📖 ReDoc: `https://your-app-name.onrender.com/redoc/`

## Test Command

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

## Troubleshooting

### If deployment fails:
1. Check build logs in Render dashboard
2. Verify all files are in GitHub
3. Check `requirements.txt` has all dependencies

### If API returns 500:
1. Check application logs in Render
2. Verify `DATABASE_URL` is set
3. Check migrations ran successfully

### If getting ALLOWED_HOSTS error:
1. Add your Render domain to `ALLOWED_HOSTS` env var
2. Format: `your-app-name.onrender.com`
3. Save and wait for redeploy

## Free Tier Notes

- ⚠️ Spins down after 15 minutes of inactivity
- First request after sleep: ~30 seconds
- 750 hours/month free
- Perfect for demos and testing!

## Keeping It Awake (Optional)

Use UptimeRobot or Cron-job.org to ping every 10 minutes:
- URL to ping: `https://your-app-name.onrender.com/api/health/`

## Ready to Deploy?

Follow: [RENDER_QUICKSTART.md](RENDER_QUICKSTART.md)

## Need Help?

- Full guide: [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)
- Render docs: https://render.com/docs
- Check logs in Render dashboard
