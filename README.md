# 🚀 Faza Nur Wafirudin — Portfolio Website

Personal portfolio website for **Faza Nur Wafirudin**, AWS Certified Cloud Practitioner & OCI Architect Associate.

🌐 Live at: [https://porto-faza.onrender.com](https://porto-faza.onrender.com)

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python / Flask |
| Frontend | HTML5 / CSS3 (vanilla) |
| Container | Docker |
| CI/CD | GitHub Actions |
| Deployment | Render.com |
| Monitoring | Prometheus + Grafana (local) |

---

## 📁 Project Structure

```
.
├── app.py                        # Flask app (routes, metrics, logging)
├── templates/
│   └── index.html                # Portfolio single-page frontend
├── static/
│   └── style.css                 # External stylesheet
├── requirements.txt
├── Dockerfile
├── docker-compose.yml            # Local dev + Prometheus + Grafana
├── prometheus.yml                # Prometheus scrape config
├── test_app.py                   # Pytest unit tests
├── .env.example                  # Environment variable template
├── .gitignore
└── .github/
    └── workflows/
        ├── ci-cd.yml             # CI/CD pipeline
        └── keep-alive.yml        # Keep-alive ping every 14 minutes
```

---

## 🔧 CI/CD Pipeline

The GitHub Actions pipeline (`.github/workflows/ci-cd.yml`) runs on every push to `main`:

```
Push to main
    │
    ▼
[1] Lint ──── flake8 (code quality check)
    │
    ▼
[2] Test ──── pytest (7 tests) + Docker build
    │
    ▼
[3] Security ─ bandit scan (vulnerability check)
    │
    ▼
[4] Deploy ── Render Deploy Hook → live in ~3 min
```

Each stage only runs if the previous one passes. Deploy only triggers on `main` branch.

### Required GitHub Secrets

Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**:

| Secret | Description | How to Get |
|---|---|---|
| `RENDER_DEPLOY_HOOK` | Render deploy trigger URL | Render Dashboard → your service → Settings → Deploy Hook |

> ⚠️ Never hardcode the Deploy Hook URL in any file. Always use GitHub Secrets.

---

## ☁️ Deployment (Render.com)

Deployed on **Render.com** free tier — no credit card required.

### Setup Steps

1. Sign up at https://render.com using GitHub login
2. New → Web Service → Connect this repository
3. Configure:

| Field | Value |
|---|---|
| Runtime | Docker |
| Region | Singapore |
| Branch | `main` |
| Instance Type | Free |

4. Add environment variables:

| Key | Value |
|---|---|
| `FLASK_ENV` | `production` |
| `PORT` | `5000` |

5. Click **Create Web Service** — done!

Every push to `main` triggers an automatic redeploy.

### Keep-Alive (Prevent Free Tier Sleep)

Free tier sleeps after 15 minutes of inactivity. Prevented using a **GitHub Actions** scheduled workflow that pings the app every 14 minutes.

| Field | Value |
|---|---|
| File | `.github/workflows/keep-alive.yml` |
| Schedule | Every 14 minutes (`*/14 * * * *`) |
| Endpoint | `https://portfolio-faza.onrender.com/health` |
| Method | `GET` |

The `/health` endpoint returns `{"status": "healthy"}` — lightweight and perfect for keep-alive pings.

---

## 🖥️ Local Development

```bash
# 1. Clone the repo
git clone https://github.com/Fazanw/<repo-name>.git
cd <repo-name>

# 2. Copy env file
cp .env.example .env

# 3. Run with Docker Compose (app + Prometheus + Grafana)
docker compose up --build

# App:        http://localhost:5000
# Metrics:    http://localhost:5000/metrics
# Prometheus: http://localhost:9090
# Grafana:    http://localhost:3000  (admin / see .env)
```

Or run directly with Python:
```bash
pip install -r requirements.txt
flask run
```

---

## 📈 Monitoring

### Application Logging
- Structured logging with timestamps
- Tracks all page visits with IP addresses
- Access logs via Render dashboard or `docker logs`

### Visitor Analytics Dashboard
- **URL:** `https://porto-faza.onrender.com/admin`
- Real-time visitor statistics
- Tracks: total visits, unique visitors, page views
- Shows last 20 visits with IP, timestamp, user agent
- Auto-refreshes every 30 seconds

### Prometheus
- Scrapes `/metrics` endpoint every 15 seconds
- Tracks: HTTP request count, latency, status codes

### Grafana Dashboard (Local)
1. Open `http://localhost:3000`
2. Login: `admin` / password from `.env`
3. Add data source → Prometheus → `http://prometheus:9090`
4. Import dashboard ID **11159** (Flask Monitoring) from Grafana.com

---

## 🔐 Security Measures

| Measure | Implementation |
|---|---|
| No hardcoded secrets | All credentials via environment variables |
| Non-root container | Dockerfile creates and uses `appuser` |
| `.gitignore` | `.env` and sensitive files excluded from git |

---

## 🧪 Running Tests

```bash
pip install pytest
pytest test_app.py -v
```

Tests cover:
- `GET /` → 200 homepage
- `GET /health` → 200 + healthy status
- `GET /health` → response contains timestamp
- `GET /admin` → 200 admin dashboard
- `GET /admin/stats` → 200 + correct JSON fields
- `GET /` → visitor tracking increments correctly
- `GET /metrics` → 200 Prometheus metrics

---

## 🚀 Scaling

### Render Paid Tier
- Upgrade to **Starter** ($7/month) for no sleep + more RAM
- Upgrade to **Standard** ($25/month) for auto-scaling

### Gunicorn Workers
Increase workers in `Dockerfile` for higher concurrency:
```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
```

---

## 📬 Contact

**Faza Nur Wafirudin**
- 📧 fazanurwafirudin@gmail.com
- 💼 [linkedin.com/in/fazanurw](https://www.linkedin.com/in/fazanurw)
- 🐙 [github.com/Fazanw](https://github.com/Fazanw)
