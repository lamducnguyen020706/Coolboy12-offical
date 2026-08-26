# COOLBOY12 — GPT Hard Audit Quickstart

## 1. Mục tiêu

Hãy audit repository này như một reviewer adversarial. Không chỉ tóm tắt nội dung và không mặc định rằng test PASS đồng nghĩa hệ thống production hoặc Claude Code runtime đã được chứng minh hoàn toàn.

Kết quả phải phân biệt rõ:

- `PASS`: có bằng chứng trực tiếp và tái hiện được.
- `FAIL`: có phản ví dụ hoặc invariant bị phá.
- `PARTIAL`: chỉ chứng minh được một phần.
- `UNVERIFIED`: chưa có môi trường/bằng chứng cần thiết.
- `NOT ENFORCED IN CODE`: chỉ được nêu trong documentation/procedure, chưa được code guard bảo vệ.

## 2. Snapshot baseline

| Item | Expected |
|---|---|
| Repository | `lamducnguyen020706/Coolboy12-offical` |
| Branch | `claude/coolboy12-build-31qwm0` |
| Baseline commit | `480584b0e745ae8774cce37989fada2664e1036e` |
| Production frontier | Artifact `021` |
| Next artifact | Artifact `022` |
| Current phase | `P0` |
| Completed artifacts | `21` |
| Implement Log events | `0` |
| Overall progress | `4.3%` |
| Roadmap | `19 phases / 490 artifacts` |

Nếu snapshot không khớp baseline, hãy ghi nhận đó là drift trước khi kết luận.

## 3. Đọc theo thứ tự

Đọc các file sau trước khi chạy test:

```text
reports/HTML_UPDATE_CONTRACT.md
scripts/update_progress.py
scripts/validate_progressreport.py
reports/progress.json
reports/implement-log.json
.claude/hooks/coolboy12_prompt_log.py
.claude/settings.json
.claude/commands/coolboy12-update.md
.claude/skills/coolboy12-update/SKILL.md
reports/progressreport.html
```

Sau đó đối chiếu authority sources:

```text
docs/sources/COOLBOY12_MASTER_BLUEPRINT_v0.7.03.md
docs/sources/COOLBOY12_RECORD_MODEL_SYSTEM_v1.0.md
docs/sources/COOLBOY12_OS_FILE_BUILD_ROADMAP_REPAIRED.md
```

Nếu có artifact extraction reference, đối chiếu thêm `COOLBOY12_artifact_extraction.md` với Roadmap. Không được sửa các authority sources trong audit.

## 4. Chạy baseline tests

Từ repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_progress_report \
  tests.test_claude_code_integration -v

python3 scripts/validate_progressreport.py
python3 scripts/update_progress.py --render
git diff --check
```

Sau render, xác nhận `reports/progress.json` và `reports/implement-log.json` không bị thay đổi ngoài chủ ý. Xác nhận canonical output vẫn là `reports/progressreport.html` và không có commit tự động.

## 5. Chạy synthetic evidence

Các evidence đã lưu trong:

```text
tests/coolboy12-progress-sync/
tests/coolboy12-progress-sync/artifact036-daily/
tests/coolboy12-progress-sync/boundary-scenarios/
```

Các scenario tối thiểu cần kiểm tra là:

| Scenario | Expected |
|---|---|
| Cuối P0 | Artifact `030`, P0 `DONE 30/30`, P1 `NOT STARTED 0/8` |
| Đầu P1 | Artifact `031`, P1 `WIP 1/8` |
| Implement Log 1 ngày | 1 day node, 1 artifact, daily `+0.2%` |
| Implement Log 10 ngày | 10 day nodes, 1 artifact/day, P1 `DONE 8/8`, P2 `WIP 2/21`, next `041` |
| Artifact 036 scenario | P1, frontier `036`, next `037`, mỗi ngày 1 artifact |
| Legacy 021→050 | synthetic regression phải PASS, production vẫn `021` |

Kiểm tra riêng rằng **Exact Artifact files**, **Dependency files** và **Repository evidence** không bị trộn. Blueprint/RMS/Roadmap không được biến thành exact files của Artifact 031 chỉ vì chúng là dependency/reference.

## 6. Audit Claude Code integration

Đối chiếu command trong `.claude/settings.json` với hook thực tế. Kiểm tra các trường hợp:

```text
normal prompt → activity event, không completion giả
same event_id → deduplicate
out-of-order artifact → bị chặn
prompt phủ định freeze/commit → không advance
đủ freeze + commit + evidence → chỉ khi đó mới có thể advance
malformed stdin → không làm hỏng production state
concurrent writes → kiểm tra atomic write/race behavior
```

Phải phân biệt hai luồng:

> `UserPromptSubmit` hook ghi activity và chỉ xử lý completion gate; `/coolboy12-update` mới là command regenerate HTML.

Một prompt hoặc một file tồn tại không được tự biến thành completed artifact. Một commit đơn lẻ cũng không đủ nếu thiếu sequential validation và evidence.

## 7. Kiểm tra UI output

Trong HTML generated, kiểm tra các invariant sau:

```text
19 phase cards
490 artifact IDs
P0 mở mặc định ở production
phase DONE màu xanh lá
current WIP màu amber
dark default
không có chữ today
phần trăm một chữ số thập phân
next-artifact card có Description, Purpose, exact files, Directory,
Dependency files, Dependencies/Unlocks và Validation/done condition
không có standalone trace/Critical path section đã bị loại bỏ
```

## 8. Kết luận readiness

Báo cáo kết luận theo ba cấp riêng:

1. **Production-safe:** state/log/render guards và regression có đủ bằng chứng không.
2. **Claude-Code-installable:** `.claude/` files, command, skill và shell invocation có nhất quán không.
3. **Claude runtime-verified:** có thực sự chạy trong binary Claude Code và nhận event lifecycle không.

Không được nâng cấp cấp 3 chỉ vì test gọi trực tiếp Python hoặc shell command. Nếu không có binary Claude Code thật, cấp 3 phải là `UNVERIFIED`.

## 9. Không được làm trong audit

Không sửa Blueprint, RMS, Roadmap hoặc source architecture. Không advance production state chỉ để tạo test evidence. Không commit, push, post hoặc cài đặt thay đổi bên ngoài nếu chưa có ủy quyền riêng. Mọi adversarial experiment phải dùng temporary copy, isolated repository hoặc branch tạm.

## 10. Báo cáo cuối GPT cần trả về

Hãy trả về một bảng gồm `Area`, `Claim`, `Evidence`, `Result`, `Severity` và `File/line`. Sau bảng, ghi rõ:

- các lỗi thực sự tái hiện được;
- các guard chỉ nằm trong documentation/procedure;
- các phần chỉ synthetic hoặc isolated;
- các phần còn `UNVERIFIED`;
- verdict production-safe / Claude-Code-installable / runtime-verified;
- danh sách remediation tối thiểu theo thứ tự ưu tiên.
