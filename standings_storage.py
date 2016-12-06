import pymysql
import json


class MySQLStandingsStorage:

    select_team_sql = "SELECT `id` FROM `teams` WHERE `name`='%s' AND `conference`='%s' AND `division`='%s';"
    insert_team_sql = "INSERT IGNORE INTO `teams` (`name`, `conference`, `division`) VALUES ('%s', '%s', '%s');"
    insert_scrape_sql = "INSERT INTO `team_season_scrapes` (`team_id`, `year`, `status_symbol`, `wins`, `losses`, `win_percentage`, `games_behind`, `conf_wins`, `conf_losses`, `div_wins`, `div_losses`, `home_wins`, `home_losses`, `road_wins`, `road_losses`, `last10_wins`, `last10_losses`, `streak_type`, `streak_length`) VALUES (%i, %i, '%s', %i, %i, %.3f, %.1f, %i, %i, %i, %i, %i, %i, %i, %i, %i, %i, '%s', %i);"

    def __init__(self, config_path="./config.json"):
        with open(config_path) as c:
            prefs = json.load(c)
            self.username = prefs["username"]
            self.password = prefs["password"]
            self.database = prefs["database"]
            self.sockpath = prefs["sockpath"]

    def store_rows(self, rows):
        try:
            conn = pymysql.connect(user=self.username, password=self.password,
                                   database=self.database,
                                   unix_socket=self.sockpath,
                                   autocommit=True)
            cur = conn.cursor()
            for c in rows:
                found = cur.execute(self.select_team_sql % (c['name'], c['conference'], c['division']))
                if found:
                    tid = cur.fetchone()[0]
                else:
                    cur.execute(self.insert_team_sql % (c['name'], c['conference'], c['division']))
                    tid = cur.lastrowid
                cur.execute(self.insert_scrape_sql % (tid, c['year'], c['status_symbol'], c['wins'], c['losses'], c['win_percentage'], c['games_behind'], c['conf_wins'], c['conf_losses'], c['div_wins'], c['div_losses'], c['home_wins'], c['home_losses'], c['road_wins'], c['road_losses'], c['last10_wins'], c['last10_losses'], c['streak_type'], c['streak_length']))
        finally:
            cur.close()
            conn.close()
