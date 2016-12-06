from pyquery import PyQuery as pq


class StandingsTableParser:
    def extract_row(self, row):
        tds = [td for td in row.children().items()]

        cells = {}
        cells['name'] = tds[0].children('a').eq(0).text()
        cells['status_symbol'] = tds[0].children('sup.super').eq(0).text()
        cells['wins'] = int(tds[1].text())
        cells['losses'] = int(tds[2].text())
        cells['win_percentage'] = float(tds[3].text())
        cells['games_behind'] = float(tds[4].text())
        cells['conf_wins'], cells['conf_losses'] = map(int, tds[5].text().split('-'))
        cells['div_wins'], cells['div_losses'] = map(int, tds[6].text().split('-'))
        cells['home_wins'], cells['home_losses'] = map(int, tds[7].text().split('-'))
        cells['road_wins'], cells['road_losses'] = map(int, tds[8].text().split('-'))
        cells['last10_wins'], cells['last10_losses'] = map(int, tds[9].text().split('-'))
        cells['streak_type'], cells['streak_length'] = tds[10].text().split(' ')
        cells['streak_length'] = int(cells['streak_length'])
        return cells

    def enrich_row(self, year, conference, division, cells):
        cells['year'] = year
        cells['conference'] = conference
        cells['division'] = division

    def parse_table(self, table_html):
        # Get Rows
        standings_rows = table_html.children('tr')
        clean_rows = []
        year = -1
        conference = None
        division = None
        for r in standings_rows.items():
            if r.hasClass('odd') or r.hasClass('even'):
                x = self.extract_row(r)
                self.enrich_row(year, conference, division, x)
                clean_rows.append(x)
            elif r.hasClass('title'):
                division = r.children('td.name').eq(0).text()
            elif r.children('td').eq(0).hasClass('confTitle'):
                conference = r.children('td.confTitle').eq(0).text()
            elif r.children('td').eq(0).hasClass('header'):
                year_td = r.children('td.header')
                year_td('div').remove()
                year_text = year_td.text()
                year = int(year_text.split(' ')[0].split('-')[0])
            else:
                pass  # This shouldn't happen
        return clean_rows

    def parse_page(self, url, query):
        d = pq(url, query)
        standings_table = d.find('table.mainStandings')
        return self.parse_table(standings_table)
