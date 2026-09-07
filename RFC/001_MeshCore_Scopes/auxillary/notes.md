```
*                                   Flood traffic / default / any
us                                  Entire United States - DOES NOT CONFLICT WITH A CITY
    west                            Western US (and Canada) - DOES NOT CONFLICT WITH A CITY
        mnw                         Mountain West (UT, CO, WY, MT, ID, NV) - DOES NOT CONFLICT WITH A CITY
            co                      Colorado (state-wide)
                [State Divisions - `co` + 2-letter abbr]
                co-ws               Western Slopes region (Colorado)
                co-fr               Front Range region (Colorado)
                co-ep               Eastern Plains region (Colorado)
                co-cm               Central Mountains region (Colorado)
                co-sl               San Luis Valley region (Colorado)
                [Counties - `co` + 3-letter abbr]
                co-adm              Adams County (Colorado)
                [Cities - <=5 letter abbr]      DOES NOT CONFLICT WITH ANY MOUNTAINS
                den                 Denver (not to be confused with `iata-den`)
                fnl                 Fort Collins (not to be confused with `iata-fnl`)
                cmrce               Commerce City
                [Mountains - <=5 letter abbr]   DOES NOT CONFLICT WITH ANY CITIES
                pikes               Pikes Peak
iata-den                            DEN IATA code
iata-fnl                            FNL IATA code
iata-pub                            PUB IATA code
        
```

### 09-06-2026

- Multiple levels above CO doesn't hurt anyone, helps interstate traffic with agreed-upon standards and future expansion
- High number of levels won't hurt transport
  - Any given packet will only be tagged with one ~3 character region
    - Cities will use <=5 abbr
    - Mountains as well if needed
  - Hierarchy only comes into play when requesting region list from a repeater
    - e.g. A repeater many levels down, e.g. ```us,west,mnw,co,co-fr,co-adm,cmrce,pikes,iata-den``` - 47 chars/bytes (out of 172 total possible) (I know, Pikes Peak isn't near Commerce City, it's just an example)
      - Most/all geographic/administrative zones defined by this point (country, country-region, country-subregion, state, geo, county, city, potential mountain, iata)
      - Leaves 125 chars/bytes for any other bespoke scopes a given repeater operator wants to add support for
  
- The shorter abbreviation, the better (easier to type and read, save the 172-byte budget in region response payload).
- Broad Colorado geographic regions, by counties (source: https://gis.dola.colorado.gov/RegionsMap/)
  - Western Slopes (Archuleta, Delta, Dolores, Eagle, Garfield, Grand, Gunnison, Hinsdale, Jackson, La Plata, Mesa, Moffat, Montezuma, Montrose, Ouray, Pitkin, Rio Blanco, Routt, San Juan, San Miguel, Summit)
  - Front Range (Adams, Arapahoe, Boulder, Broomfield, Denver, Douglas, El Paso, Jefferson, Larimer, Pueblo, Teller, Weld)
  - Eastern Plains (Baca, Bent, Cheyenne, Crowley, Elbert, Kiowa, Kit Carson, Lincoln, Logan, Morgan, Otero, Phillips, Prowers, Sedgwick, Washington, Yuma)
  - Central Mountains (Chaffee, Clear Creek, Custer, Fremont, Gilpin, Huerfano, Lake, Las Animas, Park)
  - San Luis Valley (Alamosa, Conejos, Costilla, Mineral, Rio Grande, Saguache)
  - Other divisions (8 for tourism PR, 14 for regional administrative work, etc.) not as immediately human-readable
- Reserve IATA codes for top-level (not nested since unique across entire country), prefix with `iata-` for clarity (avoid confusion between, e.g. `den` city and `iata-den` airport)
- Region codes need to be unique to "the mesh" (the within-range mesh):
  - Make sure city and county region codes along state borders don't clash (e.g. a `cen` in Colorado near a `cen` in Utah allowing a pass)

### 09-07-2026

- Remember, scopes aren't about reaching the destination, it's about how far it leaves from the source
- Drop counties, instead encourage county-specific channels (one county's traffic accidentally making it to another county isn't a problem as long as it's not abusing bandwidth)
- City / mountain scopes too specific and niche
- Add statistical region set (based on OMB: https://en.wikipedia.org/wiki/Colorado_statistical_areas) (in additional to existing geographic regions)

Example repeater config (Denver): `us,west,mnw,co,co-fr,co-den,iata-den`
  - Part of United States
  - Part of western United States
  - Part of Mountain West
  - Part of Colorado
  - Part of Front Range geographic zone in Colorado
  - Part of Denver-Aurora-Centennial metropolitan statistical zone in Colorado
  - Part of Denver Internal Airport IATA zone (closest airport)

36 characters for all zones (note: some border repeaters might fall into multiple IATA codes or multiple geographical/statistical zones; at most three of each) - leaves (172 - 36 = 136) chars / bytes for bespoke scopes

### 09-09-2026

- Drop statistical zones due to name confusion with IATA codes
- Replace `iata-` prefix with `co-` and move to under `co` topic
  - These regions (e.g. `co-fnl`) began built around IATA codes. Now that the Colorado Mesh naming scheme is designed around them, they have become de-facto "Colorado Mesh-wide regions"
    - This also allows for potential drift in the future. For example, `co-fnl` does not ALWAYS have to perfectly align with the FNL IATA airport code region.
    - The borders of these IATA zones was always subjective to begin with, in the sense that Colorado Mesh the group decided and agreed on the methodology to draw the borders in the first place (based on "as the crow flies" distance from a central point, instead of say, vibes, per-city, based on roads, accounting for mountains and obstacles, etc.)