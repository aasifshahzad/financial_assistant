from dotenv import load_dotenv, find_dotenv
import os
import requests
import json

load_dotenv("E:/Python/.env")
fmp_key = os.environ.get("FMP_API_KEY")

tools = [
        {"type": "code_interpreter"},
        {"type": "retrieval"},
        {
            "type": "function",
            "function": {"name": "get_income_statement",
            "parameters": {"type": "object",
            "properties": {
            "ticker": {"type": "string"},
            "period": {"type": "string"},
            "limit": {"type": "integer"
            }}}}},
        {
            "type": "function",
            "function": {
                "name": "get_balance_sheet_MSFT",
                "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {"type": "string"},
                    "period": {"type": "string"},
                    "limit": {"type": "integer"}
                }}}},
        {
            "type": "function",
            "function": {
                "name": "get_balance_sheet_AAPL",
                "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {"type": "string"},
                    "period": {"type": "string"},
                    "limit": {"type": "integer"}
                }}}},
        {
            "type": "function",
            "function": {
                "name": "get_cash_flow_statement",
                "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {"type": "string"},
                    "period": {"type": "string"},
                    "limit": {"type": "integer"}
                }}}},
        {
            "type": "function",
            "function": {
                "name": "get_key_metrics",
                "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {"type": "string"},
                    "period": {"type": "string"}
                }}}},
        {
            "type": "function",
            "function": {
                "name": "get_financial_ratios",
                "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {"type": "string"},
                    "period": {"type": "string"}
                }}}},
        {
            "type": "function",
            "function": {
                "name": "get_financial_growth",
                "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {"type": "string"},
                    "period": {"type": "string"}
                }}}},
        ]

def get_balance_sheet_AAPL( period, limit=10,ticker = "AAPL"):
    """_summary_

    Args:
        period (_type_): _description_
        limit (int, optional): _description_. Defaults to 10.
        ticker (str, optional): _description_. Defaults to "AAPL".

    Returns:
        _type_: _description_
    """

    #url = f"https://financialmodelingprep.com/api/v3/balance_sheet/{ticker}?period={period}&limit={limit}&apikey={fmp_key}"
    # response = requests.get(url)
    response = [
                {
                    "date": "2023-09-30",
                    "symbol": "AAPL",
                    "reportedCurrency": "USD",
                    "cik": "0000320193",
                    "fillingDate": "2023-11-03",
                    "acceptedDate": "2023-11-02 18:08:27",
                    "calendarYear": "2023",
                    "period": "FY",
                    "cashAndCashEquivalents": 29965000000,
                    "shortTermInvestments": 31590000000,
                    "cashAndShortTermInvestments": 61555000000,
                    "netReceivables": 60985000000,
                    "inventory": 6331000000,
                    "otherCurrentAssets": 14695000000,
                    "totalCurrentAssets": 143566000000,
                    "propertyPlantEquipmentNet": 43715000000,
                    "goodwill": 0,
                    "intangibleAssets": 0,
                    "goodwillAndIntangibleAssets": 0,
                    "longTermInvestments": 100544000000,
                    "taxAssets": 0,
                    "otherNonCurrentAssets": 64758000000,
                    "totalNonCurrentAssets": 209017000000,
                    "otherAssets": 0,
                    "totalAssets": 352583000000,
                    "accountPayables": 62611000000,
                    "shortTermDebt": 15807000000,
                    "taxPayables": 0,
                    "deferredRevenue": 8061000000,
                    "otherCurrentLiabilities": 58829000000,
                    "totalCurrentLiabilities": 145308000000,
                    "longTermDebt": 95281000000,
                    "deferredRevenueNonCurrent": 0,
                    "deferredTaxLiabilitiesNonCurrent": 0,
                    "otherNonCurrentLiabilities": 49848000000,
                    "totalNonCurrentLiabilities": 145129000000,
                    "otherLiabilities": 0,
                    "capitalLeaseObligations": 0,
                    "totalLiabilities": 290437000000,
                    "preferredStock": 0,
                    "commonStock": 73812000000,
                    "retainedEarnings": -214000000,
                    "accumulatedOtherComprehensiveIncomeLoss": -11452000000,
                    "othertotalStockholdersEquity": 0,
                    "totalStockholdersEquity": 62146000000,
                    "totalEquity": 62146000000,
                    "totalLiabilitiesAndStockholdersEquity": 352583000000,
                    "minorityInterest": 0,
                    "totalLiabilitiesAndTotalEquity": 352583000000,
                    "totalInvestments": 31590000000,
                    "totalDebt": 111088000000,
                    "netDebt": 81123000000,
                    "link": "https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/0000320193-23-000106-index.htm",
                    "finalLink": "https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm"
                },
                {
                    "date": "2022-09-24",
                    "symbol": "AAPL",
                    "reportedCurrency": "USD",
                    "cik": "0000320193",
                    "fillingDate": "2022-10-28",
                    "acceptedDate": "2022-10-27 18:01:14",
                    "calendarYear": "2022",
                    "period": "FY",
                    "cashAndCashEquivalents": 23646000000,
                    "shortTermInvestments": 24658000000,
                    "cashAndShortTermInvestments": 48304000000,
                    "netReceivables": 60932000000,
                    "inventory": 4946000000,
                    "otherCurrentAssets": 21223000000,
                    "totalCurrentAssets": 135405000000,
                    "propertyPlantEquipmentNet": 42117000000,
                    "goodwill": 0,
                    "intangibleAssets": 0,
                    "goodwillAndIntangibleAssets": 0,
                    "longTermInvestments": 120805000000,
                    "taxAssets": 0,
                    "otherNonCurrentAssets": 54428000000,
                    "totalNonCurrentAssets": 217350000000,
                    "otherAssets": 0,
                    "totalAssets": 352755000000,
                    "accountPayables": 64115000000,
                    "shortTermDebt": 21110000000,
                    "taxPayables": 0,
                    "deferredRevenue": 7912000000,
                    "otherCurrentLiabilities": 60845000000,
                    "totalCurrentLiabilities": 153982000000,
                    "longTermDebt": 98959000000,
                    "deferredRevenueNonCurrent": 0,
                    "deferredTaxLiabilitiesNonCurrent": 0,
                    "otherNonCurrentLiabilities": 49142000000,
                    "totalNonCurrentLiabilities": 148101000000,
                    "otherLiabilities": 0,
                    "capitalLeaseObligations": 0,
                    "totalLiabilities": 302083000000,
                    "preferredStock": 0,
                    "commonStock": 64849000000,
                    "retainedEarnings": -3068000000,
                    "accumulatedOtherComprehensiveIncomeLoss": -11109000000,
                    "othertotalStockholdersEquity": 0,
                    "totalStockholdersEquity": 50672000000,
                    "totalEquity": 50672000000,
                    "totalLiabilitiesAndStockholdersEquity": 352755000000,
                    "minorityInterest": 0,
                    "totalLiabilitiesAndTotalEquity": 352755000000,
                    "totalInvestments": 145463000000,
                    "totalDebt": 120069000000,
                    "netDebt": 96423000000,
                    "link": "https://www.sec.gov/Archives/edgar/data/320193/000032019322000108/0000320193-22-000108-index.htm",
                    "finalLink": "https://www.sec.gov/Archives/edgar/data/320193/000032019322000108/aapl-20220924.htm"
                },
                {
                    "date": "2021-09-25",
                    "symbol": "AAPL",
                    "reportedCurrency": "USD",
                    "cik": "0000320193",
                    "fillingDate": "2021-10-29",
                    "acceptedDate": "2021-10-28 18:04:28",
                    "calendarYear": "2021",
                    "period": "FY",
                    "cashAndCashEquivalents": 34940000000,
                    "shortTermInvestments": 27699000000,
                    "cashAndShortTermInvestments": 62639000000,
                    "netReceivables": 51506000000,
                    "inventory": 6580000000,
                    "otherCurrentAssets": 14111000000,
                    "totalCurrentAssets": 134836000000,
                    "propertyPlantEquipmentNet": 39440000000,
                    "goodwill": 0,
                    "intangibleAssets": 0,
                    "goodwillAndIntangibleAssets": 0,
                    "longTermInvestments": 127877000000,
                    "taxAssets": 0,
                    "otherNonCurrentAssets": 48849000000,
                    "totalNonCurrentAssets": 216166000000,
                    "otherAssets": 0,
                    "totalAssets": 351002000000,
                    "accountPayables": 54763000000,
                    "shortTermDebt": 15613000000,
                    "taxPayables": 0,
                    "deferredRevenue": 7612000000,
                    "otherCurrentLiabilities": 47493000000,
                    "totalCurrentLiabilities": 125481000000,
                    "longTermDebt": 109106000000,
                    "deferredRevenueNonCurrent": 0,
                    "deferredTaxLiabilitiesNonCurrent": 0,
                    "otherNonCurrentLiabilities": 53325000000,
                    "totalNonCurrentLiabilities": 162431000000,
                    "otherLiabilities": 0,
                    "capitalLeaseObligations": 0,
                    "totalLiabilities": 287912000000,
                    "preferredStock": 0,
                    "commonStock": 57365000000,
                    "retainedEarnings": 5562000000,
                    "accumulatedOtherComprehensiveIncomeLoss": 163000000,
                    "othertotalStockholdersEquity": 0,
                    "totalStockholdersEquity": 63090000000,
                    "totalEquity": 63090000000,
                    "totalLiabilitiesAndStockholdersEquity": 351002000000,
                    "minorityInterest": 0,
                    "totalLiabilitiesAndTotalEquity": 351002000000,
                    "totalInvestments": 155576000000,
                    "totalDebt": 124719000000,
                    "netDebt": 89779000000,
                    "link": "https://www.sec.gov/Archives/edgar/data/320193/000032019321000105/0000320193-21-000105-index.htm",
                    "finalLink": "https://www.sec.gov/Archives/edgar/data/320193/000032019321000105/aapl-20210925.htm"
                },
                {
                    "date": "2020-09-26",
                    "symbol": "AAPL",
                    "reportedCurrency": "USD",
                    "cik": "0000320193",
                    "fillingDate": "2020-10-30",
                    "acceptedDate": "2020-10-29 18:06:25",
                    "calendarYear": "2020",
                    "period": "FY",
                    "cashAndCashEquivalents": 38016000000,
                    "shortTermInvestments": 52927000000,
                    "cashAndShortTermInvestments": 90943000000,
                    "netReceivables": 37445000000,
                    "inventory": 4061000000,
                    "otherCurrentAssets": 11264000000,
                    "totalCurrentAssets": 143713000000,
                    "propertyPlantEquipmentNet": 36766000000,
                    "goodwill": 0,
                    "intangibleAssets": 0,
                    "goodwillAndIntangibleAssets": 0,
                    "longTermInvestments": 100887000000,
                    "taxAssets": 0,
                    "otherNonCurrentAssets": 42522000000,
                    "totalNonCurrentAssets": 180175000000,
                    "otherAssets": 0,
                    "totalAssets": 323888000000,
                    "accountPayables": 42296000000,
                    "shortTermDebt": 13769000000,
                    "taxPayables": 0,
                    "deferredRevenue": 6643000000,
                    "otherCurrentLiabilities": 42684000000,
                    "totalCurrentLiabilities": 105392000000,
                    "longTermDebt": 98667000000,
                    "deferredRevenueNonCurrent": 0,
                    "deferredTaxLiabilitiesNonCurrent": 0,
                    "otherNonCurrentLiabilities": 54490000000,
                    "totalNonCurrentLiabilities": 153157000000,
                    "otherLiabilities": 0,
                    "capitalLeaseObligations": 0,
                    "totalLiabilities": 258549000000,
                    "preferredStock": 0,
                    "commonStock": 50779000000,
                    "retainedEarnings": 14966000000,
                    "accumulatedOtherComprehensiveIncomeLoss": -406000000,
                    "othertotalStockholdersEquity": 0,
                    "totalStockholdersEquity": 65339000000,
                    "totalEquity": 65339000000,
                    "totalLiabilitiesAndStockholdersEquity": 323888000000,
                    "minorityInterest": 0,
                    "totalLiabilitiesAndTotalEquity": 323888000000,
                    "totalInvestments": 153814000000,
                    "totalDebt": 112436000000,
                    "netDebt": 74420000000,
                    "link": "https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/0000320193-20-000096-index.htm",
                    "finalLink": "https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm"
                },
                {
                    "date": "2019-09-28",
                    "symbol": "AAPL",
                    "reportedCurrency": "USD",
                    "cik": "0000320193",
                    "fillingDate": "2019-10-31",
                    "acceptedDate": "2019-10-30 18:12:36",
                    "calendarYear": "2019",
                    "period": "FY",
                    "cashAndCashEquivalents": 48844000000,
                    "shortTermInvestments": 51713000000,
                    "cashAndShortTermInvestments": 100557000000,
                    "netReceivables": 45804000000,
                    "inventory": 4106000000,
                    "otherCurrentAssets": 12352000000,
                    "totalCurrentAssets": 162819000000,
                    "propertyPlantEquipmentNet": 37378000000,
                    "goodwill": 0,
                    "intangibleAssets": 0,
                    "goodwillAndIntangibleAssets": 0,
                    "longTermInvestments": 105341000000,
                    "taxAssets": 0,
                    "otherNonCurrentAssets": 32978000000,
                    "totalNonCurrentAssets": 175697000000,
                    "otherAssets": 0,
                    "totalAssets": 338516000000,
                    "accountPayables": 46236000000,
                    "shortTermDebt": 16240000000,
                    "taxPayables": 0,
                    "deferredRevenue": 5522000000,
                    "otherCurrentLiabilities": 37720000000,
                    "totalCurrentLiabilities": 105718000000,
                    "longTermDebt": 91807000000,
                    "deferredRevenueNonCurrent": 0,
                    "deferredTaxLiabilitiesNonCurrent": 0,
                    "otherNonCurrentLiabilities": 50503000000,
                    "totalNonCurrentLiabilities": 142310000000,
                    "otherLiabilities": 0,
                    "capitalLeaseObligations": 0,
                    "totalLiabilities": 248028000000,
                    "preferredStock": 0,
                    "commonStock": 45174000000,
                    "retainedEarnings": 45898000000,
                    "accumulatedOtherComprehensiveIncomeLoss": -584000000,
                    "othertotalStockholdersEquity": 0,
                    "totalStockholdersEquity": 90488000000,
                    "totalEquity": 90488000000,
                    "totalLiabilitiesAndStockholdersEquity": 338516000000,
                    "minorityInterest": 0,
                    "totalLiabilitiesAndTotalEquity": 338516000000,
                    "totalInvestments": 157054000000,
                    "totalDebt": 108047000000,
                    "netDebt": 59203000000,
                    "link": "https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/0000320193-19-000119-index.htm",
                    "finalLink": "https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/a10-k20199282019.htm"
                }
    ]
    #print(url)
    return json.dumps(response)

def get_balance_sheet_MSFT( period, limit=10,ticker = "MSFT"):
    """_summary_

    Args:
        period (_type_): _description_
        limit (int, optional): _description_. Defaults to 10.
        ticker (str, optional): _description_. Defaults to "MSFT".

    Returns:
        _type_: _description_
    """

    #url = f"https://financialmodelingprep.com/api/v3/balance_sheet/{ticker}?period={period}&limit={limit}&apikey={fmp_key}"
    # response = requests.get(url)
    response = [
                {
                    "date": "2023-06-30",
                    "symbol": "MSFT",
                    "reportedCurrency": "USD",
                    "cik": "0000789019",
                    "fillingDate": "2023-07-27",
                    "acceptedDate": "2023-07-27 16:01:56",
                    "calendarYear": "2023",
                    "period": "FY",
                    "cashAndCashEquivalents": 34704000000,
                    "shortTermInvestments": 76558000000,
                    "cashAndShortTermInvestments": 111262000000,
                    "netReceivables": 48688000000,
                    "inventory": 2500000000,
                    "otherCurrentAssets": 21807000000,
                    "totalCurrentAssets": 184257000000,
                    "propertyPlantEquipmentNet": 109987000000,
                    "goodwill": 67886000000,
                    "intangibleAssets": 9366000000,
                    "goodwillAndIntangibleAssets": 77252000000,
                    "longTermInvestments": 9879000000,
                    "taxAssets": 0,
                    "otherNonCurrentAssets": 30601000000,
                    "totalNonCurrentAssets": 227719000000,
                    "otherAssets": 0,
                    "totalAssets": 411976000000,
                    "accountPayables": 18095000000,
                    "shortTermDebt": 5247000000,
                    "taxPayables": 4152000000,
                    "deferredRevenue": 50901000000,
                    "otherCurrentLiabilities": 29906000000,
                    "totalCurrentLiabilities": 104149000000,
                    "longTermDebt": 54718000000,
                    "deferredRevenueNonCurrent": 2912000000,
                    "deferredTaxLiabilitiesNonCurrent": 433000000,
                    "otherNonCurrentLiabilities": 43541000000,
                    "totalNonCurrentLiabilities": 101604000000,
                    "otherLiabilities": 0,
                    "capitalLeaseObligations": 12728000000,
                    "totalLiabilities": 205753000000,
                    "preferredStock": 0,
                    "commonStock": 93718000000,
                    "retainedEarnings": 118848000000,
                    "accumulatedOtherComprehensiveIncomeLoss": -6343000000,
                    "othertotalStockholdersEquity": 0,
                    "totalStockholdersEquity": 206223000000,
                    "totalEquity": 206223000000,
                    "totalLiabilitiesAndStockholdersEquity": 411976000000,
                    "minorityInterest": 0,
                    "totalLiabilitiesAndTotalEquity": 411976000000,
                    "totalInvestments": 86437000000,
                    "totalDebt": 59965000000,
                    "netDebt": 25261000000,
                    "link": "https://www.sec.gov/Archives/edgar/data/789019/000095017023035122/0000950170-23-035122-index.htm",
                    "finalLink": "https://www.sec.gov/Archives/edgar/data/789019/000095017023035122/msft-20230630.htm"
                },
                {
                    "date": "2022-06-30",
                    "symbol": "MSFT",
                    "reportedCurrency": "USD",
                    "cik": "0000789019",
                    "fillingDate": "2022-07-28",
                    "acceptedDate": "2022-07-28 16:06:19",
                    "calendarYear": "2022",
                    "period": "FY",
                    "cashAndCashEquivalents": 13931000000,
                    "shortTermInvestments": 90826000000,
                    "cashAndShortTermInvestments": 104757000000,
                    "netReceivables": 44261000000,
                    "inventory": 3742000000,
                    "otherCurrentAssets": 16924000000,
                    "totalCurrentAssets": 169684000000,
                    "propertyPlantEquipmentNet": 87546000000,
                    "goodwill": 67524000000,
                    "intangibleAssets": 11298000000,
                    "goodwillAndIntangibleAssets": 78822000000,
                    "longTermInvestments": 6891000000,
                    "taxAssets": 0,
                    "otherNonCurrentAssets": 21897000000,
                    "totalNonCurrentAssets": 195156000000,
                    "otherAssets": 0,
                    "totalAssets": 364840000000,
                    "accountPayables": 19000000000,
                    "shortTermDebt": 2749000000,
                    "taxPayables": 4067000000,
                    "deferredRevenue": 45538000000,
                    "otherCurrentLiabilities": 27795000000,
                    "totalCurrentLiabilities": 95082000000,
                    "longTermDebt": 58521000000,
                    "deferredRevenueNonCurrent": 2870000000,
                    "deferredTaxLiabilitiesNonCurrent": 230000000,
                    "otherNonCurrentLiabilities": 41595000000,
                    "totalNonCurrentLiabilities": 103216000000,
                    "otherLiabilities": 0,
                    "capitalLeaseObligations": 11489000000,
                    "totalLiabilities": 198298000000,
                    "preferredStock": 0,
                    "commonStock": 86939000000,
                    "retainedEarnings": 84281000000,
                    "accumulatedOtherComprehensiveIncomeLoss": -4678000000,
                    "othertotalStockholdersEquity": 0,
                    "totalStockholdersEquity": 166542000000,
                    "totalEquity": 166542000000,
                    "totalLiabilitiesAndStockholdersEquity": 364840000000,
                    "minorityInterest": 0,
                    "totalLiabilitiesAndTotalEquity": 364840000000,
                    "totalInvestments": 97709000000,
                    "totalDebt": 61270000000,
                    "netDebt": 47339000000,
                    "link": "https://www.sec.gov/Archives/edgar/data/789019/000156459022026876/0001564590-22-026876-index.htm",
                    "finalLink": "https://www.sec.gov/Archives/edgar/data/789019/000156459022026876/msft-10k_20220630.htm"
                },
                {
                    "date": "2021-06-30",
                    "symbol": "MSFT",
                    "reportedCurrency": "USD",
                    "cik": "0000789019",
                    "fillingDate": "2021-07-29",
                    "acceptedDate": "2021-07-29 16:21:55",
                    "calendarYear": "2021",
                    "period": "FY",
                    "cashAndCashEquivalents": 14224000000,
                    "shortTermInvestments": 116110000000,
                    "cashAndShortTermInvestments": 130334000000,
                    "netReceivables": 38043000000,
                    "inventory": 2636000000,
                    "otherCurrentAssets": 13393000000,
                    "totalCurrentAssets": 184406000000,
                    "propertyPlantEquipmentNet": 70803000000,
                    "goodwill": 49711000000,
                    "intangibleAssets": 7800000000,
                    "goodwillAndIntangibleAssets": 57511000000,
                    "longTermInvestments": 5984000000,
                    "taxAssets": 0,
                    "otherNonCurrentAssets": 15075000000,
                    "totalNonCurrentAssets": 149373000000,
                    "otherAssets": 0,
                    "totalAssets": 333779000000,
                    "accountPayables": 15163000000,
                    "shortTermDebt": 8072000000,
                    "taxPayables": 2174000000,
                    "deferredRevenue": 41525000000,
                    "otherCurrentLiabilities": 23897000000,
                    "totalCurrentLiabilities": 88657000000,
                    "longTermDebt": 59703000000,
                    "deferredRevenueNonCurrent": 2616000000,
                    "deferredTaxLiabilitiesNonCurrent": 198000000,
                    "otherNonCurrentLiabilities": 40617000000,
                    "totalNonCurrentLiabilities": 103134000000,
                    "otherLiabilities": 0,
                    "capitalLeaseObligations": 9629000000,
                    "totalLiabilities": 191791000000,
                    "preferredStock": 0,
                    "commonStock": 83111000000,
                    "retainedEarnings": 57055000000,
                    "accumulatedOtherComprehensiveIncomeLoss": 1822000000,
                    "othertotalStockholdersEquity": 0,
                    "totalStockholdersEquity": 141988000000,
                    "totalEquity": 141988000000,
                    "totalLiabilitiesAndStockholdersEquity": 333779000000,
                    "minorityInterest": 0,
                    "totalLiabilitiesAndTotalEquity": 333779000000,
                    "totalInvestments": 122094000000,
                    "totalDebt": 67775000000,
                    "netDebt": 53551000000,
                    "link": "https://www.sec.gov/Archives/edgar/data/789019/000156459021039151/0001564590-21-039151-index.htm",
                    "finalLink": "https://www.sec.gov/Archives/edgar/data/789019/000156459021039151/msft-10k_20210630.htm"
                },
                {
                    "date": "2020-06-30",
                    "symbol": "MSFT",
                    "reportedCurrency": "USD",
                    "cik": "0000789019",
                    "fillingDate": "2020-07-30",
                    "acceptedDate": "2020-07-30 20:44:46",
                    "calendarYear": "2020",
                    "period": "FY",
                    "cashAndCashEquivalents": 13576000000,
                    "shortTermInvestments": 122951000000,
                    "cashAndShortTermInvestments": 136527000000,
                    "netReceivables": 32011000000,
                    "inventory": 1895000000,
                    "otherCurrentAssets": 11482000000,
                    "totalCurrentAssets": 181915000000,
                    "propertyPlantEquipmentNet": 52904000000,
                    "goodwill": 43351000000,
                    "intangibleAssets": 7038000000,
                    "goodwillAndIntangibleAssets": 50389000000,
                    "longTermInvestments": 2965000000,
                    "taxAssets": 0,
                    "otherNonCurrentAssets": 13138000000,
                    "totalNonCurrentAssets": 119396000000,
                    "otherAssets": 0,
                    "totalAssets": 301311000000,
                    "accountPayables": 12530000000,
                    "shortTermDebt": 3749000000,
                    "taxPayables": 2130000000,
                    "deferredRevenue": 36000000000,
                    "otherCurrentLiabilities": 20031000000,
                    "totalCurrentLiabilities": 72310000000,
                    "longTermDebt": 67249000000,
                    "deferredRevenueNonCurrent": 3180000000,
                    "deferredTaxLiabilitiesNonCurrent": 204000000,
                    "otherNonCurrentLiabilities": 40064000000,
                    "totalNonCurrentLiabilities": 110697000000,
                    "otherLiabilities": 0,
                    "capitalLeaseObligations": 7671000000,
                    "totalLiabilities": 183007000000,
                    "preferredStock": 0,
                    "commonStock": 80552000000,
                    "retainedEarnings": 34566000000,
                    "accumulatedOtherComprehensiveIncomeLoss": 3186000000,
                    "othertotalStockholdersEquity": 0,
                    "totalStockholdersEquity": 118304000000,
                    "totalEquity": 118304000000,
                    "totalLiabilitiesAndStockholdersEquity": 301311000000,
                    "minorityInterest": 0,
                    "totalLiabilitiesAndTotalEquity": 301311000000,
                    "totalInvestments": 125916000000,
                    "totalDebt": 70998000000,
                    "netDebt": 57422000000,
                    "link": "https://www.sec.gov/Archives/edgar/data/789019/000156459020034944/0001564590-20-034944-index.htm",
                    "finalLink": "https://www.sec.gov/Archives/edgar/data/789019/000156459020034944/msft-10k_20200630.htm"
                },
                {
                    "date": "2019-06-30",
                    "symbol": "MSFT",
                    "reportedCurrency": "USD",
                    "cik": "0000789019",
                    "fillingDate": "2019-08-01",
                    "acceptedDate": "2019-08-01 16:09:55",
                    "calendarYear": "2019",
                    "period": "FY",
                    "cashAndCashEquivalents": 11356000000,
                    "shortTermInvestments": 122463000000,
                    "cashAndShortTermInvestments": 133819000000,
                    "netReceivables": 29524000000,
                    "inventory": 2063000000,
                    "otherCurrentAssets": 10146000000,
                    "totalCurrentAssets": 175552000000,
                    "propertyPlantEquipmentNet": 43856000000,
                    "goodwill": 42026000000,
                    "intangibleAssets": 7750000000,
                    "goodwillAndIntangibleAssets": 49776000000,
                    "longTermInvestments": 2649000000,
                    "taxAssets": 0,
                    "otherNonCurrentAssets": 14723000000,
                    "totalNonCurrentAssets": 111004000000,
                    "otherAssets": 0,
                    "totalAssets": 286556000000,
                    "accountPayables": 9382000000,
                    "shortTermDebt": 5516000000,
                    "taxPayables": 5665000000,
                    "deferredRevenue": 32676000000,
                    "otherCurrentLiabilities": 21846000000,
                    "totalCurrentLiabilities": 69420000000,
                    "longTermDebt": 72850000000,
                    "deferredRevenueNonCurrent": 4530000000,
                    "deferredTaxLiabilitiesNonCurrent": 233000000,
                    "otherNonCurrentLiabilities": 37193000000,
                    "totalNonCurrentLiabilities": 114806000000,
                    "otherLiabilities": 0,
                    "capitalLeaseObligations": 6188000000,
                    "totalLiabilities": 184226000000,
                    "preferredStock": 0,
                    "commonStock": 78520000000,
                    "retainedEarnings": 24150000000,
                    "accumulatedOtherComprehensiveIncomeLoss": -340000000,
                    "othertotalStockholdersEquity": 0,
                    "totalStockholdersEquity": 102330000000,
                    "totalEquity": 102330000000,
                    "totalLiabilitiesAndStockholdersEquity": 286556000000,
                    "minorityInterest": 0,
                    "totalLiabilitiesAndTotalEquity": 286556000000,
                    "totalInvestments": 125112000000,
                    "totalDebt": 78366000000,
                    "netDebt": 67010000000,
                    "link": "https://www.sec.gov/Archives/edgar/data/789019/000156459019027952/0001564590-19-027952-index.htm",
                    "finalLink": "https://www.sec.gov/Archives/edgar/data/789019/000156459019027952/msft-10k_20190630.htm"
                }
                ]
    return json.dumps(response)

def get_cash_flow_statement(ticker, period = "annual", limit = 10):
    """
    Retrieve cash flow statement data for a specific ticker.

    :param ticker: Ticker symbol for the company.
    :param period: Period of the cash flow statement.
    :param limit: Limit of data to retrieve (default: 10).
    :return: JSON formatted data of the cash flow statement.
    """
    url = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?period={period}&limit={limit}&apikey={fmp_key}"
    response = requests.get(url)
    #print(url)
    return json.dumps(response.json())

def get_key_metrics(ticker, period = "annual"):
    """
    Retrieve key metrics data for a specific ticker.

    :param ticker: Ticker symbol for the company.
    :param period: Period of the key metrics.
    :return: JSON formatted data of the key metrics.
    """
    url = f"https://financialmodelingprep.com/api/v3/key-metrics/{ticker}?period={period}&apikey={fmp_key}"
    response = requests.get(url)
    #print(url)
    return json.dumps(response.json())

def get_financial_ratios(ticker, period = "annual"):
    """
    Retrieve financial ratios data for a specific ticker.

    :param ticker: Ticker symbol for the company.
    :param period: Period of the financial ratios.
    :return: JSON formatted data of the financial ratios.
    """
    url = f"https://financialmodelingprep.com/api/v3/ratios/{ticker}?period={period}&apikey={fmp_key}"
    #print(url)
    response = requests.get(url)
    return json.dumps(response.json())

def get_financial_growth(ticker, period = "annual"):
    """
    Retrieve financial growth data for a specific ticker.

    :param ticker: Ticker symbol for the company.
    :param period: Period of the financial growth.
    :return: JSON formatted data of the financial growth.
    """
    url = f"https://financialmodelingprep.com/api/v3/financial-growth/{ticker}?period={period}&apikey={fmp_key}"
    response = requests.get(url)
    #print(url)
    return json.dumps(response.json())

def get_income_statement(ticker, period = "annual", limit = 10):
    """
    Retrieve income statement data for a specific ticker.

    :param ticker: Ticker symbol for the company.
    :param period: Period of the income statement.
    :param limit: Limit of data to retrieve (default: 10).
    :return: JSON formatted data of the income statement.
    """
    url = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?period={period}&limit={limit}&apikey={fmp_key}"
    response = requests.get(url)
    #print(url)
    return json.dumps(response.json())

available_functions = {
    "get_income_statement": get_income_statement,
    "get_balance_sheet_AAPL": get_balance_sheet_AAPL,
    "get_balance_sheet_MSFT":get_balance_sheet_MSFT,
    "get_cash_flow_statement": get_cash_flow_statement,
    "get_key_metrics": get_key_metrics,
    "get_financial_ratios": get_financial_ratios,
    "get_financial_growth": get_financial_growth
}