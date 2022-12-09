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


### Staking - Crunch Token
1. Inspired from [Validator-Delegator model of Cosmos blockchain](https://hub.cosmos.network/main/validators/validator-faq.html#how-to-become-a-validator).
2. In CrunchDAO context: Validators -> MM heros, Delegators -> MM supporters
3. 100 Heros with the highest total stake are chosen for creating the stakeweighted MM.
4. All holders of the Crunch token can act as supporters by backing their fav hero. Supporters are eligible for getting a cut of payouts from the hero pool they staked on. (Hero stake + supporter stake considered for top 100 selection)
5. To avoid frequent stake switches by supporters, their stake is locked for 1 month.
6. Heros can decide on their commission and a fixed fees. This will allow for competition between heros to attract supporters (and be among the top 100 staked).
7. Hierarchical Clustering can be used to find submissions belonging to a common cluster. Submissions belonging to the same cluster should be penalised.
8. As tournament progresses and it gets more unique submissions, the limit of 100 heros can be increased through community vote.


Why this scheme makes sense:

1. Encourages competition among heros and motivates them to continuously improve their models to attract supporters.
2. More involvement from general token holders who believe in the project, not just modellers.
3. Token holders will want the MM to do well, hence will stake on the model which contributes positively.
4. Good for overall tokenomics. As most of the tokens will be staked.
5. Payouts create positive feedback and can be restaked instead of selling in open market.
6. Unique scheme not followed by any of the competitors.


Fineprints:

1. Burning should be enabled post staking.
2. Stake cap on models. If stake limit is reached, supporters can't stake on that model, they have to stake on some other model. This will encourage decentralization and diversification.
3. Payout factor decreases if the model is part of an existing cluster. i.e if 5 models fall in the same cluster, payout factor=1/5 for all the 5 models. This would also encourage supporters to stake somewhere else i.e. stake on unique models.

Sybil attacks will be avoided due to staking. And supporters will tend to stake on a reliable model which will further prevent sybil attacks.
Payouts will only be made to staked (possibly top 100 staked) models, so no value in pursuing sybil attacks.

Problems with K-Means clustering in CrunchDao context:

1. K-means clustering is dependent on how it selects the initial points as cluster centroids. So, entirely different clusters are possible just by changing the random seed. Similar submissions might fall in different clusters in one run, and in same cluster in another run. This unpredictability is undesirable (and might seem unfair if unexpected results show up).
2. K-Means requires the 'K' parameter, i.e. we need to specify upfront how many clusters should be formed. This is non-trivial and requires another level of analysis called the 'Elbow method'; this is a visual analysis for finding the appropriate value of 'K'. This again is a subjective choice and somebody will be required to select that value for each round, this again is undesirable.

Benefits of Hierarchical clustering (Agglomerative clustering) in CrunchDao context:

1. No randomness. It starts by forming clusters of the most similar submissions and then forms bigger clusters from these small clusters in a hierarchical way. This will always produce the same clustering results.
2. No need to specify any hyperparameter. A threshold needs to be applied at the end of the process to form clusters. In our context, let's say we want all submissions which are more than 90% correlated to fall in the same cluster, then we put the threshold of 'correlation distance' as (1 - 0.9). This is easy to explain and interpret.

\textbf{Example}:

\begin{itemize}
	\item Model1
    	\begin{itemize}
        	\item Total Stake: 1000
            \item Part of Cluster 1
            \item Performance metric (spearman correlation): 0.03
		\end{itemize}
    \item Model 2
    	\begin{itemize}
        	\item Total Stake: 800
            \item Part of Cluster 2
            \item Performance metric (spearman correlation): 0.02
		\end{itemize}
   	\item Model 3
    	\begin{itemize}
        	\item Total Stake: 500
            \item Part of Cluster 1
            \item Performance metric (spearman correlation): 0.03
		\end{itemize}
    \item Payout multipliers
    	\begin{itemize}
        	\item Model 1, Model3 : 0.5  (Since they belong to same cluster)
            \item Model 2: 1.0  (Unique cluster)
		\end{itemize}
    \item Payouts: (Stake * Performance * Multiplier)
    	\begin{itemize}
        	\item Model 1: 1000 * 0.03 * 0.5 = 15
            \item Model 2: 800 * 0.02 * 1.0 = 16
            \item Model 3: 500 * 0.03 * 0.05 = 7.5
		\end{itemize}
    \item Payout distribution to stakers (Model 2 example)
    	\begin{itemize}
        	\item Total payouts for Model 2 = 16
        	\item Num Supporters = 3 (say) 
            \item Num Heroes = 1 (always)
            \item Hero Stake = 50 ; Supporters stake: 250 * 3 = 750 (assuming each supporter stakes 250 each)
            \item Hero commission (irrespective of Hero stake) = 25\% (to be chosen by Hero)
            \item Commission going to Hero upfront = 16 * 0.25 = 4
            \item Remaining Payouts : 16 - 4 = 12
            \item 12 is distributed to all Supporters + Hero based on their stake 
            \item Hero gets : $\frac{50}{800}$ * 12
            \item Each supporter gets: $\frac{250}{800}$ * 12
            \item Hero commision is in addition to Hero stake payouts. Both are necesssary beacuse Hero commission will lead to competition among Heros to provide best service at lowest commission to attract supporters; and Stake payouts are necessary as they will indicate to the supporters that the Hero has skin in the game and is willing to lose money if performs badly
        \end{itemize}
\end{itemize}
Note: Spearman Correlation is a metric that can be used as a starting point. The performance metric will need to be evaluated periodically whether it benefits the Fund performance.

\emph{Query on discord: Are both Fineprints 2 and 3 needed?}

- Short Answer, Yes. 
- Fineprint 3 is needed to disincentivise modellers submitting similar predictions.
- Fineprint 2 is needed to avoid over allocation of capital in a few models. Say over the last month a model gives outsized returns with high originality, then supporters may unsuspectingly want to switch their stakes on this model (which might be highly volatile and detrimental for future rounds). This will unwantedly lead to over allocation in a single model. Hence, having a stake cap on models will be useful. The amount of stakecap can be reviewed from time to time.
 
Alpha provider scheme is more nuanced because:

1. Providers may not want to give away their new feature for everyone to use.
2. The feature might become less useful overtime due to alpha decay, and Crunch team will have to deal with the evaluation of such decayed features and remove it from the dataset. This will lead to more manual evaluation from the Crunch team side which is a bottleneck for improvement.

Having said that, it can be taken up as 2 step process:

1. Evaluation of utility by the provider. Crunch team provides an api which can be used by providers to upload their feature (with stock tickers), the api returns the correlation of the queried feature with the existing features in the DataCrunch dataset. (not the correlation with target). This will let the providers know if their feature is unique or not.
2. Say a provider develops a new feature which is unique wrt all other features in the dataset. Then, the provider can request a custom dataset (obfuscated like existing datasets) which includes that new feature. The provider is then free to use the new feature however they like to make predictions as usual for the tournament. For requesting a custom dataset, a small amount of Crunch can be locked (not staked) to avoid spamming.

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
