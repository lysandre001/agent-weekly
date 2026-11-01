# 安全公告：Cursor 扩展市场中发现恶意版本的 Anthropic.claude-code（2.1.313）

- 来源：https://cursor.com/cn/blog/claude-code-extension-security-notice
- 发布：2026-10-29（Cursor 官方博客，公司/安全公告）
- 英文原版：cursor.com/blog/claude-code-extension-security-notice

## 要点

- 事件：太平洋时间 2026-10-29 02:27–13:35 之间，Cursor VS Code 扩展市场被上架一个篡改版 `Anthropic.claude-code` 2.1.313（非 Anthropic 发布），运行恶意代码试图植入持久 SSH 后门。受影响用户最多 5,000 名。
- 恶意行为：收集主机/用户信息（主机名、用户名、OS、架构、环境变量名、Git 邮箱、公网 IP）；向 authorized_keys 追加攻击者公钥（注释 `svc-telemetry`）；尝试开本地 SSH + 反向隧道（因代码 bug，非管理员启动时失败）；用 LaunchAgent（macOS）/ 计划任务（Windows，试图 SYSTEM 权限）做持久化，每 60 秒重试；向 `134.209.82.225:8099/beacon` POST 上报。
- 攻击者服务器已被 Cursor 与云服务商合作下线，信标与反向 shell 已失效。
- Cursor 处置：下架恶意版本 → 出于谨慎**全面关闭 VS Code Marketplace** → 审计确认无其他扩展被篡改 → 轮换密钥、重建市场上线。
- 关键提醒：**只卸载扩展不够**——payload 会释放独立持久化脚本，卸载后继续运行。
- 自查（macOS）：`grep -qs svc-telemetry ~/.ssh/authorized_keys && echo "impacted" || echo "not impacted"`；官方提供修复脚本 remediate-macos.sh / remediate-windows.ps1。
- 持久化痕迹（macOS）：`~/.config/.smt`、`~/.config/.smtk`、`$TMPDIR/.stk_<10 hex>`、`~/Library/LaunchAgents/com.apple.sysmond.plist`（伪装成 com.apple.sysmond）。

## 与本刊素材的潜在勾连

- Agent 工具链供应链安全的第一起高调事件：扩展市场作为新的信任边界。"官方包名 + 被篡改的版本"攻击模板可能复现到其他 Agent IDE。
- 与 koomen"扁平组织/强势协调"无关，属独立的安全议题簇；可做"民间雷达"类快讯素材。
