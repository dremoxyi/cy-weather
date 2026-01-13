def test_health_check(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_metrics_endpoint(client):
    response = client.get("/api/metrics")

    assert response.status_code == 200
    assert "app_requests_total" in response.text
    assert "request_latency_seconds" in response.text

def test_metrics_middleware_increments_counter(client):
    client.get("/api/health")
    response = client.get("/api/metrics")
    metrics_text = response.text
    assert 'app_requests_total' in metrics_text
    assert 'endpoint="/api/health"' in metrics_text

def test_cors_headers(client):
    response = client.options(
        "/api/health",
        headers={
            "Origin": "http://example.com",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code == 200
    assert "access-control-allow-origin" in response.headers
