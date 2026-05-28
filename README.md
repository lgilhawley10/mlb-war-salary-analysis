# MLB WAR vs Salary Analysis — 2025

Analyzing the relationship between MLB player salaries and Wins Above Replacement (WAR) to identify the most overpaid and underpaid players in the 2025 season.

## Overview

This project merges two datasets — player WAR statistics and contract salary data — to calculate the value each player provides relative to what they are paid. 
Using WAR per dollar as the key metric, I identify which players represent the best and worst value in baseball.

## Key Findings

- **Most underpaid:** Geraldo Perdomo (ARI) produced 7.1 WAR on a $2.55M salary — the best value in baseball
- **Rookie contracts dominate value:** Players like Gunnar Henderson, Paul Skenes & Hunter Brown produce elite WAR at near-minimum salaries
- **Biggest overpay:** Chad Green earned $10.5M while producing -0.9 WAR in 2025
- **Deserved Massive Contracts:** Players such as Ohtani and Judge produce at an incredibly high level, justifying their large contracts.

## Visualizations

- Scatter plot: Average Annual Salary vs Total WAR (802 players)
- Top 10 most underpaid players (min. $1M salary)
- Top 10 most overpaid players (min. $10M salary)

## Tools & Methods

- Python, pandas, matplotlib
- Data cleaning: name reformatting, salary string parsing
- Datasets merged on player name across Baseball Reference and Spotrac

## Data Sources

- WAR: Baseball Reference (2025)
- Salaries: Spotrac (2025)
