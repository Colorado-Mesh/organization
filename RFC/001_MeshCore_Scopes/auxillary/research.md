### Pacific Northwest (PNW Mesh)

Source: https://gessaman.com/meshcore/regions/

```
west                            Entire mesh (Western US / SW Canada)
    pnw                         Pacific Northwest
        wa                      Washington State
            w-wa                Western Washington
                sea             Seattle / Tacoma / Bellevue (King, Pierce, Snohomish)
                oly             Olympia / Lacey / Tumwater (Thurston)
                kit             Kitsap / Bremerton / Silverdale
                grh             Grays Harbor / WA coast
                bvs             Skagit Valley / Mount Vernon / Anacortes
                bli             Bellingham / Whatcom County
            sw-wa               Southwest Washington
                cls             Centralia / Chehalis (Lewis)
                kls             Kelso / Longview (Cowlitz)
            c-wa                Central Washington
                ykm             Yakima (Yakima)
                eat             Wenatchee (Chelan)
                eln             Ellensburg (Kittitas)
                eph             Ephrata (Grant)
            e-wa                Eastern Washington
                geg             Spokane metro
            se-wa               Southeastern Washington
                alw             Walla Walla (Walla Walla)
                puw             Pullman (Whitman, Asotin, Garfield)
                psc             Tri-Cities / Pasco / Kennewick / Richland (Benton, Franklin)
        inw                     Inland Northwest (Spokane WA + N. Idaho panhandle)
            palouse             Palouse (Pullman WA + Moscow/Lewiston/Clearwater ID, cross-border)
            lc                  Lewiston / Clarkston (Nez Perce Co. ID + Asotin Co. WA, cross-border, proposed)
        or                      Oregon
            pdx                 Portland metro (OR + Clark County WA)
            wv                  Willamette Valley
                sle             Salem / Keizer (Marion, Polk)
                cvo             Corvallis / Albany (Benton, Linn)
                eug             Eugene / Springfield (Lane)
            s-or                Southern Oregon
                mfr             Medford / Ashland (Jackson)
                rbg             Roseburg (Douglas)
                lmt             Klamath Falls (Klamath)
            coast-or            Oregon Coast
                onp             Newport / Lincoln City (Lincoln)
                ast             Astoria / Seaside (Clatsop)
                otk             Tillamook (Tillamook)
                oth             North Bend / Coos Bay (Coos)
            c-or                Central Oregon
                ben             Bend / Redmond (Deschutes)
                pdt             Pendleton (Umatilla)
                bke             Baker City (Baker)
        id                      Idaho (Moscow / Lewiston / Clearwater carry id directly — no dedicated metro tag)
            boi                 Boise metro
            cda                 Coeur d'Alene / N. Idaho panhandle
        mt                      Montana (partial — statewide expansion planned)
            fca                 Flathead Valley / Kalispell / Glacier (Glacier Park Intl)
        bc                      British Columbia (southern)
            swbc                Southwest BC / Lower Mainland
            vanisle             Vancouver Island
                southisland     South Vancouver Island / Victoria
            salishmesh          Salish Sea / Gulf Islands
```

Design Principles:
  - Short names: Region names are purely administrative — they never appear in flood packets. But shorter names are easier to type in CLI, easier to remember, and conserve the 172-byte budget in the regions response payload. Three letters or fewer where possible.
  - MSA-scale regions: The third level corresponds roughly to OMB Metropolitan Statistical Areas rather than individual counties. People don't segment their daily lives by county lines, and the mesh shouldn't either. The Seattle-Tacoma-Bellevue MSA (King, Pierce, Snohomish counties) is one region: sea.
  - Flat naming: west, pnw, wa, sea — not a complex string like west-pnw-wa-sea or noam-usa-wa-sea. The hierarchy lives in the parent relationships, not the strings.
  - Cross-border pragmatism: Portland straddles OR/WA — it lives under or, and Clark County WA repeaters dual-carry pdx and wa. The Inland Northwest straddles WA/ID and uses the same dual-carry pattern. Vancouver BC uses community-established region tags (swbc, vanisle, southisland, salishmesh) rather than IATA codes to reflect the actual geographic communities that have formed on the mesh.


Technical Constraints:
- Characters allowed: Lowercase a-z, 0-9, hyphen
- Max name length: 29 bytes (UTF-8)
- Max regions per repeater: 32
- Regions response budget: 172 bytes (comma-separated names)
- Region names must be unique within the mesh

Region names have zero impact on packet size or airtime

Region names are transmitted only in response to an explicit anonymous regions request (`ANON_REQ` type `0x01`). This is a direct-routed, rate-limited exchange (max 4 anonymous requests per 180 seconds). The response carries a comma-separated list of region names that allow flooding, with a 172-byte budget.

Budget example for a typical repeater:

```west,pnw,wa,w-wa,sea = 20 bytes including commas (152 bytes remaining)```

A repeater with sub-region depth in Oregon:

```west,pnw,or,wv,sle = 18 bytes (154 bytes remaining)```

Even a heavily tagged border repeater stays well within budget:

```west,pnw,or,pdx,wa,sw-wa = 24 bytes (148 bytes remaining)```

### MWMesh (Utah)

```
*
└── us
    └── ut
        ├── wasatch
        │   ├── slc
        │   ├── ut-county
        │   └── davis-weber
        ├── northern-ut
        ├── central-ut
        ├── eastern-ut
        └── southern-ut
```

### Nebraska Mesh

```
all
    ne
        (iata)
```

Currently the idea is to make regions by IATA based on county lines. There will be a NE statewide region and an ALL region. The plan is to block unscoped messaging across state lines in order to control traffic in our areas and also so we’re not forcing our mesh onto other states.

### NashMesh (Nashville, TN)

Source: https://nashme.sh/getting-started/meshcore/#proposed-regions

```
*                               flood, any/default channels
    us                          country-wide, Public, #bot, #test
        us-southeast            country region, neighboring states, Public, #bot, #test
            us-tn               state, statewide channels
                us-tn-middle    state division, relevant channels
                    us-tn-bna   IATA metro, aligned with MeshMapper
nashmesh - Standalone, local/tactical
```

TIP: Can discover regions: https://nashme.sh/getting-started/meshcore/#tips

### CT Mesh (Connecticut) / New England Mesh

Source: https://ctmesh.org/repeater-setup#program-mesh-settings

Source: https://newenglandme.sh/regions/

Source: https://newenglandme.sh/regions/map

```
east
    northeast
        ct          Connecticut (state)
        me          Maine (state)
        nh          New Hampshire (state)
        vt          Vermont (state)
        ri          Rhode Island (state)
        erie        Erie (part of New York)
        nyc         NYC (part of New York)
        li          Long Island (part of New York)
        ct-rv       Connecticut River Valley (inter-state region)
        ...
```

Takeaways:
- Relatively flat design
- Some states are small enough to be their own regions
- There is no state-wide region for larger states, instead just subdivisions
- Regions do not stop at state borders (more geography-based)
- Regions overlap (not via hierarchy)

### Boston Mesh (Boston, MA)

Source: https://bostonme.sh/docs/MeshCore/meshcore-regions

Largely shared with CT and New England

```
Use these region names for Greater Boston Mesh deployments:

    ma (Massachusetts)
    me (Maine)
    ri (Rhode Island)
    vt (Vermont)
    nh (New Hampshire)
    ct (Connecticut)

Also add:

    newengland (regional scope)
    us (national scope)

When deploying a repeater, add newengland and us at the same time you add the state region.
```

### Florida Mesh

Source: https://areyoumeshingwith.us/docs/meshcore/regional-settings/#region-scopes

```
us
    us-southeast
        us-{state}
            us-{state}-{subregion}
    us-iata
```