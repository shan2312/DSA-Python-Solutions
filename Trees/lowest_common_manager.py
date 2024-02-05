def getLowestCommonManager(topManager, reportOne, reportTwo):
    lowestCommonManager = None
    
    def checkReports(currentManager, reportOne, reportTwo):
        countFound = 0
        for report in currentManager.directReports:
            countFound += checkReports(report, reportOne, reportTwo)

        iscurrentReport = (currentManager == reportOne or currentManager == reportTwo)
        countReportsFound = (countFound + iscurrentReport)
        if countReportsFound == 2:
            lowestCommonManager = currentManager.name
        print(currentManager, countReportsFound)
        return countReportsFound >= 1
    checkReports(topManager, reportOne, reportTwo)
    return lowestCommonManager
            


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []


inputs = {
  "orgChart": {
    "nodes": [
      {"directReports": ["B", "C"], "id": "A", "name": "A"},
      {"directReports": ["D", "E"], "id": "B", "name": "B"},
      {"directReports": ["F", "G"], "id": "C", "name": "C"},
      {"directReports": ["H", "I"], "id": "D", "name": "D"},
      {"directReports": [], "id": "E", "name": "E"},
      {"directReports": [], "id": "F", "name": "F"},
      {"directReports": [], "id": "G", "name": "G"},
      {"directReports": [], "id": "H", "name": "H"},
      {"directReports": [], "id": "I", "name": "I"}
    ]
  },
  "reportOne": "E",
  "reportTwo": "I",
  "topManager": "A"
}
