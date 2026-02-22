# 14个核心项目配置

projects = [
    {
        "id": "disaster-management",
        "name": "灾难管控策略",
        "desc": "T+1 快速响应 · 风险降幅 10%+",
        "category": "risk"
    },
    {
        "id": "quota-strategy-v5",
        "name": "额度策略 V5",
        "desc": "规模 2 倍+ · 风险持平",
        "category": "risk"
    },
    {
        "id": "rm-system",
        "name": "RM 风险管理系统",
        "desc": "500 亿在贷余额管理",
        "category": "risk"
    },
    {
        "id": "ai-deep-strategy",
        "name": "AI 深度策略",
        "desc": "借新还旧 · 提前结清 · 额度曲线",
        "category": "risk"
    },
    {
        "id": "kyc-platform",
        "name": "KYC 经营策略中台",
        "desc": "转化率 +15.6% · 月增 2.7 亿",
        "category": "risk"
    },
    {
        "id": "telesales-system",
        "name": "电销策略推荐系统",
        "desc": "转化率 +9.8% · 月增 1.1 亿",
        "category": "risk"
    },
    {
        "id": "year-end-report",
        "name": "年终总结报告",
        "desc": "策略体系 · 时间线 · 核心成果",
        "category": "data"
    },
    {
        "id": "weekly-monitoring",
        "name": "周报监控",
        "desc": "自动化周度风险监控",
        "category": "data"
    },
    {
        "id": "customer-segmentation",
        "name": "客群分层策略",
        "desc": "风险降 11.6% · 规模 +15.3%",
        "category": "risk"
    },
    {
        "id": "data-quality",
        "name": "数据质量校验",
        "desc": "自动化校验 · 效率提升 80%+",
        "category": "data"
    },
    {
        "id": "ai-sharing",
        "name": "AI 内部分享",
        "desc": "团队 AI 赋能 · 效率提升 30%+",
        "category": "ai"
    },
    {
        "id": "fof-system",
        "name": "智能投顾系统（FOF）",
        "desc": "8 亿+ 资产管理 · 年化 12.5%",
        "category": "ai"
    },
    {
        "id": "knowledge-base-agent",
        "name": "知识库 Agent",
        "desc": "RAG 检索 · 准确率 92.5%",
        "category": "ai"
    },
    {
        "id": "skills-dev",
        "name": "Skills 技能开发",
        "desc": "效率提升 50%+ · 规范遵守 95%+",
        "category": "ai"
    }
]

print(f"Total projects: {len(projects)}")
for p in projects:
    print(f"- {p['name']} ({p['category']})")
