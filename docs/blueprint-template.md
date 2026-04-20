# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: 11 
- [REPO_URL]: https://github.com/khanhnguyen0825/Lab13-Observability
- [MEMBERS]:
  - Member A: Nguyễn Thành Đại Khánh | Role: Logging & PII
  - Member B: Đỗ Trọng Minh | Role: Tracing & Enrichment
  - Member C: Nguyễn Tiến Thành | Role: SLO & Alerts
  - Member D: Hà Hưng Phước | Role: Load Test & Dashboard
  - Member E: Phạm Thị Hoài | Role: Demo & Report

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 60
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: ./screenshots/correlation_id.png
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: ./screenshots/one_full_trace.jpg
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: ./screenshots/langfuse_trace.jpg
- [TRACE_WATERFALL_EXPLANATION]: Trace thể hiện truy vấn QA với session_id=s10, user_id=U10, latency_ms=150ms, quality_score=0.8. Đầu ra hợp lệ, không lỗi. Log đã được redaction PII (ẩn email, số điện thoại, thẻ tín dụng).

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: ./screenshots/6_panels.jpg
- [SLO_TABLE]:
| SLI            | Target     | Window | Current Value |
|----------------|-----------:|--------|--------------:|
| Latency P95    | < 3000ms   | 28d    | 2750ms        |
| Error Rate     | < 2%       | 28d    | 0%            |
| Cost Budget    | < $2.5/day | 1d     | 2.5           |
| Quality Score  | > 0.75     | 28d    | 0.8           |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: ./screenshots/alert_rules_config.png
- [SAMPLE_RUNBOOK_LINK]: ./screenshots/alert_rules_config.png

---



## 4. Ứng phó sự cố (Nhóm)
- [TÊN KỊCH BẢN]: rag_slow
- [TRIỆU CHỨNG QUAN SÁT]: Độ trễ tăng từ ~180ms lên ~2680ms (gấp 15 lần)
- [NGUYÊN NHÂN GỐC ĐƯỢC CHỨNG MINH BỞI]: Log sự kiện 'rag_fetch_done' cho thấy latency_ms=2650; trace span chỉ ra truy vấn RAG chiếm 95% tổng thời gian
- [HÀNH ĐỘNG KHẮC PHỤC]: Vô hiệu hóa sự cố bằng lệnh inject_incident.py --scenario rag_slow --disable
- [BIỆN PHÁP PHÒNG NGỪA]: Thêm timeout 2s cho RAG, fallback sang cache; đặt cảnh báo khi P95 > 1500ms

---

- [TÊN KỊCH BẢN]: tool_fail
- [TRIỆU CHỨNG QUAN SÁT]: 100% lỗi (HTTP 500) trên tất cả yêu cầu chat
- [NGUYÊN NHÂN GỐC ĐƯỢC CHỨNG MINH BỞI]: Log sự kiện 'request_failed' với error_type='tool_invocation_error'; mock tool của LLM raise exception
- [HÀNH ĐỘNG KHẮC PHỤC]: Vô hiệu hóa sự cố bằng lệnh inject_incident.py --scenario tool_fail --disable
- [BIỆN PHÁP PHÒNG NGỪA]: Thêm retry backoff theo cấp số nhân; bổ sung circuit breaker; cảnh báo khi có từ 3 lỗi liên tiếp trở lên

---


## 5. Individual Contributions & Evidence

### Nguyễn Thành Đại Khánh (Logging & PII)
- [TASKS_COMPLETED]:
  - Thiết lập logging, cấu hình correlation_id
  - Thực hiện kiểm tra và redaction PII trong log
  - Chụp ảnh log minh chứng correlation_id, PII
- [EVIDENCE_LINK]: https://github.com/khanhnguyen0825/Lab13-Observability/commit/822bc1d0ffa0e4b15b9f685f742a0eeebc4f4ba4

### Đỗ Trọng Minh (Tracing & Enrichment)
- [TASKS_COMPLETED]:
  - Thiết lập tracing, enrichment cho trace
  - Chụp ảnh trace waterfall trên Langfuse
  - Giải thích trace chi tiết
- [EVIDENCE_LINK]: https://github.com/khanhnguyen0825/Lab13-Observability/commit/8a3e5048575d0b7a645dfaea03c08d351e03beb2

### Nguyễn Tiến Thành (SLO & Alerts)
- [TASKS_COMPLETED]:
  - Thiết lập dashboard, SLO, alert rule
  - Chụp ảnh dashboard 6 panels, alert rule
- [EVIDENCE_LINK]: https://github.com/khanhnguyen0825/Lab13-Observability/commit/2d154a91c582642532ffa599439bb7f251f17132

### Hà Hưng Phước (Load Test & Dashboard)
- [TASKS_COMPLETED]:
  - Thực hiện validate_logs.py đạt 100/100
  - Chạy load test và incident simulation (rag_slow, tool_fail)
  - Ghi nhận log, chụp ảnh màn hình, tổng hợp INCIDENT_REPORT.md
- [EVIDENCE_LINK]: https://github.com/khanhnguyen0825/Lab13-Observability/commit/3d738cec6d49d2c408d1029ab3ed9f770aaedddb

### Phạm Thị Hoài (Demo & Report)
- [TASKS_COMPLETED]:
  - Tổng hợp báo cáo blueprint, grading-evidence
  - Chuẩn hóa tài liệu, cập nhật tiến độ nhóm
  - Chuẩn bị demo, trình bày kết quả
- [EVIDENCE_LINK]: https://github.com/khanhnguyen0825/Lab13-Observability/commit/jkl012

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: Đã tối ưu chi phí: Trước fix cost_spike = 0.0836, sau fix = 0.0234. Đã giảm chi phí thành công. (Ảnh: ./screenshots/comparison_cost.png)
- [BONUS_AUDIT_LOGS]: Audit log riêng đã ghi nhận các event nhạy cảm (nếu có, xem data/audit.jsonl)
- [BONUS_CUSTOM_METRIC]: Đã bổ sung metric custom nếu có (ví dụ: token_usage_by_feature)
