Apache access log is available at /app/access.log. Each line consists of client IP address,
followed by an Apache common-log-format request which includes HTTP method and
requested path (for example: "GET /index.html HTTP/1.1").

Please analyze the log and generate a JSON report in /app/report.json. It should be one
JSON object which contains precisely these three properties:

  - "total_requests": integer – number of lines in the log.
  - "unique_ips": integer – number of unique client IP addresses (whitespace-delimited
    first field in each log entry).
  - "top_path": string – path which appeared in most log entries.

Don’t touch /app/access.log.

Success conditions:
1. /app/report.json is created and is one JSON object.
2. "total_requests" equals the number of lines in /app/access.log.
3. "unique_ips" equals the number of unique client IP addresses.
4. "top_path" is the path that was requested most frequently.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
