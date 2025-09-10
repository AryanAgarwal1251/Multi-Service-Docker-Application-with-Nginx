import streamlit as st
import requests

# Set this to "http://localhost" when accessing via browser on the host,
# or "http://nginx" when this app runs inside Docker and NGINX is another service.
BASE_URL = "http://nginx"  # change to "http://nginx" in Docker network

st.title("Multi-Service ML App")

# --- Sentiment Prediction ---
st.subheader("Sentiment Prediction")
review = st.text_input("Enter a review:")

if st.button("Analyze Sentiment") and review.strip():
    try:
        resp = requests.post(f"{BASE_URL}/sentiment/predict", json={"text": review}, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        st.write("Sentiment:", data.get("sentiment", "unknown"))

        log_payload = {
            "service": "sentiment-service",
            "message": f"Analyzed review: {review[:50]}"
        }
        requests.post(f"{BASE_URL}/log_post", json = log_payload, timeout=10)

    except Exception as e:
        st.error(f"Sentiment service error: {e}")

# --- Dataset Analysis ---
st.subheader("Dataset Analysis")
uploaded_file = st.file_uploader("Upload a ZIP dataset", type="zip")

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/zip")}
    try:
        resp = requests.post(f"{BASE_URL}/analysis/analyze", files=files, timeout=60)
        content_type = resp.headers.get("Content-Type", "")
        if "application/json" in content_type:
            # Backend returned an error payload
            payload = {}
            try:
                payload = resp.json()
            except Exception:
                pass
            st.error(payload.get("error", f"Analysis error (status {resp.status_code})"))

        elif "image" in content_type:
            st.image(resp.content, caption="Analysis Result")

            log_payload = {
                "service": "analysis-service",
                "message": f"Analyzed dataset '{uploaded_file.name}' successfully"
            }

            try:
                log_resp = requests.post(f"{BASE_URL}/log_post", json=log_payload, timeout=10)
                log_resp.raise_for_status()
                
            except Exception as log_err:
                st.warning(f"Failed to send log: {log_err}")
        
        else:
            st.warning(f"Unexpected content type: {content_type}. Showing first 300 chars:")
            st.text(resp.text[:300])


    except Exception as e:
        st.error(f"Analysis service error: {e}")

# --- Logs ---
st.subheader("Service Logs")
if st.button("Fetch Logs"):
    try:
        # Adjusted URL path to match logging service GET route (/log_get)
        resp = requests.get(f"{BASE_URL}/log_get/", timeout=15)
        resp.raise_for_status()  # Raises exception for HTTP errors
        logs = resp.json()
        if not logs:
            st.info("No logs available.")
        else:
            for log in logs:
                ts = log.get("timestamp", "-")
                svc = log.get("service", "-")
                msg = log.get("message", "-")
                st.write(f"{ts} | {svc} | {msg}")
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err} - {resp.text[:200]}")
    except Exception as e:
        st.error(f"Logging service error: {e}")


