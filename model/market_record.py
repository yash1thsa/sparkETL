import datetime
from dataclasses import dataclass
from numpy import int32


@dataclass
class MarketRecord:
    ID: str
    Year_Birth: str
    Education: str
    Marital_Status: str
    Income: str
    Kidhome: str
    Teenhome: str
    Dt_Customer: str
    Recency: str
    MntWines: str
    MntFruits: str
    MntMeatProducts: str
    MntFishProducts: str
    MntSweetProducts: str
    MntGoldProds: str
    NumDealsPurchases: str
    NumWebPurchases: str
    NumCatalogPurchases: str
    NumStorePurchases: str
    NumWebVisitsMonth: str
    AcceptedCmp3: str
    AcceptedCmp4: str
    AcceptedCmp5: str
    AcceptedCmp1: str
    AcceptedCmp2: str
    Complain: str
    Z_CostContact: str
    Z_Revenue: str
    Responses: str


@dataclass
class MarketOutputRecord:
    id: int32
    education: str
    marital_status: str
    snapshot_dt: datetime.datetime
