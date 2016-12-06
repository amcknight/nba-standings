DROP TABLE IF EXISTS team_season_scrapes, teams;
CREATE TABLE team_season_scrapes (
  id INT NOT NULL AUTO_INCREMENT,
  team_id INT NOT NULL,
  year SMALLINT NOT NULL,
  status_symbol VARCHAR(4) DEFAULT "",
  wins SMALLINT NOT NULL,
  losses SMALLINT NOT NULL,
  win_percentage DECIMAL(4,3),
  games_behind DECIMAL(5,1) NOT NULL,
  conf_wins SMALLINT NOT NULL,
  conf_losses SMALLINT NOT NULL,
  div_wins SMALLINT NOT NULL,
  div_losses SMALLINT NOT NULL,
  home_wins SMALLINT NOT NULL,
  home_losses SMALLINT NOT NULL,
  road_wins SMALLINT NOT NULL,
  road_losses SMALLINT NOT NULL,
  last10_wins SMALLINT NOT NULL,
  last10_losses SMALLINT NOT NULL,
  streak_type CHAR(1) NOT NULL,
  streak_length SMALLINT NOT NULL,
  scrape_time DATETIME DEFAULT now(),
  PRIMARY KEY (id)
);

CREATE TABLE teams (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(40) NOT NULL,
  conference VARCHAR(30) NOT NULL,
  division VARCHAR(30) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY `team` (`name`,`conference`,`division`)
);