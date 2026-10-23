# 公开数据

这里保存已核对、适合公开的数据。原始交付及处理中数据留在本地 `private/`。当前没有数据行，以下只定义首批整理字段。

| 字段 | 含义 |
| --- | --- |
| product_id | 仓库内稳定标识，用于关联同一产品 |
| product_name | 来源中的产品名称 |
| website_url | 产品官网 |
| edition | 榜单期次，依据来源填写 |
| ranking_scope | 榜单范围，例如 Web 或 App，依据来源填写 |
| rank | 该榜单内排名 |
| metric_name | 排名指标名称，依据来源填写 |
| metric_value | 指标值，未知留空 |
| metric_unit | 单位，依据来源填写 |
| measurement_period | 数据统计期 |
| source_id | 对应 sources.csv 中的来源标识 |
| notes | 口径说明或缺失原因 |

数据文件优先使用 UTF-8 CSV。日期使用 ISO 8601；保留来源的指标和单位，不混用榜单发布日期、访问日期和统计期。主观分类、商业模式判断等派生字段需要另写定义和依据。
