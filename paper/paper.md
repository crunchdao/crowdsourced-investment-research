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

- [@Craib_2017]

- Discuss (Figure \ref{fig:vc})

![A portion of the fund’s performance is used to buyback $CRUNCH tokens, and use them as rewards for the next tournaments, leading to a virtuous cycle between the fund and the DAO.\label{fig:vc}](figures/virtuouscycle.png)

CrunchDAO aims at providing a \textit{market-neutral} signal: a signal able to generate returns regardless of market conditions. 

\begin{equation}
r_i = \sum_k X_{ik} f_k + u_i
\end{equation}

By balancing our model with long and short positions, we minimise our exposure to any inherent market risks.

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

- C-MECHANICS: This strategy is a trend-following strategy based on the trend of idiosyncratic (an individualizing characteristic) return and volatility.
- E-KINETIC: This momentum outlook aims to systematically isolate and harvest excess returns arising from behavioral market anomalies by investing in diversification, not performance.
- B-VOLATILITY: This strategy identifies distortions in volume, price, and volatility between short-dated options and stock prices.
- 3B1-SIGNAL: Institutional investors are leveraging equity factor risk models (Sector / Country Stock etc.) to predict return and hedge their bets.  We investigate the extent to which nonlinearities not captured by standard linear models within equity factor risk models are present. Some generated factor returns and information ratios higher than corresponding linear factors
- DOLLY: Portfolio managers invest a tremendous amount of time and resources in identifying equity that will outperform the market in the long term - alpha- ; In Dolly, the community leverages machine learning to select top long-term asset managers and piggyback their trades. Securities and Exchange Commission (SEC) 13f filing data offer valuable insight into top asset managers’ holdings at each quarterly filing point.
- GORDON-GEEKO: This strategy uses trade information from top management and senior executives (i.e. insiders) as it has been demonstrated in past academic research that insiders have insight - or alpha - over other investors.

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

The constraints for CrunchDAO's portfolio are neutrality with respect to dollar, Risk Indices, Styles factors and Industry factors.

- [Convex Optimization](https://en.wikipedia.org/wiki/Concavification), but keep also in mind [Convexification](http://larsblackmore.com/publications.htm) done in space: I would expect here to have something similar, if not more non-convex.

- Targets defined by [Barra Risk Factor Analysis](https://www.investopedia.com/terms/b/barra-risk-factor-analysis.asp);

# References
