# AI 产品研究

以单个产品的持续研究档案为主体，整理公开数据、研究结论和文章。每项研究保留来源、时间和统计口径，方便回查与复用。

第一期：[a16z Top 100 AI 产品](research/a16z-top-100-ai/README.md)。正在等待输入资料，榜单期次和发布时间尚未确认。

## 目录

```text
products/               # 每个产品的持续研究档案和相关文章
templates/              # 产品档案模板
research/
  a16z-top-100-ai/
    README.md           # 本期状态、范围和阅读入口
    sources.csv         # 来源链接、发布日期、访问日期和使用范围
    data/               # 可公开、已核对的数据和字段说明
    findings/           # 有证据支持的研究结论
    articles/           # 对外文章及其配图
scripts/                # 可复用的整理与检查脚本
private/                # 仅本地：收到的文件、讨论、草稿、临时数据
```

`private/` 已被忽略，按正常提交流程不会上传到 GitHub。首次克隆后可以自行创建：

```sh
mkdir -p private/inbox private/discussions private/drafts private/scratch
```

每个产品的组织方式见 [产品档案说明](products/README.md)。榜单记录某个时点的排名与样本，档案随研究更新。同一产品跨榜单复用档案。

## 资料怎么进入仓库

1. 收到的文件先放进 `private/inbox/`，讨论和草稿也留在 `private/`。
2. 在本期 `sources.csv` 登记来源，确认版本、时间、统计口径和公开范围。第三方材料优先保留链接及必要摘录。
3. 把可公开的数据整理进 `data/`，补齐字段说明；保留来源关联，区分原始事实与研究判断。
4. 将结论写进 `findings/`，引用对应数据和来源；对外文章放进 `articles/`。
5. 按 [产品档案模板](templates/product-profile.md) 建立 `products/<product-id>/README.md`，关联榜单索引。产品文章放在该产品的 `articles/`，跨产品文章放在研究批次的 `articles/`。
6. 提交前查看实际变更，确认文件内容适合公开，再提交和推送。

GitHub Issues 和 PR 都是公开的，只放可公开的研究任务、修正和结论。中间讨论留在本地。

## 提交前检查

克隆后启用本地提交检查：

```sh
git config core.hooksPath .githooks
python3 scripts/check_public_files.py
git diff --cached --stat
git diff --cached
```

根目录采用默认忽略、明确放行的规则；本地 hook 和 GitHub Actions 会检查已跟踪文件的路径，拦截私有目录及常见凭据文件。检查不识别正文里的敏感内容，公开前仍需阅读变更。不要用 `git add -f` 绕过忽略规则；已经进入 Git 历史的文件不能靠 `.gitignore` 隐藏。

研究数据建议用 UTF-8 CSV，正文用 Markdown；需要复算时再增加脚本或 Notebook。以后新增一期研究，在 `research/` 下建新目录，沿用同一组织方式。

## 许可

本仓库原创内容与代码采用 [MIT License](LICENSE)。第三方榜单、图表、商标和引用材料的权利归原权利人，不因收录或引用而改为 MIT 许可。来源及使用范围记录在各期 `sources.csv` 中。
