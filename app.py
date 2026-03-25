import os
import logging
from flask import Flask, render_template, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
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

# Visitor tracking (in-memory)
visitor_stats = {
    "total_visits": 0,
    "unique_visitors": set(),
    "recent_visits": deque(maxlen=100),  # Last 100 visits
    "page_views": defaultdict(int)
}

@app.route("/")
def index():
    track_visitor("/")
    logger.info("Home page visited from %s", request.remote_addr)
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()})

@app.route("/admin")
def admin_dashboard():
    """Admin dashboard page"""
    return render_template("admin.html")

@app.route("/admin/stats")
def admin_stats():
    """Admin dashboard for visitor statistics"""
    return jsonify({
        "total_visits": visitor_stats["total_visits"],
        "unique_visitors": len(visitor_stats["unique_visitors"]),
        "page_views": dict(visitor_stats["page_views"]),
        "recent_visits": list(visitor_stats["recent_visits"])[-20:]  # Last 20
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
        "user_agent": user_agent[:50]  # Truncate long user agents
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
