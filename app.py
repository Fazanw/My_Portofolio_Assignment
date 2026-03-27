import os
import logging
from flask import Flask, render_template, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Gauge
from datetime import datetime, timezone
from collections import defaultdict, deque

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info("app_info", "Portfolio app info", version="1.0.0")

# Custom Prometheus metrics
VISITOR_TOTAL = Counter(
    "portfolio_visitors_total",
    "Total number of visitors"
)
UNIQUE_VISITORS = Gauge(
    "portfolio_unique_visitors",
    "Number of unique visitors"
)
PAGE_VIEWS = Counter(
    "portfolio_page_views_total",
    "Total page views per page",
    ["page"]
)

# Visitor tracking (in-memory)
visitor_stats = {
    "total_visits": 0,
    "unique_visitors": set(),
    "recent_visits": deque(maxlen=100),
    "page_views": defaultdict(int)
}


@app.route("/")
def index():
    track_visitor("/")
    logger.info("Home page visited from %s", request.remote_addr)
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


@app.route("/admin")
def admin_dashboard():
    """Admin dashboard page"""
    return render_template("admin.html")


@app.route("/admin/stats")
def admin_stats():
    """Visitor statistics JSON API"""
    return jsonify({
        "total_visits": visitor_stats["total_visits"],
        "unique_visitors": len(visitor_stats["unique_visitors"]),
        "page_views": dict(visitor_stats["page_views"]),
        "recent_visits": list(visitor_stats["recent_visits"])[-20:]
    })


@app.route("/admin/metrics-data")
def metrics_data():
    """Chart data JSON API"""
    history = list(visitor_stats["recent_visits"])
    visits_by_minute = defaultdict(int)
    for v in history:
        minute = v["timestamp"][:16]
        visits_by_minute[minute] += 1
    sorted_minutes = sorted(visits_by_minute.items())[-20:]
    return jsonify({
        "visits_timeline": {
            "labels": [m[0] for m in sorted_minutes],
            "values": [m[1] for m in sorted_minutes]
        },
        "page_views": {
            "labels": list(visitor_stats["page_views"].keys()),
            "values": list(visitor_stats["page_views"].values())
        },
        "total_visits": visitor_stats["total_visits"],
        "unique_visitors": len(visitor_stats["unique_visitors"])
    })


def track_visitor(page):
    """Track visitor activity"""
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent", "Unknown")
    timestamp = datetime.now(timezone.utc).isoformat()
    visitor_stats["total_visits"] += 1
    visitor_stats["unique_visitors"].add(ip)
    visitor_stats["page_views"][page] += 1
    visitor_stats["recent_visits"].append({
        "ip": ip,
        "page": page,
        "timestamp": timestamp,
        "user_agent": user_agent[:50]
    })
    VISITOR_TOTAL.inc()
    UNIQUE_VISITORS.set(len(visitor_stats["unique_visitors"]))
    PAGE_VIEWS.labels(page=page).inc()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    is_dev = os.environ.get("FLASK_ENV") == "development"
    host = "127.0.0.1" if is_dev else "0.0.0.0"  # nosec B104
    app.run(host=host, port=port, debug=is_dev)
