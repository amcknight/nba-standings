from standings_parser import StandingsTableParser
from standings_storage import MySQLStandingsStorage


def main():
    # Get HTML
    base = "http://www.nba.com"
    years = [2012, 2013, 2014]
    stem = "/".join(["standings", "%i", "team_record_comparison"])
    page = "conferenceNew_Std_Div.html"
    query = {'ls': 'iref:nba:gnav'}
    standings_url = "/".join([base, stem, page])

    # Get Table from Scrape
    parser = StandingsTableParser()
    rows = []
    for year in years:
        rows += parser.parse_page(standings_url % year, query)

    # Store it
    store = MySQLStandingsStorage()
    store.store_rows(rows)


if __name__ == "__main__":
    main()
