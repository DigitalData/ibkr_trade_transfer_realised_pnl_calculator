# IBKR Trade/Transfer Realised Profit/Loss Calculator

Suppose an internal transfer of trades between two accounts. 
In a hypothetical accounting scenario, this can be considered a sale between two private parties, provided that the account ownership is different.
**This script aims to determine the Realised Profit/Loss of closed trades relative to a given transfer price.**

## The Mathematics

Ultimately, we're trying to calculate a Post-Transfer Realised P/L:

$$
 \text{Post-Transfer Realised P/L} = \text{Realised P/L} + \text{Value at Purchase} - \text{Value at Transfer}
$$

- For IBKR, $\text{Value at Purchase} = \text{Cost Basis}$ for a given lot. 
- Also, $\text{Value at Transfer} = \text{Lot Quantity} \times \text{Transfer Price}$.

A *lot* is a quantity of trades purchased at the same timestamp for the same trade price.

**Note:** Transferred lots will not necessarily match closed lots in quantities. 
This means that the *value* of the transferred lots cannot be used in the above equation. 
Instead, joining on lot dates and prices will allow for a closed lot to determine what price it was transferred at (as part of a transferred lot).
Unfortunately, if part of a closed lot is transferred at one price, and another is transferred at a different price, then this method becomes unreliable and a new formula will need to be developed.

This modifies some of the terms of the above equations.

$$
\begin{aligned}
\text{Post-Transfer Realised P/L} &= \text{Realised P/L} + \text{Value at Purchase} - \text{Value at Transfer} \\
\implies \text{Post-Transfer Realised P/L} &= \text{Realised P/L} + \text{Cost Basis} - \text{Transfer Price} \times \text{Quantity Sold}
\end{aligned}
$$

## The Technology

Made with Pandas and Jupyter Notebooks.
