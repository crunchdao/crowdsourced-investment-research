---
title: "CROWDSOURCED INVESTMENT RESEARCH"
subtitle: "BY CRUNCHDAO"
author: [Matteo Manzi, Enzo Caceres]
date: "2022/11/01"
lang: "en"
colorlinks: true
titlepage: true
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "360049"
titlepage-rule-height: 0
titlepage-background: "./figures/cover.pdf"
header-left: "\\hspace{1cm}"
header-right: "Page \\thepage"
footer-left: "Crowdsourced Investment Research"
footer-right: "CrunchDAO"
abstract: "Markets are complex, high-dimensional, chaotic, stochastic, non-Gaussian dynamical systems. With a data-driven perspective, CrunchDAO's tokenomics powers a crowdsourced investment strategy that, via machine and ensemble learning, leads to competitive financial services."
---

# Crowdsourced Investment Research

## Introduction

[@Prado_2018] and [@Craib_2017] will be discussed here.

Figure \ref{fig:vc} shows the following:

![A portion of the fund’s performance is used to buyback $CRUNCH tokens, and use them as rewards for the next tournaments, leading to a virtuous cycle between the fund and the DAO.\label{fig:vc}](figures/virtuouscycle.png)

CrunchDAO aims at providing a \textit{market-neutral} signal: a signal able to generate returns regardless of market conditions. 

\begin{equation}
r_i = \sum_k X_{ik} f_k + u_i
\end{equation}

By balancing our model with long and short positions, we minimise our exposure to any inherent market risks.

## The Tournament

[@Prado_2019] will be discussed in this section;

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


### Staking

The CrunchDAO tournament asks individual to, given a dataset $X$ and a set of targets $y$, build a deterministic nonlinear model:

$$
y = f(X)
$$

In order to simplify the discussion, let's think about only one target for $N$ stocks from now on, so that $y$ is a vector $1 \times N$. We have $M$ players, so that every week a matrix $Y$ of size $N \times M$ is submitted. We assume that a vector of stakes $w$, of size $1 \times M$ is submitted as well.

A deterministic metamodel $\Psi$ is applied to obtain, from $(Y, w)$, a vector $\mu$, of size $1 \times N$. Using ensamble averaging, a simple example is a stake-weighted average.

This vector is the input of a constrained convex optimizer $\Phi(\mu)$, whose output is a vector $\omega$  with same size, which leads to a product with the desired characteristics: market neutral, high Sharpe ratio, high Sortino ratio. Let's assume the goal is to maximize the Sharpe ratio of the portfolio for the coming week $S(\omega)$.

At the submission level, we have two kinds of noise: one is noise due to sybills, one is noise due to the probabilistic nature of the proposed supervised learning problem. About the second, if the current dataset is associated with a highly unpredictable market regime, different fitted models will lead to highly different predictions. The metamodel should take this into account.

We also need a staking system that burns tokens from sybills and an associated metamodel that does not listen to them. Sybills submission are by definition belonging to a different probability distribution from $P(y)$, which we can reconstruct from a set of submissions. Hierarchical clustering, Gaussian Mixture, Independent Component analysis can be used to identify sybills in an unsupervised way (no scoring function defined, yet) and remove them.

Once sybills are removed, we can afford to use quadratic voting to perform ensambling: this removes "trend following" implicit assumptions to the pipeline (i.e., if you have a lot of tokens, you have been good in the past, but if a lot of people are pointing in a different direction from you, all together, we should listen more to them than to you, even if the sum of their stakes is lower than your stake). We cannot do this without a sybill resistance, which cannot come from Soul-bound tokens, as wallets can always turn into sybills.

To incentivise for originality, the ensembling is not done on the raw non-sybills, but on clusters of submissions, each of which is associated with the average stake of all the submissions in that cluster. To get the clusters I would use the covariance matrix of the non-sybill submissions (assuming therefore $P(y)$ to be a multivariate Gaussian, making the gaussian mixture a good mechanism to avoid listening to sybills), again in an unsupervised setting.

Up to now, we are only talking about a pipeline to use staking to build a good signal. But what about the reward for tournament players?

In order to align the interst of the DAO as a whole and the tournament players, the most natural choice is to compute the effect of each couple $(y_i, w_i)$ on the metric used to evaluate the product:

$$
S(\Phi(\Psi(Y)))
$$

Thinking about true contribution (the metric could also be nonlinear, as I mentioned quadratic voting, but let's keep it simple), the problem is that 

$$
\nabla_{w_i} S(\Phi(\Psi(Y)))
$$

is not only a function of $y_i$, but also of the other $M-1$ submissions and stakes.

A partial solution is to make all the scripts of the pipeline open source. We cannot however share the data associated with $\Phi$. Also, $Y$ is not known in advance.

Assuming some degree of inertia in $Y$ and the data associated with $\Phi$ from one week to another, each player can play "offline" against the other submissions to maximize:

$$
\nabla_{w_i} \Phi(\Psi(Y))
$$

We are here also assuming that the function $S$ is as close to the identity as possible (desirable, as we would like to predict the market, and building a pipeline for which it is true that past performance is the best predictor of success is what we are aiming at).

As the optimal behaviour would be for each player to update their prediction according to the set of predictions of the other players, knowing all the players would optimally do it, the Nash equilibrium would be to update all the predictions until an equilibrium point of the associated discrete dynamical system (assuming such equilibrium exists). Given all this necessary considerations, it is clear how ill-posed the Numerai true contribution setup is.

If such Nash equilibrium exists, if the inertia assumption on the set of non-sybill submissions and associated staking and on the dataset used in the optimizer are met, such setup can work, even being complex. This would also burn sybill stakes without listening to them. The gradient would be the effect of adding an infinitesimal contribution of noise to the pipeline, negative.

If not, I would simplify the discussion and score people on 

$$
\nabla_{w_i} \Phi(y_i)
$$

### The Scoring System

- [Spearman's rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)

## Clustering and Dimensionality Reduction

Symbil attacks: [@Li_2017].

[@Avellaneda_2019], [@Akansu_2021] will be discussed here.

## Ensemble learning

Ensamble Averging will be presented here.

## Porfolio Optimization

[@Chriss_2005], [@Crama_2003]

The constraints for CrunchDAO's portfolio are neutrality with respect to dollar, Risk Indices, Styles factors and Industry factors.

Markovitz porfolio theory and constraints are discussed here.

# References
