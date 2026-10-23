# AI 产品研究

以文章为主的 AI 产品研究。榜单是选题入口，产品档案是写文章用的素材库，每条事实都带来源和日期。

```text
articles/   对外文章（成果）
products/   每个产品一个 Markdown 档案，跨榜单复用
lists/      榜单快照：来源、口径、排名，链接到档案
templates/  产品、榜单、文章模板
scripts/    提交前检查
private/    仅本地：收到的资料、草稿、抓取结果（已忽略）
```

研究流程和证据规则见 [AGENTS.md](AGENTS.md)，人和 agent 都按这份执行。

## 本地设置

```sh
mkdir -p private/inbox private/drafts
git config core.hooksPath .githooks   # 提交时自动运行检查
python3 scripts/check.py
```

检查内容：已跟踪文件是否都在公开目录内、文件类型是否允许、产品 frontmatter 是否完整、榜单里的档案链接是否存在。检查不识别正文里的敏感信息，公开前仍需阅读 diff。

## 许可

本仓库原创内容与代码采用 [MIT License](LICENSE)。第三方榜单、图表、商标和引用内容的权利归原权利人，不因收录或引用而改为 MIT 许可。
