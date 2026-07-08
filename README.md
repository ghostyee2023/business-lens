# business-lens · 商机透镜

> 判断一个产品机会的商业逻辑：谁会买，为什么买，怎么赚钱，先验证什么。

`business-lens` 是一个 AI agent skill。它不负责发散创意，也不负责设计产品原型；它专门做中间这层商业判断：

```text
候选机会
-> 商业逻辑链
-> 购买者 / 预算 / 获客 / 商业模式
-> 致命假设
-> proceed / reshape / park / reject
```

## 装上就能用

打开你正在用的 AI agent，告诉它：

```text
帮我安装这个 skill：https://github.com/ghostyee2023/business-lens
```

或者用通用 CLI 安装器：

```bash
npx skills add ghostyee2023/business-lens
```

## 适合什么场景

- 判断一个想法有没有商机
- 判断商业逻辑通不通
- 找出谁是用户、谁是购买者、预算从哪里来
- 判断适合模板、服务、插件、SaaS、工作坊还是诊断报告
- 找出最大的未验证假设
- 决定 proceed / reshape / park / reject

## 和另外两个 skill 的关系

```text
idea-spark      灵感火花：找机会
business-lens   商机透镜：判断商业逻辑
maker-forge     造物工坊：锻造成 3 小时 MVP
```

从资料里找机会，先用 `idea-spark`。  
判断是否值得做，交给 `business-lens`。  
要做第一版 MVP，再交给 `maker-forge`。

## 能做什么

| 能力 | 说明 |
| --- | --- |
| 商业逻辑链 | 从用户、痛点、替代方案、购买者、获客和交付完整检查 |
| 商机评分 | 评估痛点强度、购买者清晰度、预算匹配、获客可达、交付可重复 |
| 商业模式选择 | 判断适合模板、服务辅助 MVP、订阅、插件、数据产品等 |
| 致命假设 | 明确什么事实会让这个想法不成立 |
| 验证动作 | 输出本周可以做的真实测试，而不是收集口头赞美 |

## 示例提示词

```text
用 business-lens 判断这个想法有没有商机：给知识博主做一个从长文生成图卡选题的工具。
```

```text
这个产品谁会买？预算从哪里来？商业逻辑通不通？
```

```text
帮我判断这个机会应该 proceed、reshape、park 还是 reject。
```

## 边界

- 它不是财务、法律或投资建议。
- 它不会把“有用”直接等同于“能赚钱”。
- 它不会默认联网做市场研究，除非你明确要求。
- 它不会默认写文件，除非你明确要求保存或落地。

## License

MIT
