---
title: "CROWDSOURCED INVESTMENT RESEARCH"
subtitle: "BY CRUNCHDAO"
author: [Matteo Manzi]
date: "2022/11/01"
lang: "en"
colorlinks: true,
titlepage: true,
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "360049"
titlepage-rule-height: 0
titlepage-background: "./figures/cover.pdf"
header-left: "\\hspace{1cm}"
header-right: "Page \\thepage"
footer-left: "Crowdsourced Investment Research by CrunchDAO"
footer-right: "Matteo Manzi"
---

# List of contributors

| Full Name | Github @ | Discord @ | Date |
|----------|:---------------:|:-----------------:|------------|
| Matteo Manzi | matteoettam09 | matteoettam09#9362 | 2022/10/28 |
|||||
|||||
|||||

\newpage

# Crowdsourced Investment Research

## Introduction

- [@Prado_2018]

- Discuss (Figure \ref{fig:vc})

![A portion of the fund’s performance is used to buyback $CRUNCH tokens, and use them as rewards for the next tournaments, leading to a virtuous cycle between the fund and the DAO.\label{fig:vc}](figures/virtuouscycle.png)


Structure of the paper:

- Tournament
- Metamodeling
- Portfolio Optimization

## The Tournament

- [@Prado_2019] to be discussed in this section;


### Data

- Quantization & Obfuscation. Quantile-based/fixed scale quantization.

Proprietary Data and Community Data.

- [Weavechain](https://www.weavechain.com/): [arweave](https://www.arweave.org/) and [filecoin](https://filecoin.io/) make use of IPFS, they do not. Data do not go on chain. [BeekeperAI](https://www.beekeeperai.com/)

- Homomorphic Encryption links [here](https://github.com/microsoft/EVA), [here](https://github.com/microsoft/SEAL), [here](https://www.zama.ai/) CKKS [here](https://blog.openmined.org/ckks-explained-part-1-simple-encoding-and-decoding/).

- [Federated learning](https://en.wikipedia.org/wiki/Federated_learning) + [Ocean Protocol](https://oceanprotocol.com/) for new datasets.

- Confidential Computing: [paper](https://arxiv.org/abs/2110.01390) and [repo](https://github.com/data61/MP-SPDZ) discussing SPDZ.

- [PySyft](https://github.com/OpenMined/PySyft): Syft allows a Data Scientist to ask questions about a dataset and, within privacy limits set by the data owner, get answers to those questions, all without obtaining a copy of the data itself.

- [Zero-knowledge proof](https://en.wikipedia.org/wiki/Zero-knowledge_proof)

CrunchDAO makes use of different datasets.

- C-MECHANICS
- E-KINETIC
- B-VOLATILITY
- 3B1-SIGNAL
- DOLLY
- GORDON-GEEKO

- How can people add different datasets? Mention [Weavechain](https://www.weavechain.com/) and DeSci Collaborative Data, and https://oceanprotocol.com/

- Discuss how all the metamodels are combined.

### Staking


### The Scoring System

- [Spearman's rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)

## Clustering and Dimensionality Reduction

Discuss symbill attacks and [@Li_2017].

[@Avellaneda_2019], [@Akansu_2021]

## Ensemble learning

There is a need to align the incentives of the single tournament players with the DAO as a whole. Tournament players cannot build their model on some data aiming at maximizing a correlation score when the DAO pays based on a different metric: if we want to treat tournament players fairly, we have to give them access to the metamodel, so that they can adjust their goal to the maximization of the True Contribution. We are assuming that such metric is the best objective, at the tournament level, that maximizes the long-term performance of the signal produced by the DAO. Moreover, there is alredy a problematic assumption in splitting this optimization problem into a sequence of two optimization problems. More research is necessary.

Mean and Median. Discuss Ensamble Averging.

## Porfolio Optimization

[@Chriss_2005], [@Crama_2003]

- [Convex Optimization](https://en.wikipedia.org/wiki/Concavification), but keep also in mind [Convexification](http://larsblackmore.com/publications.htm) done in space: I would expect here to have something similar, if not more non-convex.

- Targets defined by [Barra Risk Factor Analysis](https://www.investopedia.com/terms/b/barra-risk-factor-analysis.asp);

# References
