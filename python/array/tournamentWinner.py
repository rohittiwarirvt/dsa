
# https://leetcode.com/problems/tournament-winners/description/

competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"]
  ]


results = [0, 1, 1, 1, 0, 1] # 1 home team win and 0 means away team win

HOME_TEAM_WON = 1


# O(n) time | O(n) s[ace]
def tournamentWinner(competitions, results):
  currentBestTeam =""
  scores = {currentBestTeam: 0}

  for idx, competition in enumerate(competitions):
    result = results[idx]
    homeTeam, awayTeam = competition

    winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

    updateScores(winningTeam, 3, scores)

    if scores[currentBestTeam] < scores[winningTeam]:
      currentBestTeam = winningTeam
  return currentBestTeam



def updateScores(team, points, scores):
  if team not in scores:
    scores[team] =0

  scores[team] +=points


print(tournamentWinner(competitions, results))


