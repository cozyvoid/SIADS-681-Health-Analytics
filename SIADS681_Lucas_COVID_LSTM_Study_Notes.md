# County-Level COVID-19 Forecasting with COVID-LSTM

*Benjamin Lucas, Behzad Vahedi, and Morteza Karimzadeh (2023), International Journal of Data Science and Analytics, 15, pp. 247–266. Published online in 2022.* [Article DOI](https://doi.org/10.1007/s41060-021-00295-9)

## Key points

- **Research question.** Can a model that learns from recent case counts and connections between places improve forecasts of weekly reported COVID-19 cases in counties across the contiguous United States?
- **Approach.** COVID-LSTM combines county case histories, Facebook-derived mobility and social connectedness features, and temperature in a long short-term memory model.
- **Main result.** Across a 17-week evaluation, the COVID-LSTM had lower average error than the COVIDhub-ensemble at **2, 3, and 4 weeks ahead**. The COVIDhub-ensemble had lower error at **1 week ahead**.
- **Main argument.** Data-driven forecasts can support local planning. The authors argue for using them alongside compartmental models, which help characterize transmission and other epidemiological processes.

## 1. Forecasting target and inputs

**Incidence** means new cases over a defined period. Here the target is the weekly count of newly reported confirmed cases in a county. **Spatiotemporal forecasting** uses information across places and over time. The model uses 10 features per time step and a 10-week input sequence consisting of the current week and nine lagged weeks.

| Input source | What it contributes |
|---|---|
| **Johns Hopkins CSSE case reports** | Recent weekly incidence and a feature based on cumulative reported cases. The authors used a seven-day rolling average in preprocessing to smooth reporting fluctuations. |
| **Facebook Movement Range** | A stay-put measure and a measure of movement relative to a reference period, plus the week-to-week changes in both measures. |
| **Facebook Social Connectedness Index (SCI)** | A measure of the strength of Facebook friendship ties between counties, adjusted for their Facebook user counts. The authors weight other counties’ cases by those ties to estimate **social proximity to cases**, and use weekly change and monthly mean features. |
| **Weather** | Average minimum and maximum temperatures. |

**Example.** A county may be strongly linked to a county with rising case counts through social ties. The connected county’s cases receive more weight in the social proximity feature, even if the counties do not share a border. The feature measures a proxy for possible exposure.

## 2. Model design and evaluation

- **LSTM (long short-term memory)** is a recurrent neural network that uses gates to retain, discard, and pass along information in a sequence. Each network in the study used two LSTM layers followed by a dense layer.
- **Ensemble** means combining predictions from multiple models. COVID-LSTM uses the median prediction from 10 separately trained networks with the same architecture. The COVIDhub-ensemble combines forecasts from multiple forecasting teams. The Forecast Hub’s **persistence baseline** projects the most recently observed weekly case count forward.
- The authors evaluated forecasts over **October 31, 2020, to February 20, 2021**, covering a rise, peak, and decline in national case counts. Forecasts were evaluated on held-out observations, with the primary evaluation using raw reported counts.
- **SEIR** is a compartmental model that describes how people move among susceptible, exposed, infectious, and recovered states. COVID-LSTM learns predictive patterns directly from observed inputs. The two approaches answer complementary forecasting and epidemiological questions.

## 3. Results by forecast horizon

**Mean absolute error (MAE)** is the average absolute difference between forecast and observed counts. Lower values indicate smaller errors. Table 2 reports average weekly MAE in cases per county.

| Forecast horizon | COVID-LSTM MAE | COVIDhub-ensemble MAE | Lower-error model and difference |
|---|---:|---:|---|
| 1 week | 87.29 | 78.77 | COVIDhub-ensemble by 8.52 cases |
| 2 weeks | 110.97 | 121.87 | COVID-LSTM by 10.90 cases |
| 3 weeks | 121.46 | 155.40 | COVID-LSTM by 33.94 cases |
| 4 weeks | 133.22 | 183.32 | COVID-LSTM by 50.10 cases |

- **Mean absolute percentage error (MAPE)** expresses each absolute error as a percentage of the actual count. Actual counts of zero make it undefined. The authors reported MAPE for the 50 most populous counties and found the same ranking between the two models at each horizon.
- A hybrid version added static county characteristics, including population density and demographic variables. Its average one-week MAE was **88.05**, compared with **87.29** for the original COVID-LSTM.

## 4. Forecast uncertainty and limitations

- **Quantile regression** estimates selected percentiles of the future outcome. The 2.5th and 97.5th percentiles form a nominal **95% prediction interval** for a future weekly case count. Figure 5 illustrates one-week intervals for six counties.
- Delayed reporting can make case counts look unusually low during a holiday and unusually high afterward. For example, Los Angeles County’s reported count fell by about 40% in the week starting January 16 compared with the prior week. The authors suggest that a holiday backlog may have inflated the prior week’s count.
- Facebook users may represent some populations better than others. County-level scores establish performance at the county scale for this study period. Subgroup performance and transfer to other places, pandemic phases, or diseases would require separate evaluation.
- The model benefits from an extensive case history. Sparse surveillance, changing reporting practices, and changes in vaccination or population behavior can affect how well historical patterns predict future counts.

## Conclusion

For the counties and weeks studied, COVID-LSTM reduced average forecast error at longer horizons, with the largest gain at four weeks. The authors propose combining data-driven forecasting with compartmental modeling to improve forecasts while preserving the ability to characterize how an outbreak evolves.

*Reading map: Data and model, §§3–4. Results and uncertainty, §5 and Tables 2–6. Limitations and future directions, §§6–7.*
