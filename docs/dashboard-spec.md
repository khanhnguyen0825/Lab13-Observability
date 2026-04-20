# Dashboard Spec

Required Layer-2 panels:
1. Latency P50/P95/P99
   - Tên metric cụ thể: latency_p95_ms
   - Đơn vị hiển thị: ms
   - Ngưỡng SLO line: 3000
   - Ví dụ cách đọc: Nếu đường latency vượt đường SLO 3000ms → hệ thống đang chậm, cần xem Traces.
2. Traffic (request count or QPS)
   - Tên metric cụ thể: request_count
   - Đơn vị hiển thị: count
   - Ngưỡng SLO line: N/A
   - Ví dụ cách đọc: Theo dõi lưu lượng người dùng, nhận biết các đợt tăng traffic đột biến.
3. Error rate with breakdown
   - Tên metric cụ thể: error_rate_pct
   - Đơn vị hiển thị: %
   - Ngưỡng SLO line: 2
   - Ví dụ cách đọc: Nếu đường đồ thị vượt 2% SLO → có lỗi API hoặc LLM, cần kiểm tra logs.
4. Cost over time
   - Tên metric cụ thể: daily_cost_usd
   - Đơn vị hiển thị: USD
   - Ngưỡng SLO line: 2.5
   - Ví dụ cách đọc: Nếu đường chi phí vượt đường SLO cho thấy chi phí token cao bất thường, cần check prompt.
5. Tokens in/out
   - Tên metric cụ thể: token_count
   - Đơn vị hiển thị: tokens
   - Ngưỡng SLO line: N/A
   - Ví dụ cách đọc: Giúp đối chiếu với biểu đồ cost, kiểm tra xem loại token in hay out đang tăng.
6. Quality proxy (heuristic, thumbs, or regenerate rate)
   - Tên metric cụ thể: quality_score_avg
   - Đơn vị hiển thị: điểm (0-1)
   - Ngưỡng SLO line: 0.75
   - Ví dụ cách đọc: Nếu đường chất lượng giảm dưới SLO 0.75 → chất lượng trả lời thấp, cần phân tích log/trace.

Quality bar:
- default time range = 1 hour
- auto refresh every 15-30 seconds
- visible threshold/SLO line
- units clearly labeled
- no more than 6-8 panels on the main layer
