## Summary

Summary: This paper examines the play-style characteristics of football RL agents and how strategies may develop during training. It uses deep reinforcement learning (RL) methods to develop agents that excel in a wide range of applications, and applies social network analysis (SNA) to explore what can be learnt from the use of simulated environments. It was found that there is a strong correlation between the agent’s competitiveness and various SNA metrics, and aspects of the RL agent’s play style become similar to real-world footballers as the agent becomes more competitive.

Experiments: An agent was trained using proximal policy optimization in a Google Research Football simulation environment for 50 million timesteps against the built-in easy, medium, and hard-level bots. The TrueSkill ranking system was used to rank the agents, and pagerank was calculated based on the total number of passes a player made. The metrics used to analyze playing characteristics included number of passes/shots, and social network analysis metrics such as closeness, betweenness, and pagerank. It was found that ”Total Shots” and ”Betweenness (mean)” had a strong positive correlation with TrueSkill rankings, and the metric with the largest overall correlation was the pagerank aggregated by the minimum value in the network. 

Further reading: To learn more about the application of RL in football, the paper ‘Robot Soccer’ by Itsuki (1995) and ‘Reinforcement Learning for Robot Soccer’ by Wunsch (2015) are recommended readings. 

Glossary: 
- Deep Reinforcement Learning (DRL): A subset of RL that combines the traditional reinforcement learning setup with deep neural networks 
- Proximal Policy Optimization (PPO): An algorithm used to learn policies for agents to play Google Research Football 
- Social Network Analysis (SNA): A technique used to analyze the intelligence of coordinated RL agents and compare their characteristics with real-world data 
- TrueSkill Ranking System: A round-robin tournament used to rank the agents

## Summary (Japanese)

概要：本論文では、サッカーRLエージェントのプレイスタイルの特徴と、トレーニング中にどのように戦略が発展する可能性があるかを検証している。深層強化学習（RL）法を用いて、幅広い用途に秀でたエージェントを開発し、ソーシャルネットワーク分析（SNA）を適用して、シミュレーション環境の利用から何が学べるかを探っている。その結果、エージェントの競争力とSNAの各種指標には強い相関があり、RLエージェントのプレイスタイルの側面は、エージェントの競争力が高まるにつれて現実世界のサッカー選手と似てくることが判明しました。

実験Google Research Football のシミュレーション環境において，プロキシマルポリシー最適化を用いて，内蔵のイージーレベル，ミディアムレベル，ハードレベルのボットに対して 5000 万タイムス テップのトレーニングを実施した．エージェントのランク付けには TrueSkill ランキングシステムを使用し、選手が行ったパスの総数に基づいてページランクを計算した。プレイ特性を分析するための指標として，パス数/ショット数，近さ，間 隔，ページランクなどのソーシャルネットワーク分析指標を用いた．その結果、「総ショット数」と「betweenness（平均値）」は TrueSkill のランキングと強い正の相関があり、全体として最も相関が大きい指標は、ネットワーク内の最小値で集計したページランクであることが判明した。

さらに読むサッカーにおけるRLの応用について詳しく知りたい方は、五木（1995）の論文「Robot Soccer」とWunsch（2015）の論文「Reinforcement Learning for Robot Soccer」がお勧めの文献です。

用語解説はこちら
- Deep Reinforcement Learning（DRL）。従来の強化学習セットアップとディープニューラルネットワークを組み合わせたRLのサブセット
- 近位政策最適化(PPO)。Google Research Footballをプレイするエージェントのポリシーを学習するために使用されるアルゴリズム
- Social Network Analysis (SNA)。協調型RLエージェントの知能を分析し、その特徴を実世界のデータと比較するために使用される手法
- TrueSkill Ranking System（トゥルースキルランキングシステム）。ラウンドロビン方式によるエージェントのランキングシステム

## Images
![img-83](outputs/2111.12340/img-83.png)

![img-174](outputs/2111.12340/img-174.png)

![img-270](outputs/2111.12340/img-270.png)

![img-311](outputs/2111.12340/img-311.png)

![img-265](outputs/2111.12340/img-265.png)

![img-318](outputs/2111.12340/img-318.png)

![img-309](outputs/2111.12340/img-309.png)

