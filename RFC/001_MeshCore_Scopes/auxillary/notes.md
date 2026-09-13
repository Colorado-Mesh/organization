```
*                                   Flood traffic / default / any
us                                  Entire United States - DOES NOT CONFLICT WITH A CITY
    west                            Western US (and Canada) - DOES NOT CONFLICT WITH A CITY
        mnw                         Mountain West (UT, CO, WY, MT, ID, NV) - DOES NOT CONFLICT WITH A CITY
            co                      Colorado (state-wide)
                [State Divisions - `co` + 2-letter abbr]
                co-ws               Western Slope region (Colorado)
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
  - Western Slope (Archuleta, Delta, Dolores, Eagle, Garfield, Grand, Gunnison, Hinsdale, Jackson, La Plata, Mesa, Moffat, Montezuma, Montrose, Ouray, Pitkin, Rio Blanco, Routt, San Juan, San Miguel, Summit)
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


### 09-11-2026

#### Inter-State Compatibility

Unfortunately states disagree on the best top-level key (country-wide versus country-region-wide)

```
west - Would allow traffic to Washington, Oregon, Montana, British Columbia, Northwestern Idaho (via PNW Mesh)
  - Would not be able to reach through Utah because Utah/Southern Idaho do not use the `west` scope
imw - Would allow traffic to Utah, Southern Idaho, Nevada (via MWMesh) (Half of Colorado is considered IMW: https://en.wikipedia.org/wiki/Intermountain_West)
ne - Would allow traffic to Nebraska (or use `all`)
east - Would allow traffic to Connecticut, New England
us - Would allow traffic to Tennessee, Florida, Boston
```

Again, scopes are about the origin, not the destination. You don't tag a message with `east` because you want it to reach Florida.
If that were the case, every repeater across the state would need to support every state and region's scopes.

No, it's about "how far from here do I want this message to continue repeating". In that case, immediate state borders are still applicable, but would only be applied to repeaters on the edges.
If someone in Grand Junction wants to reach Nebraska by way of Denver, that's a job for flooding, not scopes.

Remember, flooding still exists, and will likely remain the primary scope for the foreseeable future.

#### Intermountain West

The following Colorado geographic zones would also accompany the `imw` tag to be included in the Intermountain West region (used by Utah, Idaho and Nevada):
  - Western Slope
  - Central Mountains
  - San Luis Valley

#### Expand Geographic Region Names

Initially, we wanted to keep each scope as short as possible to preserve as much of the 172 total bytes/characters available for storing all configured scopes

A community member pointed out (ref: https://github.com/meshcore-dev/MeshCore/blob/main/docs/packet_format.md) that a given scope can be up to 29 bytes, which after hashing will add 4 bytes to the message length, regardless of whether it is 1 character or 29 characters (no scope = 0 bytes added).

With that in mind, we have more room to work with in the scope names.

Propose making geographic scopes more readable:
  - `co-frontrange` (13)
  - `co-westslope` (12)
  - `co-mountains` (12)
  - `co-slvalley` (11)
  - `co-eastplains` (13)

#### IATA Codes

Add back the `iata-` prefix for IATA codes (also Colorado Mesh defined regions). This will avoid confusion between city names and airport codes
  - e.g. `co-den` could be interpreted as Denver, Colorado rather than Denver International Airport region, which expands beyond just Denver
  - This will also avoid conflicts when city-level codes are inevitably created (including `den`)

#### Adding United States National Grid Codes

Average users likely won't use it, but it would be a great selling point to EMS if the network supported the standard United States National Grid (USNG: https://en.wikipedia.org/wiki/United_States_National_Grid).
  - > Since 2011 the USNG has been designated by the US Government's National Search and Rescue Committee (NSARC) as the primary coordinate reference system to be used for all land-based search and rescue (SAR) activities in the US.
  - > In 2015, the Federal Emergency Management Agency (FEMA) issued FEMA Directive 092–5, "Use of the United States National Grid (USNG)":[23] "POLICY STATEMENT: FEMA will use the United States National Grid (USNG) as its standard geographic reference system for land-based operations and will encourage use of the USNG among whole community partners."


REFS:
  - https://mmdolbow.github.io/usng-gmap-v3/
  - https://www.fgdc.gov/usng
  - https://usngcenter.org/
  - https://mappingsupport.com/p2/gissurfer.php (compare against UTM to see they line up, at least at the 100 square km mark)

Each repeater could have a code with precision 10,000 square meters (100 square km = ~62 square miles), based on the latitude/longitude of the repeater converted to the USNG, which will produce 5-character codes.
  - No city in Denver is larger than 60 square miles, making it big enough for city and county officials to effectively use as wide-reaching.

For example, a repeater at `39.856254, -104.670266` (Denver International Airport) would have the USNG code `13SEE` as a region code.

The majority of Colorado fits mostly in the `13S` square of the USNG, with everything north of Denver in `13T`, and everything from Grand Junction to the Utah border fitting in `12S` and `12T`.
  - Because of this, additionally including a higher level code (e.g. `13S`) feels redundant (just use `co` at that point)
  - Unfortunately, Denver is nearly perfectly at the intersection of `13SDE`, `13SDD`, `13SEE` and `13SED`, and anything north of Lafayette becomes `13TDE`/`13TEE`, go figure.
  - Fort Collins and Colorado Springs are also hugging grid square borders, and Grand Junction is squished between `12S` and `13S`. What do you expect from a state that's not actually a rectangle?

A number of online maps and tools exist to convert a latitude/longitude or address to a USNG code, and the Colorado Mesh configurator tool would use an existing JavaScript library (https://github.com/klassenjs/usng_tools) or Python library (https://pypi.org/project/pyutm/) to calculate this.
  - Users would need to enter the approximate lat/long of their repeater. Calculation is done entirely on-device (no sensitive data is sent or stored about the repeater location), and the 100 square kilometer area does not reveal the exact location of a repeater.

#### Bytes Total

With these adopted changes, a maxed-out repeater could have configured as scopes:

- `us`
- `west`
- `co`
- `imw` (near Utah) (or `ne` (near Nebraska))
- `co-eastplains` (max 13 letters)
- `iata-xxx`, `iata-xxx` and `iata-xxx` (near border of 3 IATA regions)
- `13SXX` (USNG code)
  - Potentially 9 codes to support neighboring grids - Any repeater would then be in the center of a 300 square kilometer (~186 square miles) area
  - Ex:
    - Repeater A has codes 0, 1, 2
    - Repeater B has codes 1, 2, 3
    - Repeater C has codes 2, 3, 4
    - A message with scope `2` sent via Repeater A would jump to Repeater B, and then to Repeater C
    - A message with scope `1` sent via Repeater A would jump to Repeater B, but NOT jump to Repeater C
    - A message with scope `0` sent via Repeater A would NOT jump to Repeater B or Repeater C
    - The same in the three other cardinal directions
  - Consideration needed where a repeater's neighboring zone is a different prefix (e.g. from `13S` to `12S` west of Grand Junction, `13S` to `13T` north of Lafayette)

Total: 2 + 4 + 2 + 3 + 13 + (8*3) + 5 = 53 characters for a heavily-scoped repeater, still leaving 119 characters for bespoke scopes
  - 2 + 4 + 2 + 3 + 13 + (8*3) + (5*9) = 93 characters if we want to support neighboring USNG grid squares, leaving 79 characters for bespoke scopes