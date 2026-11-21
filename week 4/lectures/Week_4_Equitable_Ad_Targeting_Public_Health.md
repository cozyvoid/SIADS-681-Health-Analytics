# Module 4 (Week 4): Equitable Ad Targeting for Public Health — Allison Koenecke

## Lecture at a Glance

This lecture asks how online advertising can be designed to reduce rather than reproduce health inequality.

The case study focuses on recruiting applicants to **SNAP** through online ads, especially balancing outreach to English- and Spanish-speaking populations. The key challenge is a trade-off between **efficiency** and **equity**: maximizing the total number of conversions may under-serve groups that are more expensive to reach.

The proposed solution combines:

1. Experimental estimation of the outcomes produced by different advertising strategies.
2. Human preference elicitation over those possible outcomes.

---

## Key Points

1. Online advertising can affect access to public-benefit programs.
2. The lecture uses **SNAP enrollment** through GetCalFresh as a public-health case study.
3. Online ad delivery is shaped by auction systems and differences in the cost of reaching different groups.
4. Cost optimization can unintentionally create discriminatory outcomes.
5. Demographic-parity constraints can improve equity but may reduce total conversions.
6. The equity-efficiency trade-off can be visualized with a **Pareto frontier**.
7. The proposed method first estimates feasible advertising outcomes using an RCT, then asks people which outcomes they prefer using conjoint-style preference elicitation.
8. The broader research question is how to incorporate human values into algorithmic decision-making.

---

# 1. Public-Health Motivation

The lecture begins with the question:

> How can we inform online decision-making to reduce health inequality?

SNAP is presented not merely as an anti-poverty program but as an important health-related intervention for low-income Americans.

The lecture notes that millions of Americans receive SNAP benefits, and improving access can therefore have major public-health implications.

---

# 2. GetCalFresh and Online Advertising

GetCalFresh is used as an example of a service that helps people apply for food assistance.

Online search ads can raise awareness of the application service.

The lecture walks through the advertising funnel:

**Search → Impression → Click → Conversion**

## Impression

An **impression** occurs when an ad is shown to a user.

## Click

A **click** occurs when the user selects the ad and visits the website.

## Conversion

A **conversion** is the desired completed action—in this case, completing or submitting a SNAP application.

### Advertiser’s goal

The slides summarize the advertiser’s objective as:

- High conversions
- Low cost

---

# 3. How Online Ad Auctions Work

Google runs an advertising auction in which advertisers bid on search keywords.

Advertisers may use strategies such as:

- Machine learning to maximize conversions
- Setting a target cost per conversion

Advertisers can also target subsets of users by:

- Location
- Language preference
- Demographics
- Search interests

This creates opportunities for both efficient targeting and unequal outcomes.

---

# 4. How Discrimination Can Emerge

The lecture asks:

> What could go wrong?

The key mechanism is **crowding out**.

If one demographic group is more expensive to reach in an ad auction, an algorithm optimized for cost-effective conversions may preferentially show ads to cheaper groups.

### Example from prior research

The lecture cites work showing that fewer women saw a STEM career ad because younger women were more expensive to advertise to.

The problem did not require an explicit rule saying “show fewer ads to women.” It emerged from the economics of the optimization system.

### Main idea

A cost-minimizing or conversion-maximizing system can produce discriminatory delivery even without directly using a discriminatory objective.

---

# 5. Efficiency vs. Demographic Parity

The lecture presents a trade-off under a fixed advertising budget.

## No demographic-parity constraint

Potential result:

- More total conversions
- Unequal distribution across groups

## Demographic-parity constraint

Potential result:

- More equitable distribution
- Fewer total conversions
- More conversions among the underrepresented group

This creates a normative question:

> How much efficiency should be sacrificed for equity?

---

# 6. Spanish-Speaking SNAP Applicants: Case Study

The case study focuses on San Diego.

Among people living below the poverty line:

- About **23% primarily speak Spanish**

But in the current GetCalFresh applicant pool:

- About **10% are Spanish speakers**

The lecture also notes that advertising to Spanish speakers can be **up to four times more expensive** than advertising to English speakers.

### The fairness question

Should the system:

- Maximize total applicants?
- Match the population share of Spanish speakers?
- Choose some point between the two?

The lecture explicitly asks whether 10% is “fair” and whether 23% should necessarily be the target.

---

# 7. The Pareto Frontier

The figure on **pages 32–34** plots a trade-off between:

- Total conversions
- Percentage of conversions allocated to Spanish speakers

As more conversions are allocated to Spanish-speaking users, total conversions fall.

This curve is the **Pareto frontier**.

## Definition

A Pareto frontier contains outcomes where improving one objective requires worsening another.

In this case:

- More equity can reduce total conversion count.
- More total conversions can reduce representation of Spanish-speaking applicants.

There is no single objectively best point without specifying how the two goals should be valued.

---

# 8. Proposed Two-Step Method

The lecture proposes two stages.

## Step 1 — Estimate outcomes from different advertising strategies

Use a randomized controlled trial (RCT) to estimate what happens under different advertising strategies.

Goal:

- Generate a feasible set of outcomes
- Estimate the relationship between equity and conversion efficiency

This produces the empirical Pareto frontier.

## Step 2 — Understand human preferences over outcomes

Use **conjoint analysis / preference elicitation** to learn how people value different trade-offs.

Instead of imposing a fairness constraint arbitrarily, the method asks how people compare realistic alternatives.

---

# 9. Preference Elicitation

The slide on **page 35** gives an example choice:

### Option A

- 36 applicants
- 13% Spanish

### Option B

- 34 applicants
- 18% Spanish

Participants are asked which outcome they prefer.

This forces a real trade-off:

- More total applicants
- More equitable representation

---

# 10. Ranking Preferences

The lecture describes:

- A Qualtrics survey
- Pairwise preference elicitation
- A partisan sample
- A **Bradley–Terry model**

## Bradley–Terry model

The Bradley–Terry model is used to estimate relative preferences from pairwise comparisons.

The slides describe it as learning a utility model with **logistic regression** over pairs of choices.

The result is a ranking of preferred outcomes.

The study also compares conjoint-based preference estimates with simpler binary yes/no preference questions.

---

# 11. Equity vs. Efficiency Preferences

The lecture compares two reference points on the Pareto frontier:

- **Maximize conversions**
- **Demographic parity**

The survey results indicate support for giving up some efficiency in exchange for more equitable allocation.

The exact preferred point does not necessarily equal either extreme.

### Important interpretation

The preferred policy may be:

- More equitable than pure conversion maximization
- Less constrained than strict demographic parity

This is precisely why the lecture argues for empirically studying human preferences rather than assuming a single fairness objective.

---

# 12. Extending the Framework

The lecture proposes extending the method to:

## Other geographic locations

The slope of the Pareto frontier may change because ad costs and population composition differ.

## Other fairness dimensions

Examples include:

- Income level
- Age
- Gender
- Race proxy

## Other public-health recruitment settings

Examples include:

- Public-assistance programs
- Clinical trials

The basic structure remains the same:

1. Estimate feasible outcomes.
2. Elicit human preferences over those outcomes.

---

# Important Definitions

| Term | Meaning |
|---|---|
| **Impression** | An instance in which an ad is shown to a user. |
| **Click** | A user selects the advertisement. |
| **Conversion** | The desired completed action after viewing/clicking the ad. |
| **Target cost per conversion** | A bidding objective designed to obtain conversions around a specified average cost. |
| **Demographic parity** | A fairness criterion seeking equal or proportional outcomes across demographic groups. |
| **Crowding out** | A market/optimization effect in which one group receives fewer opportunities because reaching that group is more expensive. |
| **Pareto frontier** | Set of non-dominated outcomes where improving one objective requires worsening another. |
| **RCT** | Randomized controlled trial; experimental design used to estimate causal effects of interventions. |
| **Conjoint analysis** | Method for learning preferences by asking people to choose among options with different combinations of attributes. |
| **Bradley–Terry model** | Statistical model for estimating rankings or utilities from pairwise comparisons. |
| **Utility model** | A model representing how strongly different outcomes are preferred. |

---

# Example of the Core Trade-Off

Suppose two possible ad strategies are available under the same budget.

### Strategy A

- 40 total conversions
- 10% Spanish-speaking applicants

### Strategy B

- 30 total conversions
- 23% Spanish-speaking applicants

Strategy A is more efficient.

Strategy B is more equitable under a proportional-representation definition.

Neither is automatically “correct.” Choosing between them requires a value judgment about the importance of conversion efficiency versus representation.

The lecture’s contribution is to make that value judgment explicit and measurable.

---

# Main Argument / Conclusion

The lecture argues that fairness in algorithmic decision-making should not be treated as a purely technical constraint chosen by engineers.

Online ad systems can create inequitable public-health outcomes because ad auctions and optimization objectives make some groups more expensive to reach. Simply maximizing conversions may therefore reproduce unequal access.

The proposed framework combines:

**Empirical outcome estimation + human preference elicitation**

to identify advertising strategies that reflect both what is technically feasible and what people consider an acceptable equity-efficiency trade-off.

---

# Quick Review

- Public-health advertising can influence access to services such as SNAP.
- Ad systems optimize impressions, clicks, conversions, and cost.
- Auction prices differ across demographic groups.
- Cost optimization can create discriminatory delivery.
- Demographic parity can improve equity but reduce total conversions.
- The Pareto frontier describes the efficiency-equity trade-off.
- RCTs estimate feasible outcomes.
- Conjoint analysis and Bradley–Terry models estimate human preferences.
- The lecture argues for incorporating human values into algorithmic optimization.
