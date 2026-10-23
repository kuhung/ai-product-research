---
title: a16z "Top 100 Consumer AI Apps" 第 7 期报告解读（2026 年 10 月）
date: 2026-10-06
status: draft
products:
  - chatgpt
  - claude
  - gemini
  - deepseek
  - canva
  - notion
  - perplexity
  - suno
  - photoroom
  - manus
  - kling-ai
  - heygen
  - elevenlabs
lists:
  - a16z-top-100-consumer-ai-2026-10
---

# a16z "Top 100 Consumer AI Apps" 第 7 期报告解读（2026 年 10 月）

> 本文为 a16z 第 7 期榜单报告的事实梳理与解读。本期官方报告由 a16z 合伙人 Olivia Moore 撰写，发布于 2026-10-05（[来源链接](https://a16z.com/100-gen-ai-apps-7/)），数据口径为 2026 年 8 月（Similarweb / Sensor Tower）及 YipitData 美国消费者 panel 信用卡与电子收据支出数据。完整排名表见 [榜单快照](../lists/a16z-top-100-consumer-ai-2026-10.md)。

## 摘要

- **方法论首次变化**：前六期仅统计流量（Similarweb 全球月独立访问量 + Sensor Tower 移动端 MAU），第 7 期首次加入 **YipitData 美国消费者信用卡支出榜（Spend 50）**。a16z 指出“仅看流量越来越掩盖消费 AI 的真实趋势”，传统流量视角看不见桌面客户端、开发者工具、自动化 API 服务以及嵌入即时通讯生态的付费 Agent。
- **核心发现：重度付费经济（Power-user economy）**：仅 4.5% 的美国消费者为 [ChatGPT](../products/chatgpt.md)、[Gemini](../products/gemini.md)、[Claude](../products/claude.md) 付费；在付费人群中，前 1% 的重度付费者（Top 1% Power Spenders）月均消费达 **$903**（18 个月内增长 80%），而付费者中位数仅为 $25/月；前 1% 付费者贡献了 19.5% 的总支出（超过后 50% 付费者合计贡献的 16.6%）；仅 13% 的付费者会购买第二个 AI 工具。
- **[ChatGPT](../products/chatgpt.md) 仍是第一**：Web 访问量约为 [Gemini](../products/gemini.md) 的 2 倍、[Claude](../products/claude.md) 的 6 倍；移动端 MAU 超过 10 亿（约为 Gemini 的 2.5 倍、Claude 的 14 倍）；美国个人付费订阅数约为 Gemini 或 Claude 各自的 3 倍。ChatGPT 是本期唯一同时在 Web 榜、Mobile 榜、消费支出榜位居第 1 的产品。
- **[Claude](../products/claude.md) 成为明确的 #3**：Web 流量超过 [DeepSeek](../products/deepseek.md) 与 [Perplexity](../products/perplexity.md)（月访问量近 10 亿）；2026 年内一度在美国家庭/个人付费订阅数上超过 Gemini；其订阅用户中有 7.3% 选用 $100+/月 Max 档（对比 ChatGPT 1.1%、Google 1.3%）。但在 7-8 月夏季出现日均会话下降、新增放缓与流失上升。
- **榜单固化**：本期仅 11 个新产品首次上榜，为七期以来最少；支出榜 Top 50 中有 29 家公司完全不在 Web 或 Mobile 流量榜上；仅 7 家公司同时进入三榜。
- **中国及华人背景产品表现**：官方正文确认 Claude 在 Web 流量上已超过 DeepSeek；[Kling AI](../products/kling-ai.md)（快手可灵）围绕专有视频模型进入消费支出榜（第 26 名）；由中国团队创立、2025 年中将总部迁至新加坡的 [Manus](../products/manus.md)（蝴蝶效应）被点名为前 1% 付费者超配的自主 Agent 工具（支出榜第 19 名）。
- **核心商业判断**：市场焦点已从“谁在赢”转向“每家公司如何执行自己的机会”（Claude for work，Gemini for consumers，ChatGPT for both）；个人自主助手（Agent）开启下一个产品周期；订阅制触及大众市场天花板，正在催生广告变现（ChatGPT 广告年化已达 $10 亿）与交易抽成。
- **对比第 6 期（2026-03）**：方法论从单一流量排名变为“流量 + 真实支出”；叙事重心从“默认入口与地理分化”转为“谁在真正付费、Agent 大众化以及既有软件（SaaS）结合 AI 反攻”。

---

## 1. 方法论变化

**前六期回顾**：
仅用流量指标排名，即 Similarweb 月独立访问量（Web 榜前 50）、Sensor Tower 月活跃用户 MAU（移动榜前 50）。

**第 7 期新规则**：
1. **首次引入 YipitData 美国消费者信用卡/电子收据观测支出数据**，新增“消费支出 Top 50（Spend 50）”榜单。官方表示纯流量数据“increasingly conceals the real trends in consumer AI”。
2. **新增维度的背景**：支出视角覆盖了流量盲区，包括桌面 App、开发工具、媒体生成 API 以及嵌入既有通信工具的 Agent。这类产品没有同等规模的网页访问量或 App 下载，但客单价较高。
3. **支出数据揭示的事实**：
   - 支出榜 Top 50 中，有 **29 家公司未进入 Web 或 Mobile 流量榜**。
   - 流量排名与支出排名差异明显，取决于产品对重度付费用户的变现程度。
   - **仅 7 家公司同时进入三榜**：[ChatGPT](../products/chatgpt.md)（唯一三榜第一）、[Claude](../products/claude.md)、[Suno](../products/suno.md)、[Perplexity](../products/perplexity.md)、[Photoroom](../products/photoroom.md)、[Canva](../products/canva.md)、[Notion](../products/notion.md)。
   - 官方提示：支出榜基于美国消费者 panel 样本观测，不包含纯企业对公采购与美国境外直购，**不能等同于公司全球总营收**。
4. **排除 NSFW 规则**：从本期起，**主要为成人/NSFW 场景设计的产品被排除**。官方估算被剔除的 NSFW 产品原本可占 Web 流量榜 20% 以上的席位（如第 6 期在榜的 JanitorAI、SpicyChat 等）。

---

## 2. 核心数据点

以下数据来源于 a16z 官方报告与 YipitData 观测（统计截至 2026 年 8 月）：

| 数据指标 | 观测数值 | 来源与口径说明 |
| --- | --- | --- |
| ChatGPT Web 访问量 vs Gemini | 约 2 倍 | a16z 官方正文（Similarweb 2026-08） |
| ChatGPT Web 访问量 vs Claude | 约 6 倍 | a16z 官方正文（Similarweb 2026-08） |
| ChatGPT 移动 MAU vs Gemini / Claude | 约 2.5 倍 / 约 14 倍 | a16z 官方正文（Sensor Tower 2026-08） |
| ChatGPT 移动端总 MAU | 10 亿+ | a16z LinkedIn 披露（2026-10-05，具体单帖链接待核实） |
| ChatGPT 美国付费订阅数 | 约为 Gemini 或 Claude 各自的 3 倍 | a16z 官方正文（YipitData panel） |
| Claude Web 全球排名 | 第 3 名（超 DeepSeek 与 Perplexity，月访问近 10 亿） | a16z 官方正文 + LinkedIn 披露 |
| Claude vs Gemini 美国付费规模 | Claude 年内一度超越 Gemini；Google 迁移老订户后两者持平 | a16z 官方正文（YipitData panel） |
| Claude $100+/月（Max 档）付费占比 | **7.3%**（Google 1.3%、ChatGPT 1.1%） | a16z 官方正文（YipitData panel） |
| 美国家庭/消费者为 AI 付费比例 | **4.5%**（拥有一项三巨头个人订阅；一年前为 2.1%） | a16z 官方正文（YipitData e-receipt） |
| 前 1% 付费者月均支出 | **$903**（18 个月增长 80%）；付费中位数 **$25**/月 | a16z 官方正文 |
| 前 1% 付费者总支出贡献 | 19.5%（超过后 50% 付费者总和 16.6%）；前 10% 贡献约一半 | a16z 官方正文 |
| 跨产品购买第二款 AI 工具比例 | **13%** | a16z 官方正文 |
| 新入榜产品数量 | **11 个**（七期最少） | a16z 官方正文 |
| ChatGPT 商业化进展 | 8 月广告年化收入达 **$10 亿**，周活跃用户 12 亿 | a16z 官方正文 |
| 商业变现模式分布（Web Top 50 中 44 个 AI 原生产品） | 84% 订阅制、64% 用量/Credits、14% 广告、2% 交易平台分成 | a16z 官方正文 |

**其他细节**：
- **竞争重叠**：全美仅 8% 的 ChatGPT 订阅者同时订阅 Claude；ChatGPT 在全美除加州、蒙大拿、马萨诸塞 3 个州外均领先。
- **Claude 波动**：2026 年 2 月底因 Pentagon 争议短暂登顶美国免费移动榜第 1；但在 7-8 月夏季日均会话下降、新增放缓且流失率抬升；ChatGPT 则随 7 月上线的 GPT-5.6（Sol/Terra/Luna）和 ChatGPT Work 重新提速。
- **专有模型创意工具**：[Suno](../products/suno.md)（Web 第 19、支出第 7）、[ElevenLabs](../products/elevenlabs.md)（Web 第 25、支出第 10）在支出榜进入前十；[Midjourney](../products/midjourney.md)（支出第 11）、[HeyGen](../products/heygen.md)（美国，支出第 23）、[Kling AI](../products/kling-ai.md)（支出第 26）、[Topaz Labs](../products/topaz-labs.md)（支出第 27）围绕各自专有模型进入支出榜。
- **交易型 Agent**：
  - Instinct：40% 用户在 3 周内绑定个人信用卡，首购后月均消费达 $1,300；年化商品交易总额（GMV）突破 $10 亿，约一半来自旅游场景（创始人披露）。
  - Meta Muse（9 月 9 日上线）：首周 DAU 达 25 万，首月下载破 500 万；上线两周内被 Amazon 封禁访问，但已与 Shopify、Instacart、OpenTable、Expedia、Ticketmaster、Plaid 达成官方集成。

---

## 3. 中国及华人团队产品表现

**官方正文与榜单确认的事实**：
1. **[DeepSeek](../products/deepseek.md)**：官方正文确认 Claude 在 Web 访问量上“已超越 DeepSeek 和 Perplexity 等竞争对手”，DeepSeek 位列 Web 榜第 5 名、移动榜第 14 名。
2. **[Kling AI](../products/kling-ai.md)（快手可灵）**：围绕专有视频模型进入美国消费者支出榜（支出榜第 26 名、Web 榜第 49 名）。此外，进入支出榜的中国产品还有 [EVOTO AI](../products/evoto-ai.md)（第 41 名）和 [MiniMax](../products/minimax.md)（第 42 名）。（注：[HeyGen](../products/heygen.md) 位列支出榜第 23 名，其总部位于美国，归为美国产品。）
3. **[Manus](../products/manus.md)**：由中国团队蝴蝶效应（Butterfly Effect）创立，2025 年中将总部迁至新加坡（2025 年 12 月 Meta 曾宣布拟以超 20 亿美元收购，2026 年 4 月因中国监管部门安全与技术出口审查叫停而解除交易，恢复新加坡独立运营）。本期被官方报告点名为美国前 1% 重度付费者超配（overindex）的工具之一（与 [n8n](../products/n8n.md)、[fal.ai](../products/fal-ai.md)、[Nous Research](../products/nous-research.md) 并列），位列支出榜第 19 名、Web 榜第 38 名。

**第三方参考与口径差异**：
- 豆包与剪映在 a16z 第 7 期移动榜中的具体 MAU 数字仅出现在官方图表图片中，正文未提供文本披露（CapCut 7.36 亿 MAU 为第 6 期即 2026 年 1 月数据）。
- 国内第三方口径（QuestMobile《2026 上半年 AI 应用市场发展洞察报告》，经 [BigGo 财经转引](https://finance.biggo.com/news/372811e2-28f1-49c7-9f53-fa56879cde3b)）：截至 2026 年 5 月，[豆包 (Doubao)](../products/doubao.md) 国内移动端 MAU 约 3.82 亿，[千问 (Qwen)](../products/qwen.md) 约 1.67 亿，[DeepSeek](../products/deepseek.md) 约 1.3 亿（该口径仅统计国内移动端，与 a16z 全球/海外口径不可直接对比）。

---

## 4. a16z 的核心判断与启示

1. **“重度付费经济（Power-user economy）”主导当前变现**：
   近半数美国网民表示使用过 AI，但仅 25% 每天使用，仅 4.5% 付费。消费 AI 找到的第一个真实付费市场，是愿意为构建产品、内容创作和完成工作支付高溢价的人群。
2. **头部固化与巨头分流**：
   - 新进产品数创七期新低（11 个），既有软件（[Canva](../products/canva.md)、[Notion](../products/notion.md)、[Figma](../products/figma.md)、[Superhuman](../products/superhuman.md)）依靠成熟工作流与分发渠道占据前列。
   - 三家大模型走向不同定位：Claude for work（专业工作人群）、Gemini for consumers（Google 生态分发）、ChatGPT for both（通用平台）。
3. **入口转向个人助手与工作流**：
   交互入口正从单一浏览器聊天框移向 iMessage、邮件、电话、浏览器插件和硬件设备。具备任务执行与交易结算能力的个人助手成为下一阶段竞争焦点。
4. **创业公司的四个切入位置**：
   - 官方正文总结的四个方向：**专有模型**（如 [Suno](../products/suno.md)、[Kling AI](../products/kling-ai.md)）、**多模型聚合体验**（如 [OpenRouter](../products/openrouter.md)）、**垂直人群深耕**（数据/隐私/工作流）、**新界面与硬件**（如 [Plaud](../products/plaud.md)）。
   - 商业模式上，单一订阅制触及大众市场天花板，广告与 Agent 交易抽成（affiliate / take rate）是主要探索方向；播客中 Olivia Moore 与 Jordan Elman 指出社交、约会、购物、娱乐等传统互联网大品类在 AI 原生应用上仍接近空白。

---

## 5. 与第 6 期（2026 年 3 月）对比

| 比较维度 | 第 6 期（2026-03，数据截至 2026-01） | 第 7 期（2026-10，数据截至 2026-08） |
| --- | --- | --- |
| **评选方法论** | 纯流量排名（Similarweb + Sensor Tower） | 流量排名 + **YipitData 美国消费者支出榜** |
| **ChatGPT 领先幅度** | Web 访问量为 Gemini 的 2.7 倍 | Web 访问量为 Gemini 的约 2 倍（口径与月份不同） |
| **ChatGPT 规模与变现** | 周活跃用户 9 亿 | 移动端 10 亿+ MAU；周活 12 亿；广告年化收入 $10 亿 |
| **Claude 态势** | 付费订阅 YoY +200%，处于高速增长期 | Web 升至第 3 名；高价档占比 7.3%；夏季增速放缓、流失上升 |
| **核心叙事** | 默认入口之争、地理分化（美/中/俄） | **Power-user economy**、谁在真正付费、既有软件反攻 |
| **Agent 形态** | 终端命令行开发者工具（如 OpenClaw） | 面向消费与交易结算的个人助手（Instinct、Muse 等） |
| **创意工具** | 独立通用图像生成器受挤压（Midjourney 跌至 Web #46） | Suno（支出 #7）、ElevenLabs（支出 #10）、Midjourney（支出 #11）、HeyGen（支出 #23）、Kling（支出 #26）进入支出榜 |
| **既有软件** | 首次调整规则纳入既有工具（CapCut 7.36 亿 MAU） | Canva、Notion 进 Web 前 10，Figma 进前 15，Superhuman 居支出第 4 |

---

## 局限与待核实

1. **支出榜样本局限**：YipitData 数据来自美国消费者信用卡与电子收据 panel 观测，未覆盖美国境外直接订阅，也未计入企业对公采购；Google Gemini 因无法从 Google 整体消费者订阅中拆分收入而未纳入支出榜。
2. **图表图片与正文披露差异**：豆包第 7 期移动端 MAU 约 3.15 亿来自 a16z 报告中的榜单图表图片，官方正文未单独披露文字数字；剪映（CapCut）7.36 亿 MAU 为第 6 期（2026 年 1 月）数据，第 7 期未披露更新值。
3. **LinkedIn 单帖链接待核实**：ChatGPT 移动端 10 亿+ MAU 与 Claude 月访问近 10 亿摘自 2026-10-05 a16z 官方 LinkedIn 动态，原始笔记仅保留机构主页链接（`https://www.linkedin.com/company/a16z/`），具体单帖 URL 待核实（2026-10-23）。
4. **国内与全球口径差异**：QuestMobile 国内移动端 MAU 数据与 a16z 全球/海外统计口径不同，不可直接横向加总或对比。

---

## Sources

1. **Andreessen Horowitz 官方报告**：[The Top 100 Gen AI Consumer Apps — 7th Edition](https://a16z.com/100-gen-ai-apps-7/)，Olivia Moore，2026-10-05。
2. **a16z 官方 LinkedIn 动态**：[a16z LinkedIn 主页](https://www.linkedin.com/company/a16z/)（2026-10-05 动态披露 ChatGPT 移动端 10 亿+ MAU 等数据，具体单帖 URL 待核实，2026-10-23）。
3. **Cryptobriefing 报道**：[A16z's seventh Top 100 Consumer AI Apps list follows the money](https://cryptobriefing.com/a16z-top-100-consumer-ai-apps-seventh-edition/)，2026-10-06。
4. **YOLOLAB 梳理**：[a16z 2026 消費者 AI 排名與支出數據解析](https://yololab.net/archives/a16z-top-100-consumer-ai-apps-2026-spending)，2026-10-06。
5. **a16z Show 播客**：*The Top 100 Consumer AI Apps: Who's Actually Paying?*，Olivia Moore & Jordan Elman，2026-10-05（[GoLoudNow 音频](https://www.goloudnow.com/podcasts/the-a16z-show-381/the-top-100-genai-products-ranked-and-explained-518312)、[YouTube 视频](https://www.youtube.com/watch?v=aCvrzhwUxg0)、[BigGo 摘要报道](https://finance.biggo.com/news/3caf4d8845cc152e)）。
6. **QuestMobile 数据（经 BigGo 财经转引）**：《2026 上半年 AI 应用市场发展洞察报告》，[BigGo 财经转引链接](https://finance.biggo.com/news/372811e2-28f1-49c7-9f53-fa56879cde3b)，2026-07-14。
