class Query1:
    def q1(con):
        cur=con.cursor()
        cur.execute("SELECT locations.location_id, locations.street_address, locations.city,\
                      locations.state_province, countries.country_name FROM locations\
               INNER JOIN countries ON locations.country_id = countries.country_id\
               WHERE countries.country_name = 'Canada'")
        rec=cur.fetchall()
        for r in rec:
            print(r[0],',',r[1],',',r[2],',',r[3],',',r[4])
            print()
        
