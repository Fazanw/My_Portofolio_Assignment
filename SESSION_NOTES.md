# 📌 Session Notes — Next Steps

## Status: Ready to Deploy (not deployed yet)

---

## TODO (In Order)

### PART 1 — Push to GitHub
```bash
cd "e:\Personal Document\Digital Skola\Tugas\Capstone Project\My_Portofolio"
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### PART 2 — Deploy on Render
1. https://render.com → sign up with GitHub (no credit card)
2. New → Web Service → connect My_Portofolio repo
3. Config:
   - Name: portfolio-faza
   - Region: Singapore
   - Runtime: Docker
   - Instance: Free
4. Env vars: FLASK_ENV=production, PORT=5000
5. Create Web Service → wait 3-5 min
6. Settings → Deploy Hook → copy URL
7. GitHub repo → Settings → Secrets → New secret
   - Name: RENDER_DEPLOY_HOOK
   - Value: paste the URL

### PART 3 — Grafana (Local Monitoring)
1. docker compose up --build
2. http://localhost:3000 → login admin / admin123
3. Connections → Data sources → Add Prometheus
   - URL: http://prometheus:9090
   - Save & test
4. Dashboards → Import → ID 11159 → Import

### PART 4 — Keep-Alive (Prevent Render Sleep)
1. https://cron-job.org → sign up free
2. Create cron job:
   - URL: https://portfolio-faza.onrender.com/health
   - Schedule: every 14 minutes
   - Method: GET

---

## Files Already Done (Do Not Redo)
- .github/workflows/ci-cd.yml — 4-stage pipeline: lint → test → security → deploy
- test_app.py — 7 tests covering all endpoints
- prometheus.yml — scrapes local + live Render app
- app.py — visitor tracking, /admin, /metrics endpoints
- templates/admin.html — visitor analytics dashboard
- templates/index.html — portfolio UI, location: Bekasi West Java
- static/style.css — glassmorphism dark theme
- .env — local credentials (git-ignored, DO NOT push)
- .env.example — safe placeholder for GitHub
- README.md — fully updated for Render deployment
- CHECKLIST.md — capstone criteria verification
- SUMMARY.md — presentation ready

---

## Key Info
- Live URL (after deploy): https://portfolio-faza.onrender.com
- GitHub: https://github.com/Fazanw
- Local app: http://localhost:5000
- Local Grafana: http://localhost:3000 (admin / admin123)
- Local Prometheus: http://localhost:9090
- Admin dashboard: https://portfolio-faza.onrender.com/admin
- Health check: https://portfolio-faza.onrender.com/health
- Metrics: https://portfolio-faza.onrender.com/metrics

---

## Next Session Prompt
Paste this at the start of next chat:
"Continue from SESSION_NOTES.md — I need to deploy my portfolio to Render,
set up Grafana monitoring locally, and configure cron-job.org keep-alive.
All files are ready, just need to execute the steps."
