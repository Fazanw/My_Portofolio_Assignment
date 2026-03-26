# 🎯 Capstone Project Summary
## Portfolio Website - Faza Nur Wafirudin

**Live URL:** https://porto-faza.onrender.com
**GitHub:** https://github.com/Fazanw/My_Portofolio_Assignment

---

## ✅ Technical Criteria - 100% Complete

| Criteria | Status | Implementation |
|---|:---:|---|
| CI/CD Pipeline | ✅ | GitHub Actions 4-stage pipeline |
| Cloud Deployment | ✅ | Render.com (Docker, Singapore) |
| Security | ✅ | 4 measures implemented |
| Monitoring | ✅ | Live Chart.js dashboard + Prometheus metrics |
| Scaling | ✅ | Gunicorn workers + Render tier options |
| Documentation | ✅ | README + CHECKLIST + SUMMARY |

---

## 🔧 CI/CD Pipeline

```
Push to main → Lint → Test → Security Scan → Deploy to Render
```

- **Lint:** flake8 code quality check
- **Test:** 7 pytest tests + Docker build validation
- **Security:** bandit vulnerability scan
- **Deploy:** Render Deploy Hook — only triggers on main if all stages pass

---

## ☁️ Cloud Deployment

- **Platform:** Render.com (free, no credit card)
- **Runtime:** Docker
- **Region:** Singapore
- **Keep-Alive:** GitHub Actions pings `/health` every 14 minutes

---

## 🔐 Security (4 Measures)

1. No hardcoded secrets — environment variables only
2. Non-root Docker container — runs as `appuser`
3. `.gitignore` — `.env` and sensitive files excluded
4. Input sanitization — all user inputs validated and truncated

---

## 📈 Monitoring

### Live Dashboard (Production)
- **URL:** https://porto-faza.onrender.com/admin
- Built with Chart.js — runs directly on Render, no external tools needed
- Auto-refreshes every 15 seconds
- Shows: visitor traffic line chart, page views doughnut, recent visits table

### Prometheus Metrics
- **URL:** https://porto-faza.onrender.com/metrics
- Custom metrics: `portfolio_visitors_total`, `portfolio_unique_visitors`, `portfolio_page_views_total`
- Flask metrics: request count, latency, status codes

---

## 🚀 Scaling

- **Current:** 2 Gunicorn workers
- **Scalable to:** 4-8 workers (change in Dockerfile)
- **Platform:** Render Starter ($7/mo) for no sleep

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Framework | Flask 3.1.0 |
| Server | Gunicorn 23.0.0 |
| Frontend | HTML5 + CSS3 + Chart.js |
| Container | Docker |
| CI/CD | GitHub Actions |
| Monitoring | Prometheus + Chart.js |
| Deployment | Render.com |
| Testing | Pytest |

---

## 📁 Key Files

| File | Purpose |
|---|---|
| `app.py` | Flask app, routes, metrics, visitor tracking |
| `templates/index.html` | Portfolio UI |
| `templates/admin.html` | Live monitoring dashboard |
| `.github/workflows/ci-cd.yml` | 4-stage CI/CD pipeline |
| `.github/workflows/keep-alive.yml` | Prevent Render sleep |
| `Dockerfile` | Container config (non-root) |
| `docker-compose.yml` | Local dev stack with Prometheus |
| `prometheus.yml` | Metrics scrape config |
| `test_app.py` | 7 unit tests |

---

## 🔗 All URLs

| Resource | URL |
|---|---|
| Portfolio | https://porto-faza.onrender.com |
| Monitoring | https://porto-faza.onrender.com/admin |
| Metrics | https://porto-faza.onrender.com/metrics |
| Health | https://porto-faza.onrender.com/health |
| GitHub | https://github.com/Fazanw/My_Portofolio_Assignment |
| LinkedIn | https://linkedin.com/in/fazanurw |

---

**Status:** ✅ READY FOR SUBMISSION
**Version:** 1.0.0
