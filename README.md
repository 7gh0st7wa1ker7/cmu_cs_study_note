# 一、这个项目里“必学”的课程有哪些？

这里我先分成两层：
- 1.学校官方要求的必学
- 2.我认为真正不能跳过的“核心能力课”

## 1）官方必学课程

### A. Computer Science Core 必修

这些基本就是 CS 主干：
- 07-128 First Year Immigration Course
- 15-122 Principles of Imperative Computation
- 15-150 Principles of Functional Programming
- 15-210 Parallel and Sequential Data Structures and Algorithms
- 15-213 Introduction to Computer Systems
- 15-251 Great Ideas in Theoretical Computer Science
- 15-451 Algorithm Design and Analysis

此外还必须从下面各类中各选课：

#### B. AI Elective（1门）

例如：
- 07-280 Artificial Intelligence and Machine Learning I
- 10-301 Introduction to Machine Learning
- 11-411 Natural Language Processing
- 11-485 Introduction to Deep Learning
- 15-281 Artificial Intelligence
- 16-385 Computer Vision

#### C. Domains Elective（1门）

例如：
- 15-330 Introduction to Computer Security
- 15-362 Computer Graphics
- 17-313 Foundations of Software Engineering
- 05-391 Human Centered Software

#### D. Logic / Languages Elective（1门）

例如：
- 15-311 Logic and Mechanized Reasoning
- 15-312 Foundations of Programming Languages
- 15-316 Software Foundations of Security and Privacy
- 17-355 Program Analysis

#### E. Systems Elective（1门）

例如：
- 15-410 Operating System Design and Implementation
- 15-411 Compiler Design
- 15-418 Parallel Computer Architecture and Programming
- 15-440 Distributed Systems
- 15-441 Networking and the Internet
- 15-445 Database Systems

#### F. 两门 SCS Electives

从 SCS 里再选两门高年级课。

---

### B. 数学必修

15-151 Mathematical Foundations for Computer Science
21-120 Calculus I
21-122 Calculus II
21-241 / 21-242 Linear Algebra
21-259 / 21-266 / 21-268 / 21-269 Multivariable Calculus

概率课四选一：
- 15-259
- 21-325
- 36-218
- 36-225 + 36-226

---

### C. 其他必修

**1门 Technical Communication**
**Science / Engineering**
**Humanities / Arts**
**99-101 Core@CMU**
**Minor 或 Concentration**

# 二、我认为真正不能跳过的“核心能力课”

如果你的问题不是“学校要求”，而是“以后真想成为强的工程师 / 研究者，哪些课必须掌握”，我会列这个版本：

---

## 1. 编程基础

### 15-122

这是非常重要的基础课。

它不只是“会写代码”，而是：
- 正确性
- 数据结构基础
- imperative programming
- C 语言与底层意识
- 从算法到实现的落地能力

这是后面 systems、AI systems、高性能工程的起点。

---

## 2. 函数式与抽象能力

### 15-150

这门课很值钱，因为它训练：
- 抽象建模能力
- 类型与递归思维
- 更强的程序结构意识

对未来做编译器、PL、形式化验证、甚至大模型工具链都很有帮助。

---

## 3. 算法与数据结构

### 15-210

这是工程与算法之间真正的桥梁。

重点是：
- 数据结构
- 并行与顺序算法
- 分析能力
- 性能意识

如果以后做 AI infra、搜索、推荐、分布式训练、编译优化，这门课的价值非常大。

---

## 4. 系统基础

### 15-213

这是我认为全页面里最关键的课之一。

它训练你理解：
- 程序如何执行
- 内存
- 编译器生成的机器代码
- 性能优化
- 并发
- 网络基础

未来最稀缺的人，不是只会调 API 的人，而是既懂 AI 又懂系统的人。

---

## 5. 理论基础

### 15-251

训练：
- 离散数学
- 可计算性
- 复杂性
- 概率与图论思维
- 严格证明能力

它让你以后学算法、密码学、复杂度、形式化方法时不会漂。

---

## 6. 高级算法

### 15-451

这是从“会用算法”到“懂算法设计”的升级。

训练：
- 降维打击式的问题建模能力
- 正确性证明
- 最优性分析
- NP-hard / approximation / advanced techniques

如果以后走研究、量化、复杂系统优化、AI 推理优化、搜索与规划方向，非常重要。

---

## 7. 概率 / 统计

### 首选 15-259 或 36-218

如果你想走 AI，这部分不能弱。

你要真正掌握：
- 随机变量
- 条件概率
- Bayes 思维
- concentration
- basic stochastic processes

未来所有 AI、推荐、搜索、因果、强化学习、评估、实验设计都离不开它。

---

## 8. 线性代数

### 21-241

AI、图形学、优化、信号处理、机器人、科学计算都需要它。

重点不是考试，而是要真正熟悉：
- 向量空间
- 特征值分解
- SVD
- projection
- 矩阵视角理解模型

---

## 9. 至少一门真正硬核系统课

我推荐在以下里至少拿下一门：
- 15-410 Operating Systems
- 15-440 Distributed Systems
- 15-445 Database Systems
- 15-418 Parallel Computer Architecture and Programming
- 15-411 Compiler Design

如果只能选一门，我通常推荐：
- **第一优先：15-440 Distributed Systems**
- **第二优先：15-410 Operating Systems**
- **第三优先：15-445 Database Systems**

---

## 10. 至少一门真正 AI 课

我推荐优先顺序：
- 10-301 Introduction to Machine Learning
- 11-485 Introduction to Deep Learning
- 15-281 Artificial Intelligence
- 11-411 NLP
- 16-385 Computer Vision

---

# 三、我推荐的学习路径

我先给你一个 标准 CS 强基路线，再给一个 面向未来 AI 的优化路线。

---

## 方案A：标准强基路线

适合目标：
- 不想太早定方向
- 想打硬基础
- 后续可转 AI / 系统 / 理论 / 安全 / 图形

### 阶段1：基础构建

1. 15-122
2. 15-150
3. 15-210
4. 15-213
5. 15-251
6. 数学：线代 + 概率 + 微积分

目标：
- 写代码
- 懂抽象
- 懂系统
- 懂理论
- 懂数学

### 阶段2：确定“主轴”

接下来选一条主轴：

#### 主轴A：系统

- 15-410
- 15-440
- 15-445
- 15-418
- 15-441

#### 主轴B：AI / ML

- 10-301
- 11-485
- 11-411
- 16-385
- 15-281

#### 主轴C：理论 / PL / Security

- 15-311
- 15-312
- 15-316
- 15-414
- 15-455
- 15-356

#### 主轴D：图形 / 视觉 / 几何

- 15-362
- 16-385
- 15-463
- 15-468
- 15-458

### 阶段3：做项目或研究

一定要做至少一种：
- research
- 系统项目
- 开源贡献
- internship
- thesis

因为你真正的能力不是“上过课”，而是：
- 能否做出系统
- 能否复现论文
- 能否独立 debug
- 能否把 idea 变成可运行结果

---

# 四、后续的发展方向分哪几块？

我会把未来 5-10 年的 CS / AI 方向划分成 8 大块：

## 1. AI / Machine Learning

内容：
- 机器学习
- 深度学习
- NLP
- CV
- 多模态
- 生成式 AI
- RL

适合：
- 想做模型、训练、应用研究的人

核心能力：
- 数学
- 概率
- 线代
- 优化
- Python / PyTorch
- 实验能力

## 2. AI Systems / Infrastructure

内容：
- 训练系统
- 推理系统
- 分布式训练
- GPU 编译
- serving
- 数据管道
- 向量检索
- agent runtime

适合：
- 想做“让 AI 真正跑起来”的人

核心能力：
- 15-213
- OS / Distributed / DB / Parallel
- C++ / Rust / CUDA
- 性能优化
- 系统设计

这是我非常看好的方向，未来非常缺人。

---

## 3. Systems / Distributed / Cloud

内容：
- 操作系统
- 分布式系统
- 存储
- 网络
- 数据库
- 云计算

适合：
- 喜欢工程硬核、基础设施、性能与可靠性的人

## 4. Programming Languages / Compiler / Formal Methods

内容：
- 编译器
- 静态分析
- 类型系统
- 程序验证
- theorem proving
- program synthesis

适合：
- 喜欢抽象、逻辑、语言设计、工具链的人

在 AI 时代，这条线会和“AI 编程工具”“代码生成验证”“安全推理”强结合。

---

## 5. Security / Privacy / Cryptography

内容：
- 系统安全
- 软件安全
- 隐私保护
- 密码学
- 区块链
- AI 安全

适合：
- 喜欢攻防、严谨性、可信系统的人

---

## 6. Graphics / Vision / Geometry / Simulation

内容：
- 图形学
- 视觉
- 几何处理
- 物理仿真
- 渲染
- XR

适合：
- 喜欢视觉表达、3D、仿真、计算几何的人

未来也会与生成式 3D、机器人世界模型、数字孪生结合。

---

## 7. Human-Computer Interaction / Product / Applied Computing

内容：
- HCI
- 人机交互
- design
- product systems
- AI 产品设计

适合：
- 想做用户价值、产品落地、交互设计的人

---

## 8. Theory / Algorithms / Optimization

内容：
- 算法
- 复杂度
- 随机化
- 博弈论
- 优化
- 量子
- 计算数学

适合：
- 喜欢深度思考、抽象问题、研究的人

---

# 五、基于我对未来 AI 发展的判断，我推荐的学习路径是什么？

这是你问题里最重要的部分。

我先给结论：

**未来最有价值的人，不是：**
- 只会调大模型 API 的人
- 只会做 prompt engineering 的人
- 只会套现成框架的人

**未来最有价值的人是：“算法理解 + 系统能力 + 产品落地 + 可信性意识”兼备的人**

也就是说，未来不会只分“AI”和“非AI”，而会分成：
1. 只会用 AI 工具的人
2. 能构建 AI 系统的人
3. 能推动 AI 成为可靠生产力的人

我建议你瞄准第 2 和第 3 类。

---

# 六、我最推荐的未来 AI 路径：T 型结构

我建议构建一个 T 型能力结构：

**横向基础（必须宽）**
- 编程
- 数据结构与算法
- 系统
- 概率统计
- 线代
- 软件工程
- 技术沟通

**纵向专长（必须深）**
在下面四条里选一条做深：
1. 模型与算法
2. AI 系统与基础设施
3. AI + 安全 / 可信
4. AI + 垂直应用领域

---

# 七、我推荐的“未来 AI 最优学习路径”

## 路线 1：AI Systems Engineer 路线（我最推荐）

这是我最看好的路线之一。

### 为什么？

未来大模型会越来越普及，但瓶颈会在：
- 训练成本
- 推理成本
- latency
- reliability
- 数据治理
- agent orchestration
- memory / retrieval
- infra scalability

这些都需要 系统型人才。

### 课程建议

基础：
- 15-122
- 15-150
- 15-210
- 15-213
- 15-251
- 15-451
- 21-241
- 15-259 / 36-218

AI：
- 10-301
- 11-485
- 11-411 或 16-385

系统：
- 15-440 Distributed Systems
- 15-445 Database Systems
- 15-418 Parallel Computer Architecture
- 15-410 OS
- 15-411 Compiler Design
- 可加：15-442 Machine Learning Systems

项目方向：
- 分布式训练框架
- 推理优化
- KV cache / serving
- RAG infra
- 向量数据库
- 多 agent runtime
- 模型评估平台
- 数据处理管线

### 未来岗位
ML Systems Engineer
AI Infrastructure Engineer
Distributed Systems Engineer
Inference Engineer
Performance Engineer
Applied Research Engineer

这是一个未来 10 年都非常强势的路线。

## 路线 2：Model / Research Engineer 路线

适合：
- 真心喜欢模型
- 愿意啃数学
- 愿意做实验和论文

### 核心课程

10-301
11-485
11-411
16-385
15-281
概率、线代、优化强化
再选一门系统课保底：15-213 + 15-440/15-445

### 项目方向

训练小模型
复现论文
instruction tuning
multimodal
alignment / evaluation
retrieval-enhanced learning

### 风险

纯模型方向竞争会越来越卷，而且更依赖：
- 顶级资源
- 算力
- 论文环境

所以我建议：即使走模型路线，也必须补系统能力。

## 路线 3：AI + Security / Trustworthiness 路线

我也非常看好。

### 为什么？

未来 AI 大规模部署后，核心问题一定不是“能不能生成”，而是：
- 能不能信
- 会不会泄露
- 能不能防攻击
- 能不能审计
- 能不能验证
- 能不能合规

### 课程建议

15-330 Introduction to Computer Security
15-316 Software Foundations of Security and Privacy
15-414 Automated Program Verification
15-311 / 15-312
15-213
15-440
10-301 / 11-485

### 项目方向

LLM security
jailbreak defense
prompt injection defense
model privacy
data provenance
secure agent execution
verifiable AI pipelines

### 未来岗位

AI Security Engineer
Trustworthy AI Engineer
AI Governance Tooling Engineer
Privacy / Security Researcher

---

## 路线 4：AI + Product / Applied Domain 路线

适合：
- 更想做落地产品，而不是最底层研究
- 希望快速形成行业价值

适合结合的领域
- 医疗
- 金融
- 法律
- 教育
- 科学计算
- 机器人
- 制造业

### 课程建议

核心 CS 不变，外加：
- 05-391 HCI
- 17-313 Software Engineering

### 领域课程

10-301 / 11-485 / 11-411

### 项目方向

垂直行业 copilot
workflow automation
knowledge system
enterprise AI agent
human-in-the-loop decision systems

这是“最容易快速产生商业价值”的路线。

# 八、如果是我自己读这个项目，我会怎么选？

如果目标是 未来 10 年最强综合竞争力，我会这样配：

**核心必打牢**
15-122
15-150
15-210
15-213
15-251
15-451
21-241
15-259 / 36-218
AI 方向
10-301
11-485
11-411

**Systems 方向**
15-440
15-445
15-418

**如果还能多学：**
15-410
15-442
Logic / Security 方向补一门
15-316 或 15-312 或 15-311
Domain / Product 补一门
17-313 或 05-391

---

# 九、最推荐的实际学习顺序

## 第1阶段：基础年

15-122
15-150
15-213
15-210
15-251

数学（线代、概率）
目标：
- 成为真正合格的 CS 学生

## 第2阶段：探索年

同时试三条线：
- 一门 AI：10-301
- 一门系统：15-440 或 15-445
- 一门逻辑/安全/软件工程：15-312 / 15-316 / 17-313

目标：
- 找到自己更适合哪种“深度”
- 第3阶段：聚焦年

如果你发现自己最强的是：

- A. 数学+实验
  - 走模型 / research engineer

- B. 工程+性能+架构
  - 走 AI systems / infra

- C. 严谨+安全+验证
  - 走 AI trust / security

- D. 用户价值+业务理解
  - 走 AI product / vertical

## 第4阶段：成果年

至少拿出 2-3 个像样成果：
- 1个深项目
- 1段实习/研究
- 1个公开作品（论文/开源/博客/系统demo）

# 十、我给你的最终建议

如果你问我一句话版本：
未来最值得走的路径是：
“硬核 CS 基础 + 系统能力 + AI 能力 + 一个真实场景落地方向”

## 最推荐组合

### 组合 A：最强就业与长期价值

核心基础课
AI（ML + DL）
分布式系统 + 数据库 + 并行
安全/验证补一门

### 组合 B：最强研究潜力

核心基础课
概率/线代强化
ML + DL + NLP/CV
理论/PL/优化补强

### 组合 C：最强商业落地

核心基础课
ML + NLP
软件工程 + HCI
一个垂直行业
