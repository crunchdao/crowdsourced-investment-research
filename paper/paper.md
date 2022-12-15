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
abstract: "Markets are complex, high-dimensional, chaotic, stochastic, non-Gaussian dynamical systems. With a data-driven perspective, CrunchDAO's tokenomics powers a crowdsourced investment strategy that, via Machine and Ensemble Learning, leads to competitive financial services."
---

# Crowdsourced Investment Research

## Introduction

In the context of quantitative finance, in which a systematic, rationalized, quantitative (i.e., scientific) approach is preferred over discretionary decision-making, the field of machine learning is getting a lot of traction [@Prado_2018]. This is because of its natural compatibility with a Bayesian approach [@Barber_2012], characterizing the field of econometrics, but also because of its potential to construct nonlinear models from financial data [@Chan_2022].

In this context, CrunchDAO proposes an Ensamble Learning framework via tournaments ([@Craib_2017], [@Prado_2019]), in order to generate \textit{market-neutral} signals.

## Traditional Econometrics and Risk

\begin{equation}
r_i = \sum_k X_{ik} f_k + u_i
\end{equation}

## Data

CrunchDAO makes use of different datasets.

- C-MECHANICS: This strategy is a trend-following strategy based on the trend of idiosyncratic (an individualizing characteristic) return and volatility.
- E-KINETIC: This momentum outlook aims to systematically isolate and harvest excess returns arising from behavioral market anomalies by investing in diversification, not performance.
- B-VOLATILITY: This strategy identifies distortions in volume, price, and volatility between short-dated options and stock prices.
- 3B1-SIGNAL: Institutional investors are leveraging equity factor risk models (Sector / Country Stock etc.) to predict return and hedge their bets.  We investigate the extent to which nonlinearities not captured by standard linear models within equity factor risk models are present. Some generated factor returns and information ratios higher than corresponding linear factors
- DOLLY: Portfolio managers invest a tremendous amount of time and resources in identifying equity that will outperform the market in the long term - alpha- ; In Dolly, the community leverages machine learning to select top long-term asset managers and piggyback their trades. Securities and Exchange Commission (SEC) 13f filing data offer valuable insight into top asset managers’ holdings at each quarterly filing point.
- GORDON-GEEKO: This strategy uses trade information from top management and senior executives (i.e. insiders) as it has been demonstrated in past academic research that insiders have insight - or alpha - over other investors.

### Anonymization 

Data anonymization is performed using quantization schemes.

Here is a non-esaustive list of interesting projects we have been researching and that could provide interesting tools to challange the current design choices:

- [PySyft](https://github.com/OpenMined/PySyft)
- [Weavechain](https://www.weavechain.com/) 
- [BeekeperAI](https://www.beekeeperai.com/)
- [Microsoft SEAL](https://github.com/microsoft/SEAL) and [associated compiler](https://github.com/microsoft/EVA)
- [ZKML](https://github.com/zkml-community/awesome-zkml)
- [Zama](https://www.zama.ai/)

## Tournament

### Staking

A set of proposal are currently being discussed to find a solution for Sybil attack resistance: [@Li_2017].

### The Scoring System

The current Scoring metric is the [Spearman's rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) between the submission and the realized targets.

## Metamodeling

### Clustering and Dimensionality Reduction

[@Avellaneda_2019], [@Akansu_2021] will be discussed here.

### Ensemble learning

Ensamble Averging will be presented here.

### Porfolio Optimization

[@Chriss_2005], [@Crama_2003]

The constraints for CrunchDAO's portfolio are neutrality with respect to dollar, Risk Indices, Styles factors and Industry factors.

Markovitz porfolio theory and constraints are discussed here.

# References
