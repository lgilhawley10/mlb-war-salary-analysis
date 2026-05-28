import pandas as pd
import matplotlib.pyplot as plt

war_df = pd.read_csv('WarDataset.csv', encoding='latin-1')
salary_df = pd.read_csv('SalaryDataset.csv', encoding='latin-1')

def fix_name(name):
    parts = name.split(", ")
    if len(parts) == 2:
        return parts[1] + " " + parts[0]
    else:
        return name

salary_df["Player"] = salary_df["Player"].apply(fix_name)

war_df["Player"] = war_df["Player"].str.strip()
salary_df["Player"] = salary_df["Player"].str.strip()

salary_df["Average Annual"] = salary_df["Average Annual"].str.replace("$", "", regex = False)
salary_df["Average Annual"] = salary_df["Average Annual"].str.replace(",", "", regex = False)
salary_df["Average Annual"] = salary_df["Average Annual"].str.strip()
salary_df["Average Annual"] = pd.to_numeric(salary_df["Average Annual"], errors = "coerce")

merged_df = pd.merge(war_df, salary_df, on = "Player", how = "inner")

merged_df.to_csv("war_salary_merged.csv", index = False)

merged_df["War Per Dollar"] = merged_df["Total War"] / merged_df["Average Annual"]

small_contracts = merged_df[merged_df["Average Annual"] > 1000000]
underpaid = small_contracts[["Player", "Average Annual", "Total War", "War Per Dollar"]].sort_values("War Per Dollar", ascending = False).head(10)
print(underpaid)

big_contracts = merged_df[merged_df["Average Annual"] > 10000000]
overpaid = big_contracts[["Player", "Total War", "Average Annual", "War Per Dollar"]].sort_values("War Per Dollar", ascending=True).head(10)
print(overpaid)

plt.scatter(merged_df["Average Annual"], merged_df["Total War"])
plt.xlabel("Average Annual Salary")
plt.ylabel("Total WAR")
plt.title("Average Annual Salary vs. Total WAR (2025)")
plt.savefig("WAR_vs_Salary.pdf")
plt.show()

print(salary_df[["Player", "Average Annual"]].head(10))
