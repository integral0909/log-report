An Apache-style access log is at /app/access.log. Each line begins with the client IP
address, followed by an Apache common-log-format request line that includes the HTTP
method and the requested path (for example: "GET /index.html HTTP/1.1").

Analyze the log and write a JSON summary to /app/report.json. The file must be a single
JSON object with exactly these three keys:

  - "total_requests": integer — the number of request lines in the log.
  - "unique_ips": integer — the count of distinct client IP addresses (the first
    whitespace-separated field on each line).
  - "top_path": string — the requested path that appears in the most requests.

Do not modify /app/access.log.

Success criteria:
1. /app/report.json exists and is a single JSON object.
2. "total_requests" equals the number of request lines in /app/access.log.
3. "unique_ips" equals the number of distinct client IP addresses.
4. "top_path" is the path requested most often across all requests.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
