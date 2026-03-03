from openpyxl import Workbook

# ----------------------------
# Performance Weights
# ----------------------------
weights = {
    "CP": 1,
    "GT": 2,
    "C": 5,
    "DC": -4,
    "ST": 6,
    "RO": 6,
    "MRO": -3,
    "DH": 4
}

# ----------------------------
# Sample Data Collection
# (Replace with actual match data)
# ----------------------------
data = [
    # MatchNo, Innings, Team, Player, Ballcount, Position,
    # Description, Pick, Throw, Runs, Overcount, Venue
    
    [1, 1, "Pakistan", "Shadab Khan", 1, "Point",
     "Clean pick and quick release", "CP", "MRO", 2, 5, "Melbourne"],
    
    [1, 1, "Pakistan", "Mohammad Rizwan", 2, "Wicketkeeper",
     "Stumping chance taken", "C", "ST", 0, 8, "Melbourne"],
    
    [1, 1, "Pakistan", "Babar Azam", 3, "Cover",
     "Dropped catch", "DC", "", -4, 10, "Melbourne"]
]

# ----------------------------
# Calculate Performance Score
# ----------------------------
def calculate_score(player_name):
    CP = GT = C = DC = ST = RO = MRO = DH = RS = 0

    for row in data:
        if row[3] == player_name:
            pick = row[7]
            throw = row[8]
            runs = row[9]

            if pick == "CP": CP += 1
            if pick == "GT": GT += 1
            if pick == "C": C += 1
            if pick == "DC": DC += 1

            if throw == "ST": ST += 1
            if throw == "RO": RO += 1
            if throw == "MRO": MRO += 1
            if throw == "DH": DH += 1

            RS += runs

    PS = (
        CP * weights["CP"] +
        GT * weights["GT"] +
        C * weights["C"] +
        DC * weights["DC"] +
        ST * weights["ST"] +
        RO * weights["RO"] +
        MRO * weights["MRO"] +
        DH * weights["DH"] +
        RS
    )

    return PS

# ----------------------------
# Save to Excel
# ----------------------------
wb = Workbook()
ws = wb.active
ws.title = "Fielding Data"

headers = ["Match No", "Innings", "Team", "Player Name", "Ballcount",
           "Position", "Short Description", "Pick", "Throw",
           "Runs", "Overcount", "Venue"]

ws.append(headers)

for row in data:
    ws.append(row)

# Summary Sheet
summary = wb.create_sheet("Performance Summary")
summary.append(["Player Name", "Performance Score"])

players = list(set([row[3] for row in data]))

for player in players:
    score = calculate_score(player)
    summary.append([player, score])

wb.save("Cricket_Fielding_Analysis.xlsx")

print("Fielding analysis completed and saved successfully.")