# 🎯 START HERE - Deploy Your ML API

## Goal
Get a public URL like: `https://student-ml-api.onrender.com/swagger/`

So people can test your ML model online!

## Step 1: Push to GitHub (2 minutes)

```bash
cd student_ml
git init
git add .
git commit -m "Student ML API"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/student-ml-api.git
git push -u origin main
```

## Step 2: Deploy to Render (3 minutes)

1. Go to: https://dashboard.render.com
2. Click: **"New +"** → **"Blueprint"**
3. Connect your GitHub repo
4. Click: **"Apply"**
5. Wait 5-10 minutes

## Step 3: Configure (1 minute)

1. Go to your web service
2. Click **"Environment"**
3. Add:
   - Key: `ALLOWED_HOSTS`
   - Value: `your-app-name.onrender.com`
4. Save

## Step 4: Test! 🎉

Visit: `https://your-app-name.onrender.com/swagger/`

## Share With Others

Send them: `https://your-app-name.onrender.com/swagger/`

They can test your ML model directly in their browser!

## Need More Help?

- Quick guide: [RENDER_QUICKSTART.md](RENDER_QUICKSTART.md)
- Detailed guide: [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)
- Checklist: [RENDER_CHECKLIST.md](RENDER_CHECKLIST.md)

## Test Tools

After deployment:
- Browser: Open `test_page.html` in browser
- Command line: `./test_api.sh https://your-app.onrender.com`

---

**Total time: ~6 minutes** ⏱️

**Cost: $0** 💰

**Result: Public ML API** 🚀
