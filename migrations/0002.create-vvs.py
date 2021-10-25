from yoyo import step
steps = [
   step(
       "CREATE TABLE vvs (id INT, bar VARCHAR(20), PRIMARY KEY (id))",
       "DROP TABLE vvs"
   )
]