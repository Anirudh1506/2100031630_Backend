class Query2:
    def q2(con):
        cur=con.cursor()
        cur.execute("SELECT location_id, street_address, city, state_province, country_name\
                     FROM locations, countries\
                     WHERE locations.country_id = countries.country_id AND countries.country_name = 'Canada'")
        rec=cur.fetchall()
        for r in rec:
            print(r[0],',',r[1],',',r[2],',',r[3],',',r[4])
            print()